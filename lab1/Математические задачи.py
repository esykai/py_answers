# вариант 1
print("Площадь комнаты:", float(input("Введите длину комнаты: ")) * float(input("Введите ширину комнаты: ")))

# вариант 2
print("Объем комнаты:", float(input("Введите длину комнаты: ")) * float(input("Введите высоту комнаты: ")) * float(input("Введите ширину комнаты: ")))

# вариант 3
total_bill = float(input("Введите сумму заказа в ресторане: "))
tip_percentage = float(input("Введите % чаевых: "))
print(f"Размер чаевых: {total_bill * tip_percentage / 100}, Общая сумма к оплате: {total_bill * (1 + tip_percentage / 100)}")

# вариант 4
print("Размер НДС в заказе:", float(input("Введите сумму заказа в магазине: ")) * 0.20)

# вариант 5
print("Общий вес посылки:", (72 * int(input("Введите количество сувениров: ")) + 89 * int(input("Введите количество безделушек: "))) * 0.20)                          

# вариант 6
initial_deposit = float(input("Введите сумму первоначального депозита: "))
print(f"Сумма на счету после 1, 2 и 3 годов: {initial_deposit * (1 + 0.04) ** 1:.2f}, {initial_deposit * (1 + 0.04) ** 2:.2f}, {initial_deposit * (1 + 0.04) ** 3:.2f}")

# вариант 7
loan_amount, loan_term_months = map(float, input("Введите сумму кредита и срок кредита в месяцах через пробел: ").split())
print(f"Сумма переплаты по кредиту: {(loan_amount * 0.14 * loan_term_months / 12):.2f}")

# вариант 8
a, b = map(int, input("Введите два целых числа a и b через пробел: ").split())
print(f"Сумма: {a + b}, Разница: {a - b}, Произведение: {a * b}, Частное: {a / b}, Остаток: {a % b}, Возведение в степень: {a ** b}")

# вариант 9 ???
mpg = float(input("Введите показатель потребления топлива автомобилем в американских единицах (MPG): "))
print(f"Эквивалентный показатель в канадских единицах (L/100 km): {(235.214583 / mpg):.2f}")

# вариант 10
usd_amount, exchange_rate = map(float, input("Введите сумму в долларах и текущий курс доллара к рублю через пробел: ").split())
print(f"Сумма в рублях: {(usd_amount * exchange_rate):.2f}")

# вариант 11
feet = float(input("Введите расстояние в футах: "))
print(f"Дюймы: {feet * 12}, Ярды: {feet / 3}, Мили: {feet / 5280}")

# вариант 12
days, hours, minutes, seconds = map(int, input("Введите количество дней, часов, минут и секунд через пробел: ").split())
print(f"Общее количество секунд: {(days * 24 * 60 * 60) + (hours * 60 * 60) + (minutes * 60) + seconds}")

# вариант 13
import time
print(time.asctime())

# вариант 14
celsius = float(input("Введите температуру в градусах Цельсия: "))
print(f"Эквивалент в градусах Фаренгейта: {(celsius * 9 / 5) + 32}")

# вариант 15
print("Температура в градусах Кельвина:", float(input("Введите температуру в градусах Цельсия: ")) + 273.15)

# вариант 16
prices = [float(input("Введите цену товара: ")) for _ in range(3)]
discount = float(input("Введите процент скидки: "))
discounted_prices = [price * (1 - discount / 100) for price in prices]
print("Цены с учетом скидки:", discounted_prices)

# вариант 17
K, P, S = map(int, input("Введите через пробел K, P и S: ").split())
print("Количество ручек:", S // (K + K * P // 100))

# вариант 18
v, t = map(int, input("Введите через пробел скорость движения и время в пути: ").split())
print("Отметка, на которой остановится Вася:", (v * t) % 109)

# вариант 19
a, b = map(int, input("Введите два числа через пробел: ").split())
a, b = b, a
print("a =", a, "b =", b)

# вариант 20
n, m = map(int, input("Введите через пробел количество километров за день и длину маршрута: ").split())
print("Необходимое количество дней:", -(-m // n))

# вариант 21
n, m = map(int, input("Введите два числа через пробел: ").split())
print(1 if (n % m == 0) or (m % n == 0) else 0)

# вариант 22
a, b = map(int, input("Введите два числа через пробел: ").split())
print(max(a, b))

# вариант 23
from math import prod
numbers = [23, 45, 67, 89, 12, 34, 56, 78, 90, 10] # или numbers = [int(input("Введите целое число: ")) for _ in range(10)]
print("Среднее арифметическое:", sum(numbers) / len(numbers), "Среднее геометрическое:",  prod(numbers) ** (1 / len(numbers)))

# вариант 24
population_density = int(input("Введите количество жителей в государстве: ")) / float(input("Введите площадь территории в квадратных километрах: "))
print("Плотность населения в государстве:", population_density, "человек/км²")
