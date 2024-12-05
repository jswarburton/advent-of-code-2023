from main.file_reader import read


def solve_1(input: list) -> int:
    total = 0
    for row in input:
        vals = row.split()
        vals = [int(x) for x in vals]

        all_diffs = []
        diffs = []

        for i in range(1, len(vals)):
            diffs.append(vals[i] - vals[i - 1])

        all_diffs.append(diffs)

        while set(diffs) != {0}:
            new_diffs = []
            for i in range(1, len(diffs)):
                new_diffs.append(diffs[i] - diffs[i - 1])

            diffs = new_diffs
            all_diffs.append(diffs)

        topup_value = 0
        for j in reversed(range(len(all_diffs))):
            topup_value += all_diffs[j][-1]
        total += vals[-1] + topup_value

    return total


def solve_2(input: list) -> int:
    total = 0
    for row in input:
        vals = row.split()
        vals = [int(x) for x in vals]

        all_diffs = []
        diffs = []

        for i in range(1, len(vals)):
            diffs.append(vals[i] - vals[i - 1])

        all_diffs.append(diffs)

        while set(diffs) != {0}:
            new_diffs = []
            for i in range(1, len(diffs)):
                new_diffs.append(diffs[i] - diffs[i - 1])

            diffs = new_diffs
            all_diffs.append(diffs)

        topup_value = 0
        for j in reversed(range(len(all_diffs) - 1)):
            topup_value = all_diffs[j][0] - topup_value
        total += vals[0] - topup_value

    return total


if __name__ == "__main__":
    input = read("day09-01.txt", "main/year2023/resources")
    print(solve_1(input))  # 1819125966
    print(solve_2(input))  # 1140
