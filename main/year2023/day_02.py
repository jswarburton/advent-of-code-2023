from main.file_reader import read


def solve_1(input: list) -> int:
    total = 0
    for i in input:
        game_id, b = i.split(": ")

        games = b.split("; ")
        games = [game.split(", ") for game in games]

        possible = True
        for game in games:
            num_red, num_blue, num_green = get_color_totals(game)
            if num_red > 12 or num_blue > 14 or num_green > 13:
                possible = False
                break

        if possible:
            total += int(game_id.split(" ")[1])
    return total


def get_color_totals(balls):
    num_red, num_blue, num_green = 0, 0, 0
    for ball in balls:
        num, color = ball.split(" ")
        num = int(num)
        if color == "red":
            num_red = num
        elif color == "blue":
            num_blue = num
        elif color == "green":
            num_green = num
    return num_red, num_blue, num_green


def solve_2(input: list) -> int:
    total2 = 0
    for i in input:
        max_blue, max_green, max_red = 0, 0, 0
        game_id, b = i.split(": ")

        games = b.split("; ")
        games = [game.split(", ") for game in games]

        color_totals = [get_color_totals(game) for game in games]

        for num_red, num_blue, num_green in color_totals:
            if num_red > max_red:
                max_red = num_red
            if num_blue > max_blue:
                max_blue = num_blue
            if num_green > max_green:
                max_green = num_green

        total2 += max_red * max_blue * max_green

    return total2


if __name__ == "__main__":
    input = read("day02-01.txt", "main/year2023/resources")
    print(solve_1(input))  # 2239
    print(solve_2(input))  # 83435
