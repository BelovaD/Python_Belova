#Задача 7

n = int(input())

result = ""

for i in range(n):
    text = input()
    
    if "плохо" in text:
        continue
        
    result = result + text + "\n"

print(result)