import math

from main.file_reader import read


def solve_1(input: list) -> int:
    conjunction_input_states, flip_flop_states, name_to_destinations = parse(input)

    high_pulses_sent, low_pulses_sent = 0, 0

    for _ in range(1000):
        queue = [("broadcaster", "low", "button")]
        low_pulses_sent += 1

        while queue:
            point, pulse, from_point = queue.pop(0)

            if point not in name_to_destinations:
                continue

            if point in flip_flop_states and pulse == "high":
                continue
            elif point in flip_flop_states and pulse == "low":
                pulse = "high" if not flip_flop_states[point] else "low"
                flip_flop_states[point] = not flip_flop_states[point]
            elif point in conjunction_input_states:
                states = conjunction_input_states[point]
                states[from_point] = pulse

                pulse = (
                    "low"
                    if all(state == "high" for state in states.values())
                    else "high"
                )

            for dest in name_to_destinations[point]:
                queue.append((dest, pulse, point))
                if pulse == "low":
                    low_pulses_sent += 1
                else:
                    high_pulses_sent += 1

    return high_pulses_sent * low_pulses_sent


def solve_2(input: list) -> int:
    # &hf feeds into rx
    # => rx receives low pulse when  hf has received high from all inputs
    # hf inputs: 4 %points: nd, pc, vd, tx
    # nd receives from &bd
    # pc receives from &bp
    # vd receives from &pm
    # tx receives from &xn

    # 4 distinct subgraphs => detect cycle of each and take lcm of cycle lengths

    conjunction_input_states, flip_flop_states, name_to_destinations = parse(input)

    first_low = {"nd": 0, "pc": 0, "vd": 0, "tx": 0}

    i = 0
    while True:
        if all(c != 0 for c in first_low.values()):
            return math.lcm(*list(first_low.values()))

        i += 1
        queue = [("broadcaster", "low", "button")]
        while queue:
            point, pulse, from_point = queue.pop(0)

            if point in first_low and pulse == "low":
                first_low[point] = i

            if point not in name_to_destinations:
                continue

            if point in flip_flop_states and pulse == "high":
                continue
            elif point in flip_flop_states and pulse == "low":
                pulse = "high" if not flip_flop_states[point] else "low"
                flip_flop_states[point] = not flip_flop_states[point]
            elif point in conjunction_input_states:
                things = conjunction_input_states[point]
                things[from_point] = pulse

                if all(a == "high" for a in things.values()):
                    pulse = "low"
                else:
                    pulse = "high"

            for dest in name_to_destinations[point]:
                queue.append((dest, pulse, point))


def parse(input):
    name_to_destinations = {}
    flip_flop_states = {}
    conjunction_input_states = {}
    for i in input:
        name, destinations = i.split(" -> ")
        destinations = destinations.split(", ")

        if "%" in name:
            name = name.split("%")[1]
            flip_flop_states[name] = False
        elif "&" in name:
            name = name.split("&")[1]
            conjunction_input_states[name] = dict()

        name_to_destinations[name] = destinations
    for i in conjunction_input_states:
        for name, destinations in name_to_destinations.items():
            if i in destinations:
                conjunction_input_states[i][name] = "low"
    return conjunction_input_states, flip_flop_states, name_to_destinations


if __name__ == "__main__":
    input = read("day20-01.txt", "main/year2023/resources")
    print(solve_1(input))  # 807069600
    print(solve_2(input))  # 221453937522197
