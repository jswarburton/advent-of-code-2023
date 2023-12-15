from main.file_reader import read


def solve_1(input: str) -> int:
    inputs = input.split(",")

    total = 0
    for i in inputs:
        total += hash_alg(i)

    return total


def solve_2(input: str) -> int:
    boxes = [[] for _ in range(256)]

    inputs = input.split(",")

    for i in inputs:
        if "-" in i:
            label, _ = i.split("-")
            box_num = hash_alg(label)

            index = find_index_startswith(boxes[box_num], label + "=")
            if index != -1:
                boxes[box_num].pop(index)
        else:
            label, _ = i.split("=")
            box_num = hash_alg(label)
            index = find_index_startswith(boxes[box_num], label + "=")
            if index != -1:
                boxes[box_num][index] = i
            else:
                boxes[box_num].append(i)

    total = 0
    for i in range(len(boxes)):
        for j, b in enumerate(boxes[i]):
            _, focal_length = b.split("=")
            total += (i + 1) * (j + 1) * int(focal_length)

    return total


def hash_alg(input: str) -> int:
    curr_value = 0
    for c in input:
        ascii_code = ord(c)
        curr_value += ascii_code
        curr_value *= 17
        curr_value %= 256

    return curr_value


def find_index_startswith(lst, prefix):
    for i, string in enumerate(lst):
        if string.startswith(prefix):
            return i
    return -1


if __name__ == "__main__":
    input = read("day15-01.txt")
    input = input[0]
    print(solve_1(input))  # 502139
    print(solve_2(input))  # 284132
