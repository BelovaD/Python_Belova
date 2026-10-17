#Задача 10

n = int(input())
translation_dict = {}

for _ in range(n):
    original, translation = input().split()
    translation_dict[original] = translation

text = input().split()
translated_words = [translation_dict.get(word, word) for word in text]

print()
print(" ".join(translated_words))
