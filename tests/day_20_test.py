from main import file_reader
from main.day_20 import solve_1

input1 = file_reader.read(file_name="day20-1.txt", path="tests/resources")
input2 = file_reader.read(file_name="day20-2.txt", path="tests/resources")


def test_solve_1():
    assert solve_1(input1) == 32000000
    assert solve_1(input2) == 11687500
