#todo: Дан целочисленный массив размера N из 10 элементов.
#Преобразовать массив, увеличить каждый его элемент на единицу.

mass = [4, 7, 5, 1, 3, 9, 6, 2, 7, 0]
for x in range(len(mass)):
    mass[x] += 1
print(mass)
