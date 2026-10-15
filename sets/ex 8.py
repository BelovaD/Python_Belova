#Задача 8

m = int(input())

fridge = set()
for i in range(m):
    product = input()
    fridge.add(product)

n = int(input())

for i in range(n):
    recipe_line = input()
    words = recipe_line.split()
    
    recipe_name = words[0]
    
    can_cook = True
    
    for j in range(1, len(words)):
        ingredient = words[j]
        
        if ingredient not in fridge:
            can_cook = False
            break
            
    if can_cook:
        print(recipe_name)
