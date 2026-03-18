def generate_fibonachi(n):
    a = 0   # Початкове число Фібоначчі
    b = 1
    while a < n:  
        yield a
        c = a
        a = b
        b = c + b   # Рахуємо наступне число Фібоначчі

print("Генератор чисел Фібоначчі:")
num_fibonachi = 7

for fibonachi in generate_fibonachi(num_fibonachi):
    print(fibonachi) # Прінт Фібоначчі


print() # Порожній рядок для розділення виводу


def generate_even(n):
    for i in range(n):
        if i % 2 == 0:  # Перевіряємо, чи є число парним
            yield i

print("Генератор парних чисел:")
num_even = 10

for even in generate_even(num_even):
    print(even) # Прінт парних чисел

print() # Порожній рядок для розділення виводу
############################################################################

class InvertIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data) - 1  # Ініціалізуємо індекс на останній елемент списку

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration # Викидаємо виключення, коли досягли початку списку
                
        value = self.data[self.index] # Отримуємо поточне значення за індексом
        self.index -= 1 # Зменшуємо індекс для наступного виклику
        return value 

    
print("Ітератор для зворотного проходження:")
inv_num = [1, 2, 3, 4, 5]

for item in InvertIterator(inv_num):
    print(item) # Прінт елементів у зворотному порядку

print() # Порожній рядок для розділення виводу

class EvenIterator:
    def __init__(self, data):

        self.data = data
        self.index = 0  # Ініціалізуємо індекс на початок списку

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.data):

            value = self.data[self.index] # Отримуємо поточне значення за індексом
            self.index += 1 # Збільшуємо індекс для наступного виклику

            if value % 2 == 0: # Перевіряємо, чи є число парним
                return value 
            
        raise StopIteration # Викидаємо виключення, коли досягли кінця списку

print("Ітератор для парних чисел:")
even_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for item in EvenIterator(even_num):
    print(item) # Прінт парних чисел


print() # Порожній рядок для розділення виводу
############################################################################

def log_decorator(func):
    def wrapper(*args): # Обгортка, яка приймає будь-яку кількість аргументів
        print(f"Викликається функція {func.__name__} з аргументами: {args}") # Логування назви функції та її аргументів
        return func(*args) # Викликаємо оригінальну функцію
    return wrapper

@log_decorator
def target_for_log(a, b):
    return a + b

print("Декоратор для логування:")
result = target_for_log(3, 5) # Викликаємо функцію з декоратором
print(f"Результат: {result}") # Виводимо результат функції

print() # Порожній рядок для розділення виводу


def handle_decorator(func):
    def wrapper(*args, **kwargs): # Обгортка, яка приймає будь-яку кількість позиційних та іменованих аргументів
        try:
            return func(*args, **kwargs) # Спробуємо виконати оригінальну функцію
        except Exception as e: # Якщо виникне помилка, перехопимо її
            print(f"Сталася помилка: {e}") # Виведемо повідомлення про помилку
    return wrapper


@handle_decorator
def target_for_handle(lst, index=0):
    return lst[index]

print("Декоратор для обробки помилок:")
result = target_for_handle([1, 2, 3], index=1) # Викликаємо функцію з декоратором, передаючи список та індекс
print(f"Результат: {result}") # Виводимо результат функції
result = target_for_handle([1, 2, 3], index=5) # Викликаємо функцію з декоратором, передаючи список та індекс, який викличе помилку
print(f"Результат: {result}") # Виводимо результат функції, який буде None через помилку


