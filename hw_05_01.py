def caching_fibonacci(): # Створення функції
    cache = {} # Створення порожнього словника

    def fibonacci(n): # Створення функції 
        if n <= 0: 
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n] # Повернення значення n зі словника 
    
    return fibonacci # Повернення функції

fib = caching_fibonacci() # Присвоєння змінній fib виклик функції

print(fib(int(input("Введіть число: "))))