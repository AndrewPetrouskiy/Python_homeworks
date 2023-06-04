# 1.Решить задачи, которые не успели решить на семинаре:
# a. Написать программу, которая будет выводить в консоль ёлочку заданной высоты

SPACE = ' '
STRAR = '*'


rows = int(input("Plese, enter the height of the Christmas tree"))
spaces = rows-1
stars = 2

for i in range(rows):
    print(
        (SPACE*spaces) +
        (STRAR*stars) +
        (SPACE*spaces)
    )
    stars += 2
    spaces -= 1


print("---------------------------------------------------")
# б. Написать порграмму, которая выодит в консоль таблицу умножения "как на тетрадках"

for i in range(1, 10):
    for j in range(10):
        print(f"{i} X {j} = {i * j}")
