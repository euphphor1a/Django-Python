import unittest
import timeit
import sys

from for_test import factorial


class TestFactorial(unittest.TestCase):
    def test_factorial_positive_number(self):
        start_time = timeit.default_timer()
        result = factorial(5)
        end_time = timeit.default_timer()
        print(f"Время выполнения теста test_factorial_positive_number: {end_time - start_time} секунд")
        self.assertEqual(result, 120)

    def test_factorial_zero(self):
        start_time = timeit.default_timer()
        result = factorial(0)
        end_time = timeit.default_timer()
        print(f"Время выполнения теста test_factorial_zero: {end_time - start_time} секунд")
        self.assertEqual(result, 1)

    def test_factorial_negative_number(self):
        start_time = timeit.default_timer()
        with self.assertRaises(ValueError):
            factorial(-5)
        end_time = timeit.default_timer()
        print(f"Время выполнения теста test_factorial_negative_number: {end_time - start_time} секунд")

    def test_factorial_large_number(self):
        start_time = timeit.default_timer()
        with self.assertRaises(ValueError):
            factorial(1000)
        end_time = timeit.default_timer()
        print(f"Время выполнения теста test_factorial_large_number: {end_time - start_time} секунд")

    def test_factorial_sys_maxsize(self):
        start_time = timeit.default_timer()
        result = factorial(sys.maxsize)
        end_time = timeit.default_timer()
        print(f"Время выполнения теста test_factorial_sys_maxsize: {end_time - start_time} секунд")
        self.assertIsInstance(result, int)


if __name__ == '__main__':
    unittest.main()
