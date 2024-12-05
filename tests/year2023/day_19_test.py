from main import file_reader
from main.year2023.day_19 import solve_1, solve_2

input = file_reader.read(file_name="day19.txt", path="tests/year2023/resources")


def test_solve_1():
    assert solve_1(input) == 19114


def test_solve_2():
    assert solve_2(input) == 167409079868000