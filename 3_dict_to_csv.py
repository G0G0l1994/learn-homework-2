import csv

"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
lst=[
    {"name" : "Ivan", "age" : 20, "job":"scientist"}, 
     {"name" : "Yuri", "age" : 24, "job":"programmer"},
     {"name" : "Natali", "age" : 26, "job":"designer"},
     {"name" : "Bruce", "age" : 80, "job":"superhero"},
     {"name" : "Peter", "age" : 40, "job":"photographer"}
     ]
def main(lst):
   with open ('users.csv','w',encoding='utf-8',newline='') as f:
       for i in lst:
           
        writer=csv.DictWriter(f,i)
        writer.writeheader()
        writer.writerow(i)


if __name__ == "__main__":
    main(lst)
