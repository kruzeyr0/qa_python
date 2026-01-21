# task 01 == Виправте синтаксичні помилки
print("Hello", end = " ")
print("world!")

# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print()

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 4
banana = apples * 4
print("Apples:", apples)
print("Bananas:", banana)

# task 05 == виправте назви змінних
storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimetery = storona_1 + storona_2 + storona_3 + storona_4
print("Perimetery:", perimetery)


"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?a
"""
apples = 4
pears = apples + 5
plums = pears - 2
total = apples + pears + plums
print("У саду маємо - яблуні:", apples, ", Груші:", pears, ", Сливи:", plums)
print("Всього дерев посадили в саду:", total)

# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
temperature_am = 5
temperature_pm = temperature_am - 10
temperature_evening = temperature_pm + 4
print("Температура до обіду:", temperature_am, "градусів")
print("Температура після обіду:", temperature_pm, "градусів")
print("Температура надвечір:", temperature_evening, "градусів")

# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
boys = 24
girls = boys // 2
boys_today = boys - 1
girls_today = girls - 2
total_today = boys_today + girls_today
print("Хлопчиків в группі всього:",boys, ", Дівчаток всього:", girls)
print("Хлопчиків сьогодні:",boys_today, ", Дівчаток сьогодні:", girls_today)
print("Всього дітей сьогодні у театральному гуртку:", total_today)

# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""

first_book = 8
second_book = first_book + 2
third_book = (first_book + second_book) / 2
total_cost = first_book + second_book + third_book
print("Total cost of all books:", total_cost)
print("Вартість першої книги:", first_book, "грн.")
print("Вартість другої книги:", second_book, "грн.")
print("Вартість третьої книги:", third_book, "грн.")
print("Загальна вартість усіх книг:", total_cost, "грн.")