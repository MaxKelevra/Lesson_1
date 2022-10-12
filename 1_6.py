days = 1
first_km = float(input("Введите результат первого дня: "))
last_km = float(input("введите желаемый результат: "))
if first_km < 0 or last_km < 0:
    print("Введенное значение должно быть больше 0 !")
else:
    while first_km < last_km:
        first_km += first_km * 0.1
        days += 1
print(f"Желаемый результат через {days} дней")
