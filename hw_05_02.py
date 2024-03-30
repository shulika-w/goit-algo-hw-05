from typing import Callable, Generator

def generator_numbers(text: str) -> Generator: # Створення функції, яка приймає рядок тексту як аргумент
    for word in text.split(): # Розділення рядку тексту на слова
        if word.isdigit(): # Перевірка слів на дійсне число
            yield int(word) # Повернення числа наступним елементом генератора

def sum_profit(text: str, func: Callable) -> int: # Створення функції, яка приймає рядок тексту і функцію, яка повертає генератор чисел, як аргументи
    return sum(func(text)) # Повернення суми всіх чисел, що повертає генератор

text = input("Введіть текст: ")
print(f"Загальна сума чисел в тексті: {sum_profit(text, generator_numbers)}")