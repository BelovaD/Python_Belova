#Задача 10

n = int(input())
word_list = [""] * n

for _ in range(n):
    position_str, letter = input().split()
    position = int(position_str)
    word_list[position - 1] = letter

print("".join(word_list))