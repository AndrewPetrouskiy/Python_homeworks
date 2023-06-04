# 3. Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
MIN = 0
MAX = 10_000


def check_number(*, min, max) -> int:
    while True:
        try:
            num = int(
                input(f"Enter the number which more than {min} and less than {max}\n"))
            if num > min and num < max:
                return num
            else:
                print('You entered incorrect number. Try again')
        except:
            print('You entered not a number. Try again')


def define_number(num: int) -> None:
    for i in range(2, num + 1):
        if num == i:
            print("this number is simple")
        elif num % i == 0:
            print("This number isn't simple")
            break


if __name__ == '__main__':
    define_number(check_number(min=MIN, max=MAX))
