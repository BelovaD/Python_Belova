#Задача 4

numbers = [int(x) for x in input().split()]
start, end = map(int, input().split())
sub_list = numbers[start : end + 1]
squares = [num ** 2 for num in sub_list]
result_sum = sum(squares)

print(f"\n{result_sum}")