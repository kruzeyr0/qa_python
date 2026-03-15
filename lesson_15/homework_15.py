from ast import parse
from pathlib import Path
import csv
import random
import json
import logging

csv_folder = Path(__file__).parent.parent / "ideas_for_test" / "work_with_csv" # шлях до теки з файлами для порівняння
json_folder = Path(__file__).parent.parent / "ideas_for_test" / "work_with_json" # шлях до теки з файлами для валідації
xml_file = Path(__file__).parent.parent / "ideas_for_test" / "work_with_xml" / "groups.xml" # шлях до XML файлу для пошуку
output_file = Path(__file__).parent / "result_Katrych.csv" # шлях до файлу, в який буде записано результат
log_file = Path(__file__).parent / "json_Katrych.log" # шлях до файлу логів



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

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s" # формат для запису логів, включаючи час, рівень логування та повідомлення
)

def validate_json_files(json_folder): # функція для валідації JSON файлів у вказаній теці
    for file in json_folder.iterdir():
        if file.is_file():
            try:
                with open(file, "r", encoding="utf-8") as f: # відкриття файлу для читання з вказівкою кодування
                    json.load(f)
                    print(f"Valid JSON file: {file.name}") # виведення повідомлення про валідний файл у консоль

            except json.JSONDecodeError as e:
                logging.error(f"Invalid JSON file: {file.name} | {e}")  # запис помилки у лог, якщо файл не є валідним JSON, включаючи ім'я файлу та повідомлення про помилку
                print(f"Invalid JSON file: {file.name} | {e}")  # виведення повідомлення про невалідний файл у консоль

validate_json_files(json_folder) # виклик функції для валідації JSON файлів у вказаній теці
print(f"Валідація JSON файлів завершена. Результати записані у файл: {log_file.name}") # виведення повідомлення про завершення валідації та ім'я файлу логів

#############################################################################################################################################

def find_incoming_by_group_number(xml_file, group_number):
    tree = parse(xml_file) # парсинг XML файлу

    root = tree.getroot() # отримання кореневого елемента XML
    


find_incoming_by_group_number(xml_file, 1)