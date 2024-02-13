# вариант 1
name = input("Введите ваше имя: ")
hour = int(input("Введите текущее время (в часах): "))

if 8 <= hour < 12:
    print("Доброе утро, ", name, "!")
elif 12 <= hour < 18:
    print("Добрый день, ", name, "!")
else:
    print("Добрый вечер, ", name, "!")

# вариант 2
s1 = input("Введите название первой страны: ")
s2 = input("Введите название второй страны: ")

t1 = s2
t2 = s1

print(t1, t2)

# вариант 3
string = input("Введите строку: ")

middle_index = len(string) // 2

first_half = string[:middle_index]
second_half = string[middle_index:]

print("Первая часть строки:", first_half)
print("Вторая часть строки:", second_half)

# вариант 4
city_name = input("Введите название города: ")

if len(city_name) % 2 == 0:
    print("Количество символов в названии города", city_name, "четное.")
else:
    print("Количество символов в названии города", city_name, "нечетное.")

# вариант 5
my_string = "Это строка с пробелами, которую мы хотим разрезать на четыре равные части"

string_length = len(my_string)
part_length = string_length // 4

part1 = my_string[:part_length]
part2 = my_string[part_length:part_length*2]
part3 = my_string[part_length*2:part_length*3]
part4 = my_string[part_length*3:]

print("Часть 1:", part1)
print("Часть 2:", part2)
print("Часть 3:", part3)
print("Часть 4:", part4)

# вариант 6
word1, word2 = input().split()
print(word2, word1)

# вариант 7
word1, word2 = "первое", "второе"
print(word2, word1)

# вариант 8
fio = input("Введите Фамилию, Имя и Отчество через пробел: ")
print(fio.replace(' ', '')) # че блять

# вариант 9
day = input("Введите день рождения: ")
month = input("Введите месяц рождения: ")
year = input("Введите год рождения: ")
print(day + '.' + month + '.' + year)

# вариант 10
city1 = input("Введите название первого города: ")
city2 = input("Введите название второго города: ")
city3 = input("Введите название третьего города: ")
cities = [city1, city2, city3]
print("Самое длинное название:", max(cities, key=len))
print("Самое короткое название:", min(cities, key=len))

# вариант 11
word = input("Введите слово: ")
stars = '*' * len(word)
print(stars + word + stars)

# вариант 12
string = input("Введите строку: ")
print(string + string)

# вариант 13
word = input("Введите слово: ")
print("Предпоследний символ:", word[-2])

# вариант 14
word = input("Введите слово: ")
print("Последний символ:", word[-1])

# вариант 15
word = input("Введите слово: ")
half_length = len(word) // 2
print("Первая половина слова:", word[:half_length])

# вариант 16
word = input("Введите слово: ")
half_length = len(word) // 2
print(word[half_length:] + word[:half_length])

# вариант 17
surname1 = input("Введите первую фамилию: ")
surname2 = input("Введите вторую фамилию: ")
if len(surname1) > len(surname2):
    print("Первая фамилия длиннее")
elif len(surname1) < len(surname2):
    print("Вторая фамилия длиннее")
else:
    print("Фамилии одинаковой длины")

# вариант 18
word = input("Введите слово: ")
if word[0] == word[-1]:
    print("Слово начинается и заканчивается на одну и ту же букву")
else:
    print("Слово не начинается и не заканчивается на одну и ту же букву")

# вариант 19
word1 = input("Введите первое слово: ")
word2 = input("Введите второе слово: ")

if word1[0] == word2[-1]:
    print("Первое слово начинается на ту же букву, на которую заканчивается второе слово.")
else:
    print("Первое слово не начинается на ту же букву, на которую заканчивается второе слово.")

# вариант 20
word = input("Введите слово: ")
print("Буквосочетание из второго и четвертого символа:", word[1] + word[3])

# вариант 21
word = input("Введите слово: ")
print("Буквосочетание из третьего и последнего символа:", word[2] + word[-1])

# вариант 22
word = input("Введите слово: ")
k = int(input("Введите количество букв, которые нужно перенести в конец: "))

new_word = word[k:] + word[:k]
print("Слово после переноса:", new_word)

# вариант 23
word = input("Введите слово: ")
print("Буквосочетание из 5 и 8 символа:", word[4] + word[7])

# вариант 24
word = input("Введите слово: ")
k = int(input("Введите количество букв, которые нужно перенести в начало: "))

new_word = word[-k:] + word[:-k]
print("Слово после переноса:", new_word)
