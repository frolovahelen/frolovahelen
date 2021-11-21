tickets = int(input("Количество участников:"))
result = 0
for i in range(tickets):
    age = int(input("Возраст участника:"))
    if age < 18:
        result = result + 0
    elif 18 <= age < 25:
        result = result + 990
    elif age > 25:
        result = result + 1390
        print("Итоговая сумма без скидки:", result)
if tickets > 3:
    result = result -(result * 0.1)
    print("Итоговая сумма с учетом возможной скидки:", result)
