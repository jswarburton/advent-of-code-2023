import functools

from main.file_reader import read


def solve_1(input: list) -> int:
    return solve(input)


def solve_2(input: list) -> int:
    return solve(input, 5)


def solve(input: list, multiplier: int = 1) -> int:
    total = 0

    progress = 0
    for i in input:
        progress += 1

        pattern, dist = i.split()
        dist = [int(d) for d in dist.split(",")]

        pattern = "?".join([pattern] * multiplier)
        dist = dist * multiplier

        total += count_matches(pattern, len(pattern), tuple(dist))

    return total


@functools.cache
def count_matches(remaining_pattern, size, remaining_dist):
    if len(remaining_dist) == 0:
        if all(c in ".?" for c in remaining_pattern):
            return 1
        return 0

    dist_value = remaining_dist[0]
    remaining_dist = remaining_dist[1:]

    # min required remaining pattern length
    after = sum(remaining_dist) + len(remaining_dist)

    count = 0

    for before in range(size - after - dist_value + 1):
        candidate_prefix = "." * before + "#" * dist_value + "."
        if all(
            c0 == c1 or c0 == "?" for c0, c1 in zip(remaining_pattern, candidate_prefix)
        ):
            count += count_matches(
                remaining_pattern[len(candidate_prefix) :],
                size - dist_value - before - 1,
                remaining_dist,
            )

    return count


if __name__ == "__main__":
    input = read("day12-01.txt", "main/year2023/resources")
    print(solve_1(input))  # 6981
    print(solve_2(input))  # 4546215031609
