#Задача 3

n = int(input())
dictionary = {}

for _ in range(n):
    word, translation = input().split()
    dictionary[word] = translation

target_word = input()

print()

result = dictionary.get(target_word, "Слово не найдено")

print(result)