from for_test import average_num


def test_average_num_valid_input():
    assert average_num([1, 2, 3, 4, 5]) == 3.0


def test_average_num_mixed_input():
    assert average_num([1, 2.5, 3, 4, 5.5]) == 3.0


def test_average_num_empty_list():
    assert average_num([]) == 0.0


def test_average_num_negative_numbers():
    assert average_num([-1, -2, -3, -4, -5]) == -3.0


def test_average_num_float_input():
    assert average_num([1.5, 2.5, 3.5, 4.5, 5.5]) == 3.5


def test_average_num_string_input():
    assert average_num(['1', '2', '3', '4', '5']) == 3.0


def test_average_num_mixed_string_input():
    assert average_num(['1', 2, '3', 4, '5']) == 3.0


def test_average_num_invalid_input():
    assert average_num(['a', 'b', 'c']) == "Bad request"
