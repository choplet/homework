'''
Нужно сгенерировать все числа из трех цифр, которые состоят из:

Цифр от 1 до 9.
Цифры идут в порядке возрастания.
Числа, которые подходят под указанные выше условия: 118, 127, 136, 145, 226, 235, 244, 334

Вам нужно написать функцию, которая получает 2 аргумента:

Сумма цифр числа.
Количество цифр в числе.
Функция должна выводить массив с тремя значениями

Сумма всех возможных комбинаций.
Минимальное число
Максимальное число
Например:
Вход	Выход
findAll(10, 3)

[8, 118, 334]

findAll(27, 3)

[1, 999, 999]

findAll(84, 4)

[]

findAll(35, 6)

[123, 116999, 566666]
'''

def findAll(sum_komb, amount_numb):
    
