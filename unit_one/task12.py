#Единицы массы пронумерованы следующим образом: 1 — килограмм, 2 — миллиграмм, 3 — грамм, 4 — тонна, 5 — центнер.
#Дан номер единицы массы и масса тела M в этих единицах (вещественное число). Вывести массу данного тела в килограммах.
# Данную задачу нужно решить с помощью конструкции  match  (Python v3.10)


# Пример:
# Введите единицу массы тела
#       1 - килограмм
#       2 — миллиграмм
#       3 — грамм
#       4 — тонна
#       5 — центнер
#>4

#Введите  массу тела
#>1

#Ответ: 1000 кг

print("Коды единиц массы тела: 1 — килограмм, 2 — миллиграмм, 3 — грамм, 4 — тонна, 5 — центнер.")
code = int(input("Введите код еденицы массы тела"))
mass = int(input("Введите значение массы тела"))
match code:
    case 1:
        print(f"Ответ: {mass} кг")
    case 2:
        mass = mass/10000000
        print(f"Ответ: {mass} кг")
    case 3:
        mass = mass/1000
        print(f"Ответ: {mass} кг")
    case 4:
        mass = mass*1000
        print(f"Ответ: {mass} кг")
    case 5:
        mass = mass*100
        print(f"Ответ: {mass} кг")
