price = 0
num_of_tickets = int(input("Введите количество билетов: "))
for i in range(1, num_of_tickets + 1):
    age = int(input(f'Введите возраст посетителя, билет № {i}: '))
    if 18 <= age < 25:
        price += 990
    elif age >= 25:
        price += 1390
if num_of_tickets > 3:
    price = int(price - ((price / 100) * 10))
print(f"Общая стоимость билетов за {num_of_tickets} посетителей: {price} рублей")

