#Задача 6


text = input().upper()
words = text.split()
robotic_words = ["-".join(word) for word in words]

print()

print(" ".join(robotic_words))