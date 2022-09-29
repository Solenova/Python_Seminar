import csv
def sarchDirectory():  
    req=input('Введите фамилию, чей номер хотие найти в справочнике - ')
    with open("data.csv", encoding='utf-8') as r_file:
        # Создаем объект reader, указываем символ-разделитель ","
        file_reader = csv.reader(r_file, delimiter = ",")
        # Счетчик для подсчета количества строк и вывода заголовков столбцов
        count = 0
        # Считывание данных из CSV файла
        for row in file_reader:
            if req == row[0]:
                with open("output_new.csv", mode="w", encoding='utf-8') as w_file:
                    file_writer = csv.writer(w_file, lineterminator="\r")
                    file_writer.writerow(f'           {row[0]} :    {row[1]}      ({row[2]} )')
            
 
