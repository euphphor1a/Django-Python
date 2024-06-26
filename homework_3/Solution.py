from typing import List


class Calculator:
    def operate(self, op, x, y):
        return {
            '1': x + y,
            '2': x - y,
            '3': x * y,
            '4': x / y if y != 0 else None,
            '5': x ** y,
        }.get(op, None)

    def run_calculator(self):
        while True:
            print("Выберите операцию:")
            print("1. Сложение")
            print("2. Вычитание")
            print("3. Умножение")
            print("4. Деление")
            print("5. Возведение в степень")
            print("6. Выход")

            choice = input("Введите номер операции: ")

            if choice == '6':
                print("Программа завершена.")
                break

            if choice not in {'1', '2', '3', '4', '5'}:
                print("Некорректный ввод. Пожалуйста, выберите операцию от 1 до 6.")
                continue

            try:
                num1 = float(input("Введите первое число: "))
                num2 = float(input("Введите второе число: "))
            except ValueError:
                print("Ошибка: введите числа корректно.")
                continue

            result = self.operate(choice, num1, num2)
            if result is not None:
                print("Результат:", result)
            else:
                print("Ошибка: деление на ноль недопустимо.")


def multiply_elements(lst: List[int | float], multiplier: int | float = 2) -> List[int | float]:
    return [x * multiplier for x in lst]


multiply_lambda = lambda lst, multiplier=2: [x * multiplier for x in lst]


def function_name(search: str, status: bool, *args: int | str, **kwargs: str | int) -> List[int] | str:
    result = []
    result_2 = ""
    if search == "args":
        if status:
            for i in args:
                if isinstance(i, int):
                    result.append(i)
            return result
        else:
            for i in args:
                result_2 += f" {i}"
            return result_2
    elif search == "kwargs":
        for k, v in kwargs.items():
            result_2 += (" Key: {}, Value: {}; ".format(k, v))
        return result_2
    else:
        raise ValueError("Error for search")


class Wallet:
    payment_system = "WalletPay"

    def __init__(self, name: str, currency: str):
        self._balance = 0
        self.name = name
        self.currency = currency

        if currency not in ("USD", "EUR", "RUB"):
            raise ValueError("Unsupported currency")

    def deposit(self, amount: float):
        self._balance += amount
        print(f"Баланс кошелька {self.name} успешно пополнен на {amount} {self.currency}")

    def withdraw(self, amount: float):
        if self._balance >= amount:
            self._balance -= amount
            print(f"Оплата с кошелька {self.name} на сумму {amount} {self.currency} прошла успешно")
        else:
            print("Ошибка: недостаточно средств на кошельке")

    def balance_info(self):
        print(f"На кошельке {self.name} {self._balance} {self.currency}")

    def delete_account(self):
        del self


class CryptoWallet(Wallet):
    def __init__(self, name: str, currency: str, coin: str):
        super().__init__(name, currency)
        self.coin = coin

    def balance_info(self):
        print(f"На кошельке {self.name} {self._balance} {self.coin}")

    def balance_in_usd(self, btc_price: float, eth_price: float):
        if self.coin == "BTC":
            usd_balance = self._balance * btc_price
        elif self.coin == "ETH":
            usd_balance = self._balance * eth_price
        else:
            raise ValueError("Unsupported coin")

        print(f"На кошельке {self.name} {usd_balance} USD")