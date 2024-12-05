from main.file_reader import read


def solve_1(input: list) -> int:
    seeds, mappings = parse(input)

    location_nums = []

    for seed in seeds:
        for mapping in mappings:
            for dest_range_start, source_range_start, range_length in mapping:
                if source_range_start <= seed < source_range_start + range_length:
                    seed = dest_range_start + (seed - source_range_start)
                    break

        location_nums.append(seed)

    return min(location_nums)


def solve_2(input: list) -> int:
    seeds, mappings = parse(input)
    seed_ranges = [(seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)]

    reversed_mappings = list(reversed(mappings))

    location = 0
    while True:
        seed = location
        for mapping in reversed_mappings:
            for source_range_start, dest_range_start, range_length in mapping:
                if source_range_start <= seed < source_range_start + range_length:
                    seed = dest_range_start + (seed - source_range_start)
                    break

        if any(start <= seed < (start + length) for start, length in seed_ranges):
            return location
        location += 1


def parse(input):
    _, seeds = input[0].split(": ")
    seeds = [int(i) for i in seeds.split()]

    mappings = []
    range_infos = []
    for i in input[2:]:
        if not i:
            mappings.append(range_infos)
            range_infos = []
        elif "map" in i:
            pass
        else:
            dest_range_start, source_range_start, range_length = i.split()
            dest_range_start = int(dest_range_start)
            source_range_start = int(source_range_start)
            range_length = int(range_length)

            range_infos.append((dest_range_start, source_range_start, range_length))
    mappings.append(range_infos)

    return seeds, mappings


if __name__ == "__main__":
    input = read("day05-01.txt", "main/year2023/resources")
    print(solve_1(input))  # 424490994
    print(solve_2(input))  # 15290096
