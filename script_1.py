import math #імпорт стандартного модуля math

def get_lenght(d):
    lenght = math.pi * d  #імпорт значення числа pi з модуля math
    print(f'Diameter = {d} lenght = {lenght}')

if __name__ == '__main__':
    get_lenght(50)

# конструкція if __name__ == '__main__': має бути обов'язкова
# для функцій що можуть імпортуватися. Це потрібно щоб фунція
# НЕ виводила розрахунки в основному файл, тобто не було видно
# результату озрахунку get_lenght(50)    