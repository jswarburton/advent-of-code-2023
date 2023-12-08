from main.file_reader import read


def solve_1(input: list) -> int:
    return solve(input, swap_jokers=False)


def solve_2(input: list) -> int:
    return solve(input, swap_jokers=True)


def get_best_possible_hand(hand: str, sort_order: str) -> str:
    if "J" not in hand:
        return hand
    elif hand == "JJJJJ":
        return sort_order[0] * 5

    character_counts = {}
    for i in hand:
        if i != "J":
            character_counts[i] = character_counts.get(i, 0) + 1

    keys_with_max_value = [
        k for k, v in character_counts.items() if v == max(character_counts.values())
    ]

    joker_replacement = sort_items(keys_with_max_value, sort_order)[-1]

    return hand.replace("J", joker_replacement)


def sort_items_by_type(type_and_items: list, sort_order: str) -> list:
    order = ["five", "four", "full", "three", "two pair", "one pair", "high"]

    sorted_items = []

    type_to_items = dict()
    for o in order:
        for t, item in type_and_items:
            if t == o:
                type_to_items[o] = type_to_items.get(o, []) + [item]

    for k in type_to_items.keys():
        type_to_items[k] = sort_items(type_to_items[k], sort_order)

    for i in reversed(order):
        sorted_items += type_to_items.get(i, [])

    return sorted_items


def sort_items(items: list, sort_order: str) -> list:
    def custom_sort_key(string):
        return [sort_order.index(char) for char in string]

    return sorted(items, key=custom_sort_key, reverse=True)


def get_type(hand: str) -> str:
    character_counts = {}
    for i in hand:
        if i in character_counts:
            character_counts[i] += 1
        else:
            character_counts[i] = 1

    if len(character_counts) == 1:
        return "five"
    elif len(character_counts) == 5:
        return "high"
    elif len(character_counts) == 2 and any(v == 2 for v in character_counts.values()):
        return "full"
    elif any(v == 4 for v in character_counts.values()):
        return "four"
    elif any(v == 3 for v in character_counts.values()):
        return "three"
    elif len(character_counts) == 3 and any(v == 2 for v in character_counts.values()):
        return "two pair"
    elif any(v == 2 for v in character_counts.values()):
        return "one pair"


def solve(input: list, swap_jokers: bool) -> int:
    items = []
    hand_to_value = dict()

    sort_order = "AKQT98765432J" if swap_jokers else "AKQJT98765432"

    for i in input:
        hand, value = i.split()
        value = int(value)

        best_possible_hand = (
            get_best_possible_hand(hand, sort_order) if swap_jokers else hand
        )

        hand_type = get_type(best_possible_hand)
        hand_to_value[hand] = value

        items.append((hand_type, hand))

    sorted_items = sort_items_by_type(items, sort_order)

    total = 0
    for i in range(len(sorted_items)):
        total += (i + 1) * hand_to_value[sorted_items[i]]

    return total


if __name__ == "__main__":
    input = read("day07-01.txt")
    print(solve_1(input))  # 251058093
    print(solve_2(input))  # 249781879
