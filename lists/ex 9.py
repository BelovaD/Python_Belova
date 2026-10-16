#Задача 9

white_list = []
while True:
    line = input()
    if line == "":
        break
    white_list.append(line)

queries = []
while True:
    query = input()
    if query == "":
        break
    queries.append(query)

for query in queries:
    if query in white_list:
        print(query)
