from typing import NoReturn


class Solution:
    @staticmethod
    def task_1() -> NoReturn:
        while True:
            try:
                number = input("Введите ваше число: ")
                if number == "exit":
                    break
                number = int(number)
                print(f"Знаков числа {len(str(number))}")

            except ValueError:
                print("Тип данных не соответствует числу")

    @staticmethod
    def task_2() -> NoReturn:
        negative = 0
        positive = 0
        number = int(input("Введите ваше число: "))
        interval = [i for i in range(-number, number + 1)]
        for i in interval:
            print(i)
            if i < 0:
                negative+=i
            else:
                positive+=i
        print(f"Сумма отрицательных чисел: {negative}, Сумма положительных чисел: {positive}")

    @staticmethod
    def task_3() -> NoReturn:
        number = input("Введите трехзначное число, в котором все цифры различны: ")

        if len(number) != 3 or len(set(number)) != 3:
            print("Ошибка: Введенное число не является трехзначным или содержит повторяющиеся цифры.")
            return

        def generate_permutations(digits, start, end):
            if start == end:
                print(int(''.join(digits)))
            else:
                for i in range(start, end + 1):
                    digits[start], digits[i] = digits[i], digits[start]
                    generate_permutations(digits, start + 1, end)
                    digits[start], digits[i] = digits[i], digits[start]

        digits_list = list(number)
        generate_permutations(digits_list, 0, len(digits_list) - 1)

    @staticmethod
    def task_4_1() -> NoReturn:
        def check_shot(shot, ship):
            shot_upper = shot.upper()

            for coord in ship.split():
                if shot_upper in coord:
                    return True
            return False

        ship = "Б1В1Г1 Е4Е5 В4В5В6В7 Д3 Д6 З2К2"
        try:
            while True:
                shot = input("Ваша координата для бомбы: ")
                if check_shot(shot, ship):
                    print(f"Попадание по координате {shot.upper()}!")
                else:
                    print(f"Промах по координате {shot.upper()}!")
        except KeyboardInterrupt:
            print("Я наблюдаю")

    @staticmethod
    def task_4_2() -> NoReturn:
        name = input("Введите ваше имя: ")
        surname = input("Введите вашу фамилию: ")
        age = input("Введите ваш возраст: ")

        output_format = "Ваше имя: {}, Фамилия: {}, Возраст: {} лет.".format(name, surname, age)
        print(output_format)

        output_str_fstring = f"Ваше имя: {name}, Фамилия: {surname}, Возраст: {age} лет."
        print(output_str_fstring)


if __name__ == '__main__':
    Solution.task_1()
    # Solution.task_2()
    # Solution.task_3()
    # Solution.task_4_1()
    # Solution.task_4_2()
