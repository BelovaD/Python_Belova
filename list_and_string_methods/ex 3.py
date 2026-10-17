#Задача 3

numbers = [int(x) for x in input().split()]
start, end = map(int, input().split())
sub_list = numbers[start : end + 1]
result_sum = sum(sub_list)

print(f"\n{result_sum}")