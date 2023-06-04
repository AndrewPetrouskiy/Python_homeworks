# 4. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.
from task3 import check_number
from random import randint
MIN = 0
MAX = 1000
MAX_TRIES = 10
number = randint(0, 1000)


def guess_the_number(*, number: int, max_tries: int) -> None:
    numbers = []
    while max_tries > 0:
        your_number = check_number(min=MIN, max=MAX)
        numbers.append(your_number)
        if your_number == number:
            print("Congratulations!!! You guess the number")
            break
        if your_number > number:
            print('Your number more than number which you need to guess!')
        else:
            print('Your number less than number which you need to guess!')
        max_tries -= 1
        print(f'Remain {max_tries} tries. The choose {numbers=}', end="\n\n")

    else:
        print(
            f"YOU LOSE!!!! The number which you needed to guess equals {number}")


if __name__ == '__main__':
    guess_the_number(number=number, max_tries=MAX_TRIES)
