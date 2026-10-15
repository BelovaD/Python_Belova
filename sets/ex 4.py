#Задача 4

m = int(input())
english = set()
for _ in range(m):
    english.add(input())
  
n = int(input())
german = set()
for _ in range(n):
    german.add(input())

difference = english ^ german
count = len(difference)
if count > 0:
    print(count)
else:
    print("NO")