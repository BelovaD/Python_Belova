#Задача 8

url = input()
query_string = url.split("?")[1]
parameters = query_string.split("&")

for param in parameters:
    if param.startswith("q="):
        value = param.split("=")[1]    
print(f"\n{value}")

