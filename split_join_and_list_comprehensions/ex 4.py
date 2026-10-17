#Задача 4

numbers = [int(x) for x in input().split()]

result = [
    num ** 2 
    for num in numbers 
    if num % 2 != 0 and (num ** 2) % 10 != 9
]

print()
print(*result)