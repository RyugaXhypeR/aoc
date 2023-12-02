with open("inputs/day_02.txt") as file:
    IN = file.read().strip().splitlines()

TEST1 = """\
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
""".splitlines()

R, G, B = 12, 13, 14


def is_valid(ln):
    for st in ln.split(";"):
        r, g, b = 0, 0, 0
        for s in st.split(","):
            i, c = s.split()
            if c[0] == "b":
                b += int(i)
            elif c[0] == "g":
                g += int(i)
            elif c[0] == "r":
                r += int(i)
        if r > R or g > G or b > B:
            return False
    return True

def max_clr(ln):
    r, g, b = [], [], []
    for st in ln.split(";"):
        for s in st.split(","):
            i, c = s.split()
            if c[0] == "b":
                b += [int(i)]
            elif c[0] == "g":
                g += [int(i)]
            elif c[0] == "r":
                r += [int(i)]
    return max(r), max(g), max(b)


def part1(inp):
    s = 0
    for ln in inp:
        g, st = ln.split(":")
        if is_valid(st):
            s += int(g.split()[-1])
    return s

def part2(inp):
    s = 0
    for ln in inp:
        g, st = ln.split(":")
        r, g, b = max_clr(st)
        s += r * g * b
    return s


if __name__ == "__main__":
    print(part1(IN))
    print(part2(IN))
