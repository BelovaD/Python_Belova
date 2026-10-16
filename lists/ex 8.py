#Задача 8

n = int(input())
soups = ["щи", "борщ", "щавелевый", "овсяный", "по-чабански"]
menu_length = len(soups)

for i in range(n):
    soup_index = i % menu_length
    print(soups[soup_index])