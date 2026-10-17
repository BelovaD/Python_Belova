#Задача 2

words = input().split()
lengths = [len(word) for word in words]
max_length = max(lengths)

print(f"\n{max_length}")