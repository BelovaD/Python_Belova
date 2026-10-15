#Задача 2

n = int(input())
cities = set()

for _ in range(n):
    cities.add(input())

# Считываем новый город
new_city = input()

if new_city in cities:
    print("TRY ANOTHER")
else:
    print("OK")