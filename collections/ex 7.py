#Задача 7

first_list = []
while True:
    line = input().strip()
    if line == "":
        break
    first_list.append(line)
  
second_set = set()
while True:
    try:
        line = input().strip()
        if line == "":
            break
        second_set.add(line)
    except EOFError:
        break

print()

for word in first_list:
    if word not in second_set:
        print(word)
