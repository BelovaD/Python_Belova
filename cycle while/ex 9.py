#Задача 9

numb = int(input())

digit_sum = 0

while numb > 0:
    digit_sum += numb % 10
    numb //= 10

print(digit_sum)
