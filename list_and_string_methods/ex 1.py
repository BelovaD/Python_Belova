#Задача 1

n = int(input())
results = []

for line_number in range(1, n + 1):
    line = input()
    
    position = line.find("кот")
    
    if position != -1:
        results.append((line_number, position))

print()

for line_num, pos in results:
    print(f"{line_num} {pos}")