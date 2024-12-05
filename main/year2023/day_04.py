from main.file_reader import read


def solve_1(input: list) -> int:
    total = 0
    for i in input:
        card, rest = i.split(": ")
        winners, nums = rest.split(" | ")

        winners = winners.split()
        nums = nums.split()

        winners = {int(i) for i in winners}
        nums = {int(i) for i in nums}

        num_winners = len(winners.intersection(nums))

        if num_winners > 0:
            total += 2 ** (num_winners - 1)

    return total


def solve_2(input: list) -> int:
    extra_copies = dict()

    for i in input:
        card, rest = i.split(": ")
        _, card_num = card.split()
        card_num = int(card_num)

        winners, nums = rest.split(" | ")

        winners = winners.split()
        nums = nums.split()

        winners = {int(i) for i in winners}
        nums = {int(i) for i in nums}

        num_winners = len(winners.intersection(nums))

        extra_copies_of_this_one = extra_copies.get(card_num, 0)

        for j in range(num_winners):
            extra_copies[card_num + j + 1] = (
                extra_copies.get(card_num + j + 1, 0) + extra_copies_of_this_one + 1
            )

    return len(input) + sum(extra_copies.values())


if __name__ == "__main__":
    input = read("day04-01.txt", "main/year2023/resources")
    print(solve_1(input))  # 18619
    print(solve_2(input))  # 8063216
