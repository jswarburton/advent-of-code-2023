from main.year2023.day_06 import solve_1, solve_2

input = ["Time:      7  15   30", "Distance:  9  40  200"]


def test_solve_1():
    assert solve_1(input) == 288


def test_solve_2():
    assert solve_2(input) == 71503
