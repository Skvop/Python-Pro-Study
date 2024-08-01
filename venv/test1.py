# Функция показывает длину строки которую ей передаем
import random
def lenght_of_word(test_word):
    print(f"The length of {test_word} is {len(test_word)}")


# Функция возвращает объединение двух строк
def concatenation():
    string1 = input("Enter 1st line:\n")
    string2 = input("Enter 2nd line:\n")
    print(f"{str(string1) + str(string2)} ")

# Функция возвращает квадрат числа
def square(number):
    print(number**2)

# Функция возвращает сумму чисел
def summ_(num1, num2):
    print(int(num1) + int(num2))


# Функция возвращает целую часть и остаток от деления двух чисел
def action(num1, num2):
    print(int(num1)%int(num2))
    print(int(num1)//int(num2))


# Функция считает среднее арифметическое списка
def average(list1):

    aver = 0
    for part in list1:
        aver = aver + part
    meaning_average = aver / len(list1)
    print(meaning_average)


# Создает список со случайными числами. Это для легкости проверки некоторых следующих функций
def create_rand_list():
    testlist = []
    for i in range(10):
        testlist.append(random.randint(0, 10))
    return testlist


# Функция возвращает списокб который имеет общие элементы двух списков
def common(list1,list2):
    common_list = []
    for i in list1:
        for iter in list2:
            if i == iter:
                common_list.append(iter)
    print(common_list)


# Выводит ключи словаря
def show_keys (dict = {}):
    for i in dict.keys():
        print(i)


# Возвращает объединение двух словарей
def merging_dictionaries(dict1={},dict2={}):
    combined_dict = dict1 | dict2

    print(combined_dict)

# Возвращает объединение двух множеств
def merging_sets (set1 = (), set2 = ()):
    merg_set = set1 + set2
    print(merg_set)



# Проверкаб есть ли одно множество подмножеством другого
def comparison_of_sets(set1,set2):
    return print(all(element in set2 for element in set1))


# Выводит парность числа
def doubles(income_number = nt):
    if income_number % 2 == 0:
        print("income_number is double")
    else:
        print("income_number is  not double")


# Выводит список только парных чисел из двух списков
def union(list_input) :
    list_output = []
    for i in list_input:
        if i % 2 == 0:
            list_output.append(i)
        else:
            continue
    print(list_output)



