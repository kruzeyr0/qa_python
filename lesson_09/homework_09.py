class Romb:
    def __setattr__(self, name, value): # метод для встановлення атрибутів класу, який перевіряє правильність введених даних (по умовах завдання)

        if name == "side_a" and value <= 0: # перевірки
            print("Сторона a повинна бути більше 0")
        else:
            self.__dict__[name] = value # встановлюємо атрибут класу, якщо всі перевірки пройшли успішно


        if name == "angle_a":
            if value <= 0 or value >= 180:
                print (f"Кут {name} має бути від 0 до 180 градусів")
            else:
                self.__dict__[name] = value # сетапимо атрибути
                if "angle_b" not in self.__dict__:
                    self.__dict__["angle_b"] = 180 - value # якщо кут b не встановлений, встановлюємо його як 180 - кут a


        if name == "angle_b":
            if value <= 0 or value >= 180:
                print (f"Кут {name} має бути від 0 до 180 градусів")
            else:
                self.__dict__[name] = value


        angle_a = self.__dict__.get("angle_a")
        angle_b = self.__dict__.get("angle_b")

        if angle_a is not None and angle_b is not None: # якщо обидва кути встановлені, перевіряємо їх суму
            if angle_a + angle_b != 180:
                print("Сумма кутів має дорівнювати 180 градусам")
            
        
        self.__dict__[name] = value # встановлюємо інші атрибути класу, якщо всі перевірки пройшли успішно



    
# Приклади використання класу Romb:
romb = Romb()
romb.side_a = 5
romb.angle_a = 60
print(f"Сторона a: {romb.side_a}, Кут a: {romb.angle_a}, Кут b: {romb.angle_b}")

romb_full = Romb()
romb.side_a = 5
romb.angle_a = 60
romb_full.angle_b = 120
print(f"Сторона a: {romb.side_a}, Кут a: {romb.angle_a}, Кут b: {romb.angle_b}")

romb_two = Romb()
romb_two.side_a = -3
romb_two.angle_a = 60
print(f"Сторона a: {romb_two.side_a}, Кут a: {romb_two.angle_a}, Кут b: {romb_two.angle_b}")

romb_three = Romb()
romb_three.side_a = 5
romb_three.angle_a = 90
romb_three.angle_b = 130
print(f"Сторона a: {romb_three.side_a}, Кут a: {romb_three.angle_a}, Кут b: {romb_three.angle_b}")

romb_fourth = Romb()
romb_fourth.side_a = 5
romb_fourth.angle_a = 60
romb_fourth.angle_b = 150
print(f"Сторона a: {romb_three.side_a}, Кут a: {romb_three.angle_a}, Кут b: {romb_three.angle_b}")