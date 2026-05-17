# Функція яка буде аналізувати текст, ідентифікувати всі дійсні числа, що вважаються частинами доходів, і повертати їх як генератор.
import re 
from typing import Callable

def generator_numbers(text: str):# функція яка буде аналізувати текст.
    pattern = r'\b\d+\.\d+\b' # регулярний вираз для пошуку дійсних чисел з десятковою крапкою.
    
    found_numbers = re.findall(pattern, text)

    for num in found_numbers: # знайден число пертворюємо у тип float і повертаємо як генератор.
        yield float(num)

def sum_profit(text: str, func: Callable): # функція яка приймає текст і функцію генератора, викликає генератор для отримання чисел і повертає їх суму.
    return sum(func(text))

# Приклад використання функції:
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")

    