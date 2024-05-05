import datetime
import os
import random

variant = 1


class Solution:
    @staticmethod
    def task_1():
        number = random.randint(1, 100)
        if number % 2 == 0:
            print(f"Чётное число {number}!")
        else:
            print(f"Нечётное число {number}!")

    @staticmethod
    def task_2():
        today = datetime.date.today()
        directory_name = today.strftime("%Y-%m-%d")
        os.mkdir(directory_name)

        with open(f"{directory_name}/empty_file.txt", "w"):
            pass

        os.mkdir(f"{directory_name}/welcome_directory")

        os.rename(f"{directory_name}/file.txt", f"{directory_name}/welcome_directory/file.txt")
