#Задача 1

text = input()
words = text.split()

secret_words = words[2::3]

print()

print(" ".join(secret_words))