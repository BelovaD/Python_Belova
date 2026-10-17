#Задача 4

text = input()
char_counts = {}

for char in text:
    if char != " ":
        if char not in char_counts:
            char_counts[char] = 1
        else:
            char_counts[char] += 1

print()

most_frequent = max(char_counts, key=char_counts.get)

print(most_frequent)
