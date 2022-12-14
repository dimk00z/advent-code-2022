TEST_DATA = [
    "2-4,6-8",
    "2-3,4-5",
    "5-7,7-9",
    "2-8,3-7",
    "6-6,4-6",
    "2-6,4-8",
]


def parse_line(line: str, numbers: int) -> list[set[int]]:
    parts: list[str] = line.split(",")
    parts_numbers: list[set[int]] = []
    for part in parts:
        start, fininsh = tuple(map(int, part.split("-")))
        parts_numbers.append(set(range(start, fininsh + 1)))
    parts_numbers.sort(reverse=True)
    return parts_numbers


def check_over_lap(parts_numbers: list[set[int]]):
    if len(parts_numbers[0].intersection(parts_numbers[-1])):
        return True
    return False


def check_subset(parts_numbers: list[set[int]]) -> bool:
    return parts_numbers[-1].issubset(parts_numbers[0])


def main():
    # part 1
    pairs: int = 0
    over_laps: int = 0
    for line in TEST_DATA:
        parts = parse_line(line=line, numbers=2)
        if check_subset(parts):
            pairs += 1
        if check_over_lap(parts):
            over_laps += 1
    print(pairs, over_laps)
    # part 2
    pairs = 0
    over_laps = 0
    with open("./day_4/input.txt") as file:
        for line in file:
            parts = parse_line(line=line, numbers=2)
            if check_subset(parts):
                pairs += 1
            if check_over_lap(parts):
                over_laps += 1
    print(pairs, over_laps)


if __name__ == "__main__":
    main()
