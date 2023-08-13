N = int(input("Введите общее количество билетов:"))
price = 0
for value in range(N):
    age = int(input("Введите возраст"))
    if 18 <= age <= 25:
        price = price + 990
        print("Стоимость билетов", price, "р.")
    elif age > 25:
        price = price + 1390
        print("Стоимость билетов:", price, "р.")
if N > 3:
    price = price - price/10
    print("Стоимость всех билетов со скидкой", price, "р.")
