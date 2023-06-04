# 2.Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
#  Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

print("Please, you need to enter the sides of the triangle")
side_a = int(input("Please, enter the first side of the triangle"))
side_b = int(input("Please, enter the second side of the triangle"))
side_c = int(input("Please, enter the third side of the triangle"))

if (side_a > side_b + side_c) or (side_b > side_a + side_c) or (side_c > side_a + side_b):
    print(
        f"The triangle with sides {side_a} , {side_b}, {side_c} doesn't exist")
else:
    if side_a == side_b == side_c:
        print("This triangle is equilatera")
    elif side_a == side_b or side_b == side_c or side_c == side_a:
        print("This triange is isosceles")
    else:
        print("this triange is scalene")
