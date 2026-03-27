from datetime import datetime

time_log = "hblog.txt"  # змінна для зберігання шляху до файлу з логами
key = "Key TSTFEED0300|7E3E|0400" # змінна для зберігання ключа, який потрібно знайти в логах


def heartbeat_test(time_log, key, output_log):
    key_time = [] # список для зберігання часу, коли було знайдено ключ
    key_line = [] # список для зберігання рядків, в яких було знайдено ключ

    with open(time_log, "r", encoding="utf-8") as log_file: # відкриваємо файл з логами для читання
        for log_line in log_file:
            if key not in log_line: # якщо ключ не знайдено в рядку, переходимо до наступного рядка
                continue

            time_line = log_line.split("Timestamp ") # якщо ключ знайдено в рядку, виводимо цей рядок на екран


            if len(time_line) > 1:
                time_str = time_line[1].split()[0] # отримуємо рядок з часом, який знаходиться після "Timestamp "
                time_obj = datetime.strptime(time_str, "%H:%M:%S") # перетворюємо рядок у об'єкт datetime
                #print(f"Знайдено ключ: {key} в рядку: {log_line.strip()} з часом: {time_obj}") # дебаг прінт для перевірки правильності отримання часу
                
                key_time.append(time_obj) # додаємо отриманий час до списку key_time
                key_line.append(log_line.strip()) # додаємо рядок, в якому було знайдено ключ, до списку

            for i in range(len(key_time) - 1): # проходимо по списку key_time, щоб знайти різницю між часами
                current_time = key_time[i]
                next_time = key_time[i + 1]
                delta_time = abs((next_time - current_time).total_seconds()) # обчислюємо різницю між двома часами
                #print(f"Різниця: {delta_time} секунд") # виводимо різницю між часами на екран для дебага

    with open("hb_test.log", "w", encoding="utf-8") as output_log: # відкриваємо файл для запису результатів теста
        for i in range(len(key_time) - 1): # проходимо по списку key_time, щоб записати різницю між часами у файл
            current_time = key_time[i]
            next_time = key_time[i + 1]
            delta_time = abs((next_time - current_time).total_seconds()) # обчислюємо різницю між двома часами

            if 31 < delta_time < 33:
                output_log.write(f"WARNING: Різниця між часами: {delta_time} секунд в {current_time.time()} та {next_time.time()} IN {key_line[i]}\n") # записуємо як варнінг різницю між часами у файл, якщо вона знаходиться в діапазоні від 31 до 33 секунд

            elif delta_time >= 33:
                output_log.write(f"ERROR: Різниця між часами: {delta_time} секунд в {current_time.time()} та {next_time.time()} IN {key_line[i]}\n") # записуємо як помилку різницю між часами у файл, якщо вона більша або дорівнює 33 секундам
    
    return output_log # повертаємо об'єкт файлу з результатами теста




heartbeat_test(time_log, key, "hb_test.log") # викликаємо функцію для виконання теста
