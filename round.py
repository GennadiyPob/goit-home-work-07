from math import pi

# round
number = pi
rounded_number = round(number, 5)  # Округлення до 5 знаків після коми
print(rounded_number)  # Виведе: 3.14159


# formatted
number = pi
formatted_number = "{:.5f}".format(number)  # Округлення до 5 знаків після коми
print(formatted_number)  # Виведе: "3.14159"

# f-рядки (Python 3.6 і вище)
number = 3.14159265
precision = 5
formatted_number = f"{number:.{precision}f}"  # Округлення до 5 знаків після коми
print(formatted_number)  # Виведе: "3.14159"

