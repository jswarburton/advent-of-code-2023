from main.file_reader import read
import heapq


def solve_1(grid: list) -> int:
    grid = [[int(y) for y in x] for x in grid]
    return solve(grid, 1, 3)


def solve_2(grid: list) -> int:
    grid = [[int(y) for y in x] for x in grid]
    return solve(grid, 4, 10)


def solve(grid, min_dist, max_dist):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    q = [(0, 0, 0, -1)]  # cost, x, y, disallowed_dir
    seen = set()
    costs = {}
    while q:
        cost, x, y, disallowed_dir = heapq.heappop(q)
        if x == len(grid) - 1 and y == len(grid[0]) - 1:
            return cost
        if (x, y, disallowed_dir) in seen:
            continue
        seen.add((x, y, disallowed_dir))
        for direction in range(len(directions)):
            cost_increase = 0
            if direction == disallowed_dir or (direction + 2) % 4 == disallowed_dir:
                continue
            for distance in range(1, max_dist + 1):
                xx = x + directions[direction][0] * distance
                yy = y + directions[direction][1] * distance
                if 0 <= xx < len(grid) and 0 <= yy < len(grid[0]):
                    cost_increase += grid[xx][yy]
                    if distance < min_dist:
                        continue
                    nc = cost + cost_increase
                    if costs.get((xx, yy, direction), 1e100) <= nc:
                        continue
                    costs[(xx, yy, direction)] = nc
                    heapq.heappush(q, (nc, xx, yy, direction))


if __name__ == "__main__":
    input = read("day17-01.txt")
    print(solve_1(input))  # 635
    print(solve_2(input))  # 734
