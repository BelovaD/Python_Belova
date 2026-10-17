#Задача 12

text = input()

if not text:
    max_count = 0
else:
    max_count = 1
    current_count = 1
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            current_count += 1
        else:
            current_count = 1
        if current_count > max_count:
            max_count = current_count

print(f"\n{max_count}")