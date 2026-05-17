# Функція яка створює та використовує кеш для зберігання й повторного використання вже обчислених значень чисел Фібоначчі.
def caching_fibonacci(): 
    cache = {}

    def fibonacci(n): # внутрішня функція для обчислення числа Фібоначчі з використанням кешу
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache: 
            return cache[n]
        else: 
            result = fibonacci(n - 1) + fibonacci(n - 2)
            cache[n] = result
            return result
    return fibonacci 

# Отримуємо функцію fibonacci
fib = caching_fibonacci()
# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))
print(fib(15))