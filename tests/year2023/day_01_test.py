from main.year2023.day_01 import solve_1, solve_2


def test_solve_1():
    input = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
    assert solve_1(input) == 142


def test_solve_2():
    input = [
        "two1nine",
        "eightwothree",
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen",
    ]
    assert solve_2(input) == 281
