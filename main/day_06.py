from main.file_reader import read


def solve_1(input: list) -> int:
    times = [int(t) for t in input[0].split(":")[1].split()]
    distances = [int(d) for d in input[1].split(":")[1].split()]

    return solve(times, distances)


def solve_2(input: list) -> int:
    times = [int("".join(input[0].split(":")[1].split()))]
    distances = [int("".join(input[1].split(":")[1].split()))]

    return solve(times, distances)


def solve(times, distances):
    product = 1
    for time, distance in zip(times, distances):
        num = 0

        for time_held in range(1, time + 1):
            distance_covered = time_held * (time - time_held)
            if distance_covered > distance:
                num += 1

        product *= num

    return product


if __name__ == "__main__":
    input = read("day06-01.txt")
    print(solve_1(input))  # 219849
    print(solve_2(input))  # 29432455
