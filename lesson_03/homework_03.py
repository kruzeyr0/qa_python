#alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії

alice_in_wonderland = (
    '"Would you tell me, please, which way I ought to go from here?"\n'
    '"That depends a good deal on where you want to get to," said the Cat.\n'
    '"I don\'t much care where ——" said Alice.\n'
    '"Then it doesn\'t matter which way you go," said the Cat.\n'
    '"—— so long as I get somewhere," Alice added as an explanation.\n'
    '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."\n'
    )


# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті

count = alice_in_wonderland.count("'")
print("Кількість одинарних лапок:", count)  # як і що відобразити
print()


# task 03 == Виведіть змінну alice_in_wonderland на друк

print(alice_in_wonderland)
print()


"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""

black_sea_area = 436402 # Initialize areas
azov_sea_area = 37800
total_area = black_sea_area + azov_sea_area # Calculate total area

print("Площа Азовського моря =", azov_sea_area, "км2")
print("Площа Чорного моря =", black_sea_area, "км2")
print("Щоб дізнатись площу, яку займають обидва моря - їх треба скласти:")
print(azov_sea_area, "+", black_sea_area, "=", total_area, "км2")
print("Загальна площа Азовського та Чорного моря:", total_area, "км2")
print()


# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""

total_qty = 375291
first_and_second_qty = 250449
second_and_third_qty = 222950
warehouse_three_qty = total_qty - first_and_second_qty
warehouse_two_qty = second_and_third_qty - warehouse_three_qty
warehouse_one_qty = first_and_second_qty - warehouse_two_qty
print("На першому складі: ", warehouse_one_qty)
print("На другому складі: ", warehouse_two_qty)
print("На третьому складі: ", warehouse_three_qty)
print("Загалом товарів: ", total_qty)
print()


# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""

total_cost = 1179 * 18
print("Загальна вартість комп'ютора за півтора року: ", total_cost)
print()

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""

ost_a = 8019 % 8
ost_b = 9907 % 9
ost_c = 2789 % 5
ost_d = 7248 % 6
ost_e = 7128 % 5
ost_f = 19224 % 9

print("Остатки від ділення: ")
print("a) ",ost_a, "     ", "d) ", ost_d)
print("b) ",ost_b, "     ", "e) ", ost_e)
print("c) ",ost_c, "     ", "f) ", ost_f)
print()

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""

pizza_l_qty = 4
pizza_m_qty = 2
juice_qty = 4
cake_qty = 1
water_qty = 3

pizza_l_price = 274
pizza_m_price = 218
juice_price = 35
cake_price = 350
water_price = 21

total_price = (pizza_l_price*pizza_l_qty)+(pizza_m_price*pizza_m_qty)+(juice_price*juice_qty)+(cake_price*cake_qty)+(water_qty*water_price)

print("Загальна ціна замовлення равна: ",total_price)
print()

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""

photo_total = 232
per_album_page = 8

max_pages = (photo_total//per_album_page) + (photo_total%per_album_page)

print("Мінімальна кількість сторінок для фотографій: ",max_pages)
print()


# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""

distance = 1600
tank_volume = 48
fuel_consumption_per_100 = 9/100

total_fuel = distance * fuel_consumption_per_100
fuel_refill_qty = total_fuel / tank_volume

print("Для такої подорожі знадобиться мінімум: ", total_fuel)
print("Мінімальна кількість заправок: ",fuel_refill_qty)
print()