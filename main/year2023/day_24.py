from main.file_reader import read

from itertools import combinations

from sympy import symbols, Symbol, solve, Eq


def solve_1(input: list, start=200000000000000, end=400000000000000) -> int:
    ps_and_vs = parse(input)

    total = 0
    for a, b in combinations(ps_and_vs, 2):
        (ax, ay, _), (vax, vay, _) = a
        (bx, by, _), (vbx, vby, _) = b

        line1 = get_slope_and_intercept(ax, ay, vax, vay)
        line2 = get_slope_and_intercept(bx, by, vbx, vby)

        intersection_x, intersection_y = find_intersection(line1, line2)

        if intersection_x is None or intersection_y is None:
            continue
        if (intersection_x < ax and vax >= 0) or (intersection_x > ax and vax <= 0):
            continue
        if (intersection_x < bx and vbx >= 0) or (intersection_x > bx and vbx <= 0):
            continue
        if (intersection_y < by and vby >= 0) or (intersection_y > by and vby <= 0):
            continue
        if (intersection_y < ay and vay >= 0) or (intersection_y > ay and vay <= 0):
            continue

        if start <= intersection_x <= end and start <= intersection_y <= end:
            total += 1

    return total


def get_slope_and_intercept(x0, y0, dx, dy):
    slope = dy / dx
    intercept = y0 - slope * x0
    return slope, intercept


def find_intersection(line1, line2):
    m1, b1 = line1
    m2, b2 = line2

    if m1 == m2:
        x_intersection = None
        y_intersection = None
    else:
        x_intersection = (b2 - b1) / (m1 - m2)
        y_intersection = m1 * x_intersection + b1

    return x_intersection, y_intersection


def solve_2(input: list) -> int:
    ps_and_vs = parse(input)

    throw_start_x, throw_start_y, throw_start_z, throw_vx, throw_vy, throw_vz = symbols(
        "throw_start_x throw_start_y throw_start_z throw_vx throw_vy throw_vz"
    )

    equations = []
    t_symbols = []
    for idx, pv in enumerate(ps_and_vs[:3]):
        (x0, y0, z0), (xv, yv, zv) = pv

        t = Symbol("t" + str(idx))
        t_symbols.append(t)

        eq_x = Eq(throw_start_x + throw_vx * t, x0 + xv * t)
        eq_y = Eq(throw_start_y + throw_vy * t, y0 + yv * t)
        eq_z = Eq(throw_start_z + throw_vz * t, z0 + zv * t)
        equations.extend([eq_x, eq_y, eq_z])

    solution = solve(
        equations,
        *(
            [throw_start_x, throw_start_y, throw_start_z, throw_vx, throw_vy, throw_vz]
            + t_symbols
        ),
    )
    return solution[0][0] + solution[0][1] + solution[0][2]


def parse(input):
    ps_and_vs = []
    for i in input:
        ps, vs = i.split(" @ ")
        px, py, pz = map(int, ps.split(", "))
        vx, vy, vz = map(int, vs.split(", "))

        ps_and_vs.append(((px, py, pz), (vx, vy, vz)))
    return ps_and_vs


if __name__ == "__main__":
    input = read("day24-01.txt", "main/year2023/resources")
    print(solve_1(input))  # 16018
    print(solve_2(input))  # 1004774995964534
