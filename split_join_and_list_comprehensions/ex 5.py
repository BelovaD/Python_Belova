#Задача 4

import json

words = input().split()

print()
print(json.dumps(words, ensure_ascii=False))