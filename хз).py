import math
import random
import string
import datetime
import itertools
import functools
import os
import sys
import time

# Создание класса для вывода сообщения
class MessagePrinter:
    def __init__(self, message):
        self.message = message

    def print_message(self):
        print(self.message)

# Генерация случайного символа
def generate_random_character():
    return random.choice(string.ascii_letters)

# Создание списка из случайных символов
def create_random_string(length):
    return ''.join(generate_random_character() for _ in range(length))

# Функция для задержки перед выводом сообщения
def delay(seconds):
    time.sleep(seconds)

# Основная функция
def main():
    # Получение текущего времени
    now = datetime.datetime.now()
    print(f"Текущая дата и время: {now}")

    # Создание случайной строки
    random_string = create_random_string(10)
    print(f"Случайная строка: {random_string}")

    # Задержка перед выводом сообщения
    delay(2)

    # Создание экземпляра класса MessagePrinter
    printer = MessagePrinter("Hello, World!")
    
    # Использование функции map для создания списка из одного элемента
    list(map(lambda x: printer.print_message(), [1]))

if __name__ == "__main__":
    main()
