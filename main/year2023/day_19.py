from main.file_reader import read


def solve_1(input: list) -> int:
    ratings, workflows = parse(input)

    return sum(accepted_total("in", rating, workflows) for rating in ratings)


def accepted_total(curr_poss, rating, workflows):
    total = 0
    while True:
        workflow = workflows[curr_poss]

        for rule in workflow:
            if ":" in rule:
                first, second = rule.split(":")

                if "<" in first:
                    val, num = first.split("<")
                    num = int(num)

                    if rating[val] < num:
                        if second == "A":
                            total += sum(rating.values())
                            return total
                        elif second == "R":
                            return total
                        else:
                            curr_poss = second
                            break
                elif ">" in first:
                    val, num = first.split(">")
                    num = int(num)

                    if rating[val] > num:
                        if second == "A":
                            total += sum(rating.values())
                            return total
                        elif second == "R":
                            return total
                        else:
                            curr_poss = second
                            break
            elif rule == "A":
                total += sum(rating.values())
                return total
            elif rule == "R":
                return total
            else:
                curr_poss = rule
                break


def solve_2(input: list) -> int:
    ratings, workflows = parse(input)

    paths = []

    def rec(path_so_far, curr_pos):
        if curr_pos == "A":
            paths.append(path_so_far)
            return
        elif curr_pos == "R":
            return

        for i, rule in enumerate(workflows[curr_pos]):
            prevs = workflows[curr_pos][0:i]
            prevs = ["!" + prev.split(":")[0] for prev in prevs]

            if ":" in rule:
                first, second = rule.split(":")

                rec(path_so_far + prevs + [first], second)
            else:
                rec(path_so_far + prevs, rule)

    rec([], "in")

    total = 0

    for path in paths:
        x_min, x_max = 1, 4000
        m_min, m_max = 1, 4000
        a_min, a_max = 1, 4000
        s_min, s_max = 1, 4000

        for p in path:
            if "!" in p and "<" in p:
                a, b = p[1:].split("<")
                p = a + ">" + str(int(b) - 1)
            elif "!" in p and ">" in p:
                a, b = p[1:].split(">")
                p = a + "<" + str(int(b) + 1)

            if "<" in p:
                first, second = p.split("<")
                second = int(second)

                if first == "x":
                    x_max = min(x_max, second - 1)
                elif first == "m":
                    m_max = min(m_max, second - 1)
                elif first == "a":
                    a_max = min(a_max, second - 1)
                elif first == "s":
                    s_max = min(s_max, second - 1)
            elif ">" in p:
                first, second = p.split(">")
                second = int(second)

                if first == "x":
                    x_min = max(x_min, second + 1)
                elif first == "m":
                    m_min = max(m_min, second + 1)
                elif first == "a":
                    a_min = max(a_min, second + 1)
                elif first == "s":
                    s_min = max(s_min, second + 1)

        total += (
            (1 + (x_max - x_min))
            * (1 + (m_max - m_min))
            * (1 + (a_max - a_min))
            * (1 + (s_max - s_min))
        )

    return total


def parse(input):
    workflows = dict()
    ratings = []
    doing_workflows = True
    for i in input:
        if not i:
            doing_workflows = False
            continue

        if doing_workflows:
            name, rest = i.split("{")
            rest = rest[:-1]
            rules = rest.split(",")

            workflows[name] = rules
        else:
            these_ratings = dict()
            rs = i[1:-1]
            rs = rs.split(",")
            for r in rs:
                k, v = r.split("=")
                these_ratings[k] = int(v)
            ratings.append(these_ratings)
    return ratings, workflows


if __name__ == "__main__":
    input = read("day19-01.txt", "main/year2023/resources")
    print(solve_1(input))  # 342650
    print(solve_2(input))  # 130303473508222
