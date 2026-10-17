#Задача 5

n = int(input())
products_prices = {}

for _ in range(n):
    product, price = input().split()
    products_prices[product] = price

target_product = input()

print()

result = products_prices.get(target_product, "Товар не найден")

print(result)
