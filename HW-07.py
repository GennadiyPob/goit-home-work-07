'''Задача 01 - Створення функції з параметрами словника'''

# from setuptools import setup


# def do_setup(args_dict):
#     setup(**args_dict)

# args_dict = {
#     "name": "useful",
#     "version": "1",
#     "description": "Very useful code",
#     "url": "http://github.com/dummy_user/useful",
#     "author": "Flying Circus",
#     "author_email": "flyingcircus@example.com",
#     "license": "MIT",
#     "packages": ["useful"]
# }         

'''Задача 02 - прописуємо додаткові параметри'''

# from setuptools import setup

# def do_setup(args_dict, requires):
#     setup(name=args_dict['name'],
#           version=args_dict['version'],
#           description=args_dict['description'],
#           url=args_dict['url'],
#           author=args_dict['author'],
#           author_email=args_dict['author_email'],
#           license=args_dict['license'],
#           packages=args_dict['packages'],
#           install_requires = requires)

'''Задача 03 - список "точок входу" для ключа console_scripts'''

# from setuptools import setup

# def do_setup(args_dict, requires, entry_points):
#     setup(name=args_dict['name'],
#           version=args_dict['version'],
#           description=args_dict['description'],
#           url=args_dict['url'],
#           author=args_dict['author'],
#           author_email=args_dict['author_email'],
#           license=args_dict['license'],
#           packages=args_dict['packages'],
#           install_requires=requires,
#           entry_points = {'console_scripts': ['helloworld = useful.some_code:hello_world']}
#           )

'''Задача 04 - перевірка цифр в рядку'''

# def is_integer(s):
    
#     if len(s) == 0:
#         return False
#     s = s.strip()  # Видаляємо початкові та кінцеві прогалини
#     if not s:
#         return False  # Рядок пустий, отже, не є цілим числом
    
#     # Перша цифра або може бути "+" або "-"
#         s = s[1:]#     if s[0] == '+' or s[0] == '-':
  # Відкидаємо перший символ
    
#     return s.isdigit()  # Перевіряємо, чи всі залишившіся символи - цифри
        

'''Задача 05 - ВЕЛИКА ЛІТЕРА. ПОВТОРЕННЯ ФУНКЦІЙ'''

# def capital_text(s):
#     new_s = ""
#     capitalize_next = True #індикатор потреби заміни букви
    
#     for char in s:
#         if char.isalpha():
#             if capitalize_next:
#                 new_s += char.upper()
#                 capitalize_next = False
#             else:
#                 new_s += char.lower()
#         else:
#             new_s += char
#             if char in ".!?":
#                 capitalize_next = True
                
#     return new_s

# # Запуск фунції
# input_text = "hi! what is your name? i hope you're doing well."
# output_text = capital_text(input_text)
# print(output_text)

'''Задача 06 -  ребус "Знайди слово"'''

# def solve_riddle(riddle, word_length, start_letter, reverse=False):
#     if reverse:
#         riddle = riddle[::-1]
        
#     for i in range(len(riddle) - word_length + 1):
#         if riddle[i] == start_letter:
#             potential_word = riddle[i:i + word_length]
#             if potential_word.isalpha():
#                 return potential_word
    
#     return ""

# # Тестуємо функцію
# riddle = "нетдомкратос"
# word_length = 7
# start_letter = "д"
# reverse = False
# result = solve_riddle(riddle, word_length, start_letter, reverse)
# print(result)  # Output: "домкрат"



'''Задача 07 - позбавитися екстремальних значень, перш ніж почати працювати з даними далі ''' 

# def data_preparation(list_data):
#     new_list =[]
#     for lower_list in list_data:
#         if len(lower_list) > 2:
#             lower_list.remove(max(lower_list))
#             lower_list.remove(min(lower_list))
#         new_list.extend(lower_list)

#     return sorted(new_list, reverse=True)


'''Задача 08 - РОЗБИТТЯ РЯДКА НА ЛЕКСЕМИ'''

# def token_parser(s):
#     tokens = []
#     current_token = ''

#     for char in s:
#         if char.isdigit():
#             current_token += char
#         else:
#             if current_token:
#                 tokens.append(current_token)
#                 current_token = ''
#             if char.strip():
#                 tokens.append(char)

#     if current_token:
#         tokens.append(current_token)

#     return tokens

'''Задача 09 - РОБОТА З ВКЛАДЕНИМИ СПИСКАМИ'''
# def all_sub_lists(data):
#     result = [[]]
#     #print('len lst = ', len(data))
#     for i in range(len(data)):
#         #print('i = ', i)
#         for j in range(i + 1, len(data) + 1):
#             #print('j = ', j)
#             result.append(data[i:j])
#             #print('sub_lists = ', result)
#             result.sort(key=len)
#     return result

# original_list = [4, 6, 1, 3]
# result = all_sub_lists(original_list)
# print(result)

'''Задача 10 - РОБОТА З ВКЛАДЕНИМИ СПИСКАМИ'''

# def make_request(keys, values):
    
#     if len(keys) != len(values):
#         return {}

#     request_data = {}
#     for i in range(len(keys)):
#         request_data[keys[i]] = values[i]

#     return request_data

'''Задача 11 - Кнопковий телефон (букви)'''

# def sequence_buttons(string):
# # Створення словника, де ключ - номер кнопки, значення - символи, що відповідають кнопці
#     button_mapping = {
#         '1': '.,?!:',
#         '2': 'ABC',
#         '3': 'DEF',
#         '4': 'GHI',
#         '5': 'JKL',
#         '6': 'MNO',
#         '7': 'PQRS',
#         '8': 'TUV',
#         '9': 'WXYZ',
#         '0': ' '
#     }
#     # Ініціалізація порожнього рядка для збереження послідовності кнопок
#     sequence = ''
#     # Ітеруємося по кожному символу вхідного тексту
#     for char in string:
#         # Переведення символу у верхній регістр
#         char_upper = char.upper()
#         # Пошук кнопки, яка містить символ в наборі
#         for button, chars in button_mapping.items():
         
#             if char_upper in chars:
#                 # Визначення кількості натискань на кнопку
#                 press_count = chars.index(char_upper) + 1
#                 # Додавання кнопки до послідовності відповідно до кількості натискань
#                 sequence += button * press_count
#                 # Зупинка пошуку для поточного символу
#                 break
    
#     return sequence

# # Приклад використання
# input_text = "Hello, World!"
# result_sequence = sequence_buttons(input_text)
# print(result_sequence)  # Виведе: 4433555555666110966677755531111

'''Задача 12 - Кнопковий телефон (букви)'''

# def file_operations(path, additional_info, start_pos, count_chars):
#     # Додавання додаткової інформації до файлу
#     with open(path, 'a') as file:
#         file.write(additional_info)
    
#     # Читання позиції з файлу
#     with open(path, 'r') as file:
#         # Встановлення позиції за допомогою методу seek
#         file.seek(start_pos)
#         # Читання та повернення відповідної кількості символів за допомогою методу read
#         result = file.read(count_chars)
    
#     return result

# # Приклад використання
# file_path = 'example.txt'
# additional_info = 'Additional information.\n'
# start_position = 10
# chars_to_read = 20

# result_string = file_operations(file_path, additional_info, start_position, chars_to_read)
# print(result_string)

'''Задача 13 - Пошук даних у файлі '''

# def get_employees_by_profession(path, profession):
#     # Відкриваємо файл за допомогою менеджера контексту для читання
#     with open(path, 'r') as file:
#         # Отримуємо всі рядки з файлу
#         lines = file.readlines()
    
#     # Знаходимо рядки, де є вказана професія, і додаємо імена з цих рядків до списку
#     matched_names = [line.split()[0] for line in lines if profession in line]
    
#     # Об'єднуємо імена в одну строку, розділену пробілами
#     result = ' '.join(matched_names)
    
#     return result

# Приклад використання
# file_path = 'employees.txt'
# desired_profession = 'cook'

# employees_with_profession = get_employees_by_profession(file_path, desired_profession)
# print(employees_with_profession)

'''Задача 14 - Пошук даних у файлі '''

# def flatten(input_list):
#     # Якщо вхідний список порожній, повертаємо порожній список
#     if not input_list:
#         return []

#     # Якщо перший елемент є списком
#     if isinstance(input_list[0], list):
#         # Рекурсивно викликаємо функцію для першого елемента
#         first_list = flatten(input_list[0])
#         # Рекурсивно викликаємо функцію для решти списку
#         rest_list = flatten(input_list[1:])
#         # Повертаємо конкатенацію першого та решти списку
#         return first_list + rest_list
#     else:
#         # Отримуємо перший елемент списку
#         first_element = input_list[0]
#         # Рекурсивно викликаємо функцію для решти списку
#         rest_list = flatten(input_list[1:])
#         # Повертаємо конкатенацію першого елемента та решти списку
#         return [first_element] + rest_list

# # Приклад використання
# nested_list = [1, 2, [3, 4, [5, 6]], 7]
# flattened_list = flatten(nested_list)
# print(flattened_list)

'''Задача 15 - Рекурсія -вирівнювання списків '''

# def flatten(data):
    
#     # Якщо вхідний список порожній, повертаємо порожній список
#     if not data:
#         return []

#     # Якщо перший елемент є списком
#     if isinstance(data[0], list):
#         # Рекурсивно викликаємо функцію для першого елемента
#         first_list = flatten(data[0])
#         # Рекурсивно викликаємо функцію для решти списку
#         rest_list = flatten(data[1:])
#         # Повертаємо конкатенацію першого та решти списку
#         return first_list + rest_list
#     else:
#         # Отримуємо перший елемент списку
#         first_element = data[0]
#         # Рекурсивно викликаємо функцію для решти списку
#         rest_list = flatten(data[1:])
#         # Повертаємо конкатенацію першого елемента та решти списку
#         return [first_element] + rest_list

'''Задача 16 - Декодування '''

def decode(encoded_list):
    def recursive_decode(index):
        # Якщо індекс виходить за межі списку, повертаємо порожній список
        if index >= len(encoded_list):
            return []

        current_item = encoded_list[index]
        
        # Якщо поточний елемент є числом, це означає кількість повторів
        if isinstance(current_item, int):
            repeated_item = encoded_list[index + 1]
            decoded_group = [repeated_item] * current_item
            # Рекурсивно викликаємо декодування для наступних елементів
            return decoded_group + recursive_decode(index + 2)
        else:
            # Рекурсивно викликаємо декодування для наступних елементів
            return [current_item] + recursive_decode(index + 1)
    
    return recursive_decode(0)

# Приклад використання
encoded_list = ["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]
decoded_list = decode(encoded_list)
print(decoded_list)

