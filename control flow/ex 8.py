#Задача 8

has_cat = False

while True:
    text = input()
    if text == "СТОП":
        break
    if "пёс" in text or "Пёс" in text:
        has_cat = False
    elif "кот" in text or "Кот" in text:
        has_cat = True
if has_cat:
    print("МЯУ")
else:
    print("НЕТ")
