from main.day_15 import solve_1, solve_2

input = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"


def test_solve_1():
    assert solve_1(input) == 1320


def test_solve_2():
    assert solve_2(input) == 145
