#Задача 10

shift = int(input())
text = input()

alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

result = []

for char in text:
    if char in alphabet:
        current_index = alphabet.index(char)
        new_index = (current_index + shift) % 33
        result.append(alphabet[new_index])
    else:
        result.append(char)

print("".join(result))