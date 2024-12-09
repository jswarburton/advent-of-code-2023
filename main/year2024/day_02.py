from main.file_reader import read


def solve_1(input: list) -> int:
    total = 0
    for i in input:
        parts = [int(h) for h in i.split()]

        if check(parts):
            total += 1
    return total


def check(nums):
    is_increasing = all(nums[i - 1] < nums[i] for i in range(1, len(nums)))
    is_decreasing = all(nums[i - 1] > nums[i] for i in range(1, len(nums)))

    if not (is_increasing or is_decreasing):
        return False

    for i in range(1, len(nums)):
        diff = abs(nums[i - 1] - nums[i])
        if diff < 1 or diff > 3:
            return False

    return True


def solve_2(input: list) -> int:
    total = 0
    for i in input:
        parts = [int(h) for h in i.split()]

        if check(parts):
            total += 1
            continue

        for j in range(len(parts)):
            if check(parts[:j] + parts[j + 1 :]):
                total += 1
                break
    return total


if __name__ == "__main__":
    input = read("day02-01.txt", "main/year2024/resources")
    print(solve_1(input))  # 390
    print(solve_2(input))  # 439
