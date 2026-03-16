from ast import parse
from pathlib import Path
from xml.etree.ElementTree import parse
import csv
import random
import json
import logging


base_folder = Path(__file__).parent # шлях до теки, в якій знаходиться цей скрипт
test_folder = base_folder.parent / "ideas_for_test" # шлях до теки з ідеями для тестування

csv_folder = test_folder / "work_with_csv" # шлях до теки з файлами для порівняння
json_folder = test_folder / "work_with_json" # шлях до теки з файлами для валідації
xml_file = test_folder / "work_with_xml" / "groups.xml" # шлях до XML файлу для пошуку

output_file = base_folder / "result_Katrych.csv" # шлях до файлу, в який буде записано результат
log_file = base_folder / "json_Katrych.log" # шлях до файлу логів



files = [] # створення порожнього списку для зберігання файлів з теки
for file in csv_folder.iterdir():
    if file.is_file():
        files.append(file) # збір всіх файлів з теки у список

file_1 = random.choice(files) # вибір випадкового файлу з теки
file_2 = random.choice(files)

while file_1 == file_2:
    file_2 = random.choice(files) # щоб уникнути вибору одного і того ж файлу двічі




def remove_duplicates(file_1, file_2, output_file):

    with open(file_1, mode="r") as file_1, open(file_2, mode="r") as file_2: # відкриття обох файлів для читання
        reader1 = csv.reader(file_1)
        reader2 = csv.reader(file_2)

        data1 = set(tuple(row) for row in reader1) # створення сету для зберігання унікальних рядків з файлів
        data2 = set(tuple(row) for row in reader2)

        unique_data = data1 | data2 # об'єднання двох сетів для отримання унікальних рядків

        with open(output_file, mode="w", newline="") as output: # відкриття файлу для запису результату
            writer = csv.writer(output) # створення об'єкта для запису у файл
            for row in unique_data:
                writer.writerow(row) # запис унікальних рядків у файл результату


remove_duplicates(file_1, file_2, output_file) # виклик функції для видалення дублікатів та запису результату у файл

print(f"Файл 1: {file_1.name}") # виведення імені першого файлу
print(f"Файл 2: {file_2.name}") # виведення імені другого файлу
print(f"Результат записано у файл: {output_file.name}") # виведення імені файлу, в який записано результат

#############################################################################################################################################

json_logger = logging.getLogger("json_logger")
json_logger.setLevel(logging.ERROR)
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.ERROR)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
json_logger.addHandler(file_handler) # налаштування логера для валідації JSON файлів, з рівнем ERROR та форматом, що включає час, рівень та повідомлення, а також додавання обробника для запису логів у файл

def validate_json_files(json_folder): # функція для валідації JSON файлів у вказаній теці
    for file in json_folder.iterdir():
        if file.is_file():
            try:
                with open(file, "r", encoding="utf-8") as f: # відкриття файлу для читання з вказівкою кодування
                    json.load(f)
                    print(f"Valid JSON file: {file.name}") # виведення повідомлення про валідний файл у консоль

            except json.JSONDecodeError as e:
                json_logger.error(f"Invalid JSON file: {file.name} | {e}")  # запис помилки у лог, якщо файл не є валідним JSON, включаючи ім'я файлу та повідомлення про помилку
                print(f"Invalid JSON file: {file.name} | {e}")  # виведення повідомлення про невалідний файл у консоль

validate_json_files(json_folder) # виклик функції для валідації JSON файлів у вказаній теці
print(f"Валідація JSON файлів завершена. Результати записані у файл: {log_file.name}") # виведення повідомлення про завершення валідації та ім'я файлу логів

#############################################################################################################################################

xml_logger = logging.getLogger("xml_logger")
xml_logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(levelname)s - %(message)s")
console_handler.setFormatter(formatter)
xml_logger.addHandler(console_handler) # додавання обробника для виведення логів у консоль, з рівнем INFO та вказаним форматом


def find_incoming_by_group_number(xml_file, group_number):
    tree = parse(xml_file) # парсинг XML файлу
    root = tree.getroot() # отримання кореневого елемента XML

    for group in root.findall("group"): 
        number = group.find("number") # отримання тексту елемента "number" для поточної групи

        if number is None:
            continue # пропуск поточної ітерації, якщо елемент "number" не знайдено

        if number.text == str(group_number): 
            timing  = group.find("timingExbytes") # отримання тексту елемента "timingExbytes" для поточної групи

            if timing  is None:
                xml_logger.info(f"Group {group_number} timingExbytes not found") # запис інформації у лог, якщо елемент "timingExbytes" не знайдено для групи з заданим номером
                return None # повернення None, якщо елемент "timingExbytes" не знайдено
            
            incoming = timing.find("incoming")
            if incoming is None:
                xml_logger.info(f"Group {group_number} incoming not found") # запис інформації у лог, якщо елемент "incoming" не знайдено для групи з заданим номером
                return None # повернення None, якщо елемент "incoming" не знайдено
            
            xml_logger.info(f"Group {number.text}, Incoming: {incoming.text}") # запис інформації у лог, якщо група з заданим номером знайдена, включаючи номер групи та значення "incoming"           
            return incoming.text # повернення тексту елемента "incoming" для групи з заданим номером        
        
    xml_logger.info(f"Group {group_number} not found") # запис інформації у лог, якщо група з заданим номером не знайдена
    


for i in range(6): # цикл для пошуку значення "incoming" для груп з номерами від 0 до 5
    find_incoming_by_group_number(xml_file, i)

print(f"Пошук значення 'incoming' для груп завершено. Логи виведено в консоль.") # виведення повідомлення про завершення пошуку 
