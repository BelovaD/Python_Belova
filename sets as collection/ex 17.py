#Задача 17

word1 = input()
word2 = input()

bulls = 0
w1_remaining = []
w2_remaining = []

for i in range(len(word1)):
    if word1[i] == word2[i]:
        bulls += 1
    else:
        w1_remaining.append(word1[i])
        w2_remaining.append(word2[i])

cows = 0
for char in w1_remaining:
    if char in w2_remaining:
        cows += 1
        w2_remaining.remove(char)

print(f"Быки: {bulls}")
print(f"Коровы: {cows}")