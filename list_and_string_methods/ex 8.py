#Задача 8

text = input().lower()
most_frequent_char = max(text, key=text.count)

print()
print(most_frequent_char)
