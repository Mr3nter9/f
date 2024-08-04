def find_line_with_word(file_path, target_word):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if target_word in line:
                return line.strip()  # ترجع السطر وتزيل الفراغات الزائدة
    return None

# مثال على الاستخدام
file_path = 'd.txt'  # استبدل هذا بمسار الملف الخاص بك
target_word = 'Qamar242'  # استبدل هذا بالكلمة التي تبحث عنها

result = find_line_with_word(file_path, target_word)

if result:
    print(f'السطر الذي يحتوي على الكلمة هو: {result}')
else:
    print('لم يتم العثور على الكلمة في الملف.')
