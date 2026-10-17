#Задача 9

target_char = input().lower()
text_words = input().split()

result_words = [
    word 
    for word in text_words 
    if target_char in word.lower()
]

print()
print(" ".join(result_words))