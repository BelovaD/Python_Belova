#Задача 10

total_count = 0
count = 0

while True:
    num = int(input())

    if num == 0 and total_count >= 100:
      print("СТОП")
      print(count)
      break
    
    if num == 0:
        print("OK")
        break
    count += 1
    total_count += num
    