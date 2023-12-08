from main.file_reader import read


def solve_1(input: list) -> int:
    total = 0

    stringified = ""
    for i in input:
        for j in i:
            if j.isdigit():
                stringified += j
                break

        for k in i[::-1]:
            if k.isdigit():
                stringified += k
                break

        total += int(stringified)
        stringified = ""

    return total


def solve_2(input: list) -> int:
    mapping = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9",
    }

    min_keys = {}
    max_keys = {}

    total = 0
    for i in input:
        for a in mapping.keys():
            if a in i:
                min_keys[a] = i.index(a)

        for a in mapping.keys():
            if a in i:
                max_keys[a] = i.rfind(a)

        min_key = min(min_keys, key=min_keys.get)
        max_key = max(max_keys, key=max_keys.get)

        total += int(mapping[min_key] + mapping[max_key])

        min_keys = {}
        max_keys = {}

    return total


if __name__ == "__main__":
    input = read("day01-01.txt")
    print(solve_1(input))  # 54601
    print(solve_2(input))  # 54078
