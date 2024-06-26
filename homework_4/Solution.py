def decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Метод {func.__name__} был вызван с позиционными аргументами: {args} и именованными аргументами: {kwargs}")
        return func(*args, **kwargs)
    return wrapper


class Solution:
    @staticmethod
    def task_1() -> tuple:
        squares = [x ** 2 for x in range(1, 11)]

        weekdays = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
        weekdays_dict = {day: index + 1 for index, day in enumerate(weekdays)}

        tags = ["Django", "FastAPI", "Numpy", "PYTHON", "Pandas", "FASTAPI", "Python", "random"]

        tags_set = {tag.lower() for tag in tags}

        return squares, weekdays_dict, tags_set

    @staticmethod
    @decorator
    def task_2(n: int):
        a, b = 1, 1
        count = 0
        while count < n:
            yield a
            a, b = b, a + b
            count += 1

    @staticmethod
    def task_3(text, filename):
        with open(filename, 'a+') as file:
            file.write(text + '\n')

        with open(filename, 'r') as file:
            lines = file.readlines()
            for i in range(1, len(lines), 2):
                print(lines[i].strip())


class CardDeck:
    def __init__(self):
        self.suits = ["Пики", "Трефы", "Черви", "Бубны"]
        self.values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Валет", "Дама", "Король", "Туз"]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.suits) * len(self.values):
            raise StopIteration
        else:
            card = f"{self.values[self.index % len(self.values)]} {self.suits[self.index // len(self.values)]}"
            self.index += 1
            return card


if __name__ == "__main__":
    Solution.task_1()

    # q = Solution.task_2(10)
    # for i in q:
    #     print(i, end=" ")

    # Solution.task_3("True_or_False", "Temka")

    # deck = CardDeck()
    # for card in deck:
    #     print(card)


