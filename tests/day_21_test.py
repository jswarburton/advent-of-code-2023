from main import file_reader
from main.day_21 import solve_1

input = file_reader.read(file_name="day21.txt", path="tests/resources")


def test_solve_1():
    assert solve_1(input, steps=6) == 16
