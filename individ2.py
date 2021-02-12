#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import json

#Использовать словарь, содержащий следующие ключи: фамилия и инициалы; номер
#группы; успеваемость (список из пяти элементов). Написать программу, выполняющую
#следующие действия: ввод с клавиатуры данных в список, состоящий из словарей заданной
#структуры; записи должны быть упорядочены по возрастанию номера группы; вывод на
#дисплей фамилий и номеров групп для всех студентов, включенных в массив, если средний
#балл студента больше 4.0; если таких студентов нет, вывести соответствующее сообщение.

def add(students, name, group, marks):
    person = {
        'name': name,
        'group': group,
        'marks': marks,
    }

    students.append(person)
    if len(students) > 1:
        students.sort(key=lambda item: item.get('group', ''))

def list(students):
    line = '+-{}-+-{}-+-{}-+-{}-+-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
        '-' * 8,
        '-' * 11
    )
    print(line)
    print(
        '| {:^3} | {:^30} | {:^20} | {:^8}  |'.format(
            "№",
            "Ф.И.О.",
            "Группа",
            "Оценки"
        )
    )
    print(line)
    # Вывести данные о всех сотрудниках.
    for idx, person in enumerate(students, 1):
        print(
            '| {:>3} | {:<30} | {:<20} | {:>11}  |'.format(
                idx,
                person.get('name', ''),
                person.get('group', ''),
                person.get('marks', f'{marks}'),
            )
        )
    print(line)

def select(students):
    count = 0
    for person in students:
        if (s / len(marks)) > 4.0:
            count += 1
            print(
                '{:>4}: {}'.format(count, person.get('name', ''))
            )
    # Если счетчик равен 0, то работники не найдены.
    if count == 0:
        print("Нет студентов.")
def load(parts):
    with open(parts, 'r') as f:
        return students


def save(students, parts):
    with open(parts, 'w') as f:
        json.dump(students, f)

if __name__ == '__main__':
    # Список студентов.
    students = []
    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()
        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break
        elif command == 'add':
            # Запросить данные о студенте.
            name = input("Введите фамилию и имя: ")
            group = input("Введите группу: ")
            marks = list(map(int, input("Введите пять оценок в формате - 1 2 3: ").split()))

            add(students, name, group, marks)

        elif command == 'list':
            print(list(students))

        elif command.startswith('select '):
            parts = command.split(' ', maxsplit=2)
            period = int(parts[1])
            s = float(sum(marks))

            select(students)


        elif command.startswith('load '):
            parts = command.split(' ', maxsplit=1)
            students = load(parts[1])

        elif command.startswith('save '):
            parts = command.split(' ', maxsplit=1)
            save(students, parts[1])

        elif command == 'help':
            print("Список команд:\n")
            print("add - добавить поезд;")
            print("list - вывести список поездов;")
            print("select <номер поезда> - запросить информацию о выбранном поезде;")
            print("load <имя_файла> - загрузить данные из файла;")
            print("save <имя_файла> - сохранить данные в файл;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)