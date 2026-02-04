# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier
        # десь тут помилка, а може не одна (fixed)
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(2)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_of_two_numbers(num1, num2):
    return num1 + num2

print(sum_of_two_numbers(5, 10)) # print 15


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def avg(*args):
    return sum(args) / len(args)

print(avg(1, 2, 3, 4, 5)) # print 3.0
print(avg(0,0,0)) # print 0.0


# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse(string):
    reversed_result = ""
    index = len(string) - 1
    while index >= 0:
        reversed_result += string[index]
        index -= 1

    return reversed_result

print(reverse("Hello, world!")) # print "!dlrow ,olleH"


# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def longest_word(string):
    longest = ""
    for words in string:
        if len(words) > len(longest):
            longest = words
    return longest

print(longest_word(["cat", "dog", "elephant", "giraffe"])) # print "elephant"

longest_with_input = input("Enter words: ") 
print(longest_word(longest_with_input.split())) # print the longest word from the input



# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    string_index = str1.find(str2)

    return string_index

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7 - sum of even numbers in a list

numbers_list = [10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 4, 5, 6, 7, 4, 9, 10]

def sum_of_even_numbers(numbers):
    sum_even = 0
    i = 0

    while i < len(numbers):
        if numbers[i] % 2 == 0:
            print(f"Even number: {numbers[i]}")
            sum_even += numbers[i]
        i += 1

    print("Total sum of even numbers:", sum_even)

sum_of_even_numbers(numbers_list)

# task 8 - filter strings from a list

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']

def filter_string(lst):
    result = []

    for item in lst1:
        if isinstance(item, str):
            result.append(item)

    return(result)

print(filter_string(lst1))

# task 9 - unique characters in a string

text = input("Enter string: ") 

def unique_characters(text):
    unique_chars = set(text)
    print(f'You entered: {text}')

    print(f'Unique characters: {unique_chars}')

    if len(unique_chars) > 10:
        print('More than 10 unique characters: True')
    else:
        print('Less than or equal to 10 unique characters: False')

    return unique_chars

unique_characters(text)
# task 10 - calculate quantities in warehouses with given totals


total = input("Input total quantity: ") # total quantity of goods in all warehouses

first_and_second_warehouse = input("Input quantity of first and second warehouse combined: ") # quantity of goods in first and second warehouses combined

second_and_third_warehouse = input("Input quantity of second and third warehouse combined: ") # quantity of goods in second and third warehouses combined
print()

def calculate_warehouse_quantities(total, first_and_second_warehouse, second_and_third_warehouse):
    total_qty = int(total)
    first_and_second_qty = int(first_and_second_warehouse)
    second_and_third_qty = int(second_and_third_warehouse)

    if (first_and_second_qty + second_and_third_qty - total_qty < 0) or (first_and_second_qty > total_qty + second_and_third_qty) or (second_and_third_qty > total_qty + first_and_second_qty): # check for inconsistent data
        print("Error: inconsistent warehouse quantities!")
        return None

    if first_and_second_qty > total_qty:
        print("Error: sum of first and second warehouse is greater than total quantity!")
        return None

    if second_and_third_qty > total_qty:
        print("Error: sum of second and third warehouse is greater than total quantity!")
        return None

    warehouse_three_qty = total_qty - first_and_second_qty
    warehouse_two_qty = second_and_third_qty - warehouse_three_qty
    warehouse_one_qty = first_and_second_qty - warehouse_two_qty

    return warehouse_one_qty, warehouse_two_qty, warehouse_three_qty

warehouse_one_data, warehouse_two_data, warehouse_three_data = calculate_warehouse_quantities(total, first_and_second_warehouse, second_and_third_warehouse) # get quantities for each warehouse

print("На першому складі: ", warehouse_one_data)
print("На другому складі: ", warehouse_two_data)
print("На третьому складі: ", warehouse_three_data)
print("Загалом товарів: ", total)






"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""