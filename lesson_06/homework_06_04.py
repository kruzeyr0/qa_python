numbers_list = [10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 4, 5, 6, 7, 4, 9, 10]
sum_even = 0
i = 0

while i < len(list):
    if list[i] % 2 == 0:
        print(f"Even number: {list[i]}")
        sum_even += list[i]
    i += 1

print("Total sum of even numbers:", sum_even)