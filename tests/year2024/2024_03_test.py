from main.year2024.day_03 import solve_1, solve_2


def test_solve_1():
    input = ["xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"]
    assert solve_1(input) == 161


def test_solve_2():
    input = [
        "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    ]
    assert solve_2(input) == 48
