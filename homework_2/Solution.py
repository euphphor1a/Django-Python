from typing import NoReturn


class Solution:
    @staticmethod
    def task_1() -> NoReturn:
        powered_numbers = []
        power = int(input("Введите степень: "))
        n = int(input("Введите кол-во чисел/строк: "))
        i = 0
        while i < n:
            i += 1
            try:
                number = input("Введите число либо строку: ")
                powered_number = int(number) ** power
                powered_numbers.append(powered_number)
            except ValueError:
                powered_numbers.append(str(number) * power)
        print(powered_numbers)

    @staticmethod
    def task_2() -> NoReturn:
        ans = {}
        string = str(input("Введите строку: ")).replace(" ", "").lower()
        for i in string:
            ans[i] = string.count(i)
        print(ans)

    @staticmethod
    def task_3() -> NoReturn:
        dct = {1: 11, 2: 22, 3: 33, 4: 4, 5: 33, 6: 1}
        keys = set()
        values = set()
        for k, v in dct.items():
            keys.add(k)
            values.add(v)
        print(f"Множество ключей: {keys}, Множество значений: {values}")
        ans = keys | values
        print("Обьединенное множество: ", ans)

    @staticmethod
    def task_4_1() -> NoReturn:
        dictionary = {
            "Имя": ["Андрей", "Кирилл", "Анна", "Евгений", "Евгений", "Александр", "Татьяна", "Аркадий", "Игорь",
                    "Кирилл"],
            "Фамилия": ["Иванов", "Лазарев", "Петрова", "Надобников", "Никитин", "Иванов", "Никитина", "Лихачев",
                        "Никитин", "Левашев"],
            "Город проживания": ["Москва", "Омск", "Псков", "Псков", "Москва", "Псков", "Москва", "Омск", "Псков",
                                 "Москва"],
            "Год рождения": [2000, 1987, 2003, 1993, 2001, 2001, 1976, 1957, 1969, 1999],
            "Месяц рождения": [6, 4, 11, 12, 9, 9, 5, 2, 3, 6],
            "Число рождения": [11, 25, 5, 3, 27, 31, 13, 12, 28, 24],
            "Статус": ["Студент", "Работает", "Школьница", "Работает", "Студент", "Студент", "Работает", "Пенсия",
                       "Работает", "Студент"]
            }

        def update_data(data) -> dict:
            updated_data = {}
            for i in range(len(data["Имя"])):
                full_name = data["Фамилия"][i] + " " + data["Имя"][i]
                if data["Имя"][i] == "Кирилл":
                    updated_name = "Кириллл"
                else:
                    updated_name = data["Имя"][i]
                if data["Фамилия"][i] == "Никитин" and data["Город проживания"][i] == "Москва":
                    city = "Махачкала"
                else:
                    city = data["Город проживания"][i]
                birth_date = "{:04d}-{:02d}-{:02d}".format(data["Год рождения"][i], data["Месяц рождения"][i],
                                                           data["Число рождения"][i])
                updated_data[full_name] = {
                    "Дата рождения": birth_date,
                    "Город проживания": city,
                    "Статус": data["Статус"][i]
                }
            return updated_data

        def remove_deceased(data) -> dict:
            updated_data = {}
            for full_name, info in data.items():
                if full_name not in ["Иванов Александр", "Лихачев Аркадий"]:
                    updated_data[full_name] = info
            return updated_data

        updated_data = update_data(dictionary)
        updated_data = remove_deceased(updated_data)

        for full_name, info in updated_data.items():
            print(full_name)
            for key, value in info.items():
                print(f"{key}: {value}")

    @staticmethod
    def task_4_2() -> NoReturn:
        set1 = {6, 31, 14, 25, 19, 3, 55}
        set2 = {30, 22, 6, 79, 25}
        set3 = {9, 1, 22, 19, 30}

        combined_set = set1.union(set2).union(set3)

        not_in_sets = [x for x in range(1, max(combined_set) + 1) if x not in combined_set]

        difference = combined_set.difference(not_in_sets)

        print("Элементы, которые не вошли в множества:", not_in_sets)
        print("Разница между элементами множества и списком:", difference)


if __name__ == "__main__":
    Solution.task_1()
    # Solution.task_2()
    # Solution.task_3()
    # Solution.task_4_1()
    # Solution.task_4_2()