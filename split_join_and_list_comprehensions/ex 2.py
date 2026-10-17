#Задача 2

line = input()
numbers = [int(x) for x in line.split()]

print()

for num in numbers:
    print("*" * num)
