#Задача 6

current_sum = 0
count = 0
result_count = -1

while True:
    num = int(input())

    if num == 0:
        break
    count += 1
    current_sum += num

    if current_sum == 10 and result_count == -1:
        result_count = count

print(result_count)