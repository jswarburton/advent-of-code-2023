from main import file_reader
from main.year2023.day_11 import solve_1, solve_2

input = file_reader.read(file_name="day11.txt", path="tests/year2023/resources")


def test_solve_1():
    assert solve_1(input) == 374


def test_solve_2():
    assert solve_2(input) == 82000210
