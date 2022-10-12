income = float(input("Введите выручку фирмы: "))
outgoings = float(input("Введите издержки фирмы: "))
if income > outgoings:
    print(f"Фирма отработала с прибылью. Рентабельность: {income / outgoings:.2f}")
    workers = int(input("Введите количество сотрудников фирмы: "))
    print(f"Прибыль в расчете на одного сторудника сотавила: {income / workers:.2f}")
elif income == outgoings:
    print("Фирма отработала без прибыли")
else:
    print("Фирма отработала в убыток")