from itertools import islice

TEST_DATA = [
    "vJrwpWtwJgWrhcsFMMfFFhFp",
    "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    "PmmdzqPrVvPwwTWBwg",
    "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    "ttgJtRGJQctTZtZT",
    "CrZsJsPPZsGzwwsLwLmpwMDw",
]


def chunk(it, size):
    it = iter(it)
    return iter(lambda: tuple(islice(it, size)), ())


def get_parts(rucksack: str, parts_number) -> list[set[str]]:
    return [set(part) for part in chunk(rucksack, parts_number)]


def parse_rucksack(parts: list[set[str]]) -> int:
    share_element: str = list(parts[0].intersection(*parts[1:]))[0]
    start_lower: int = 96
    start_upper: int = 64 - 26
    result: int = (
        ord(share_element) - start_lower if share_element.islower() else ord(share_element) - start_upper
    )
    return result


def main():
    # part 1
    count: int = 0

    with open("./day_3/input.txt") as file:
        for line in file:
            parts: list[set[str]] = get_parts(line.strip(), int(len(line) / 2))
            count += parse_rucksack(parts=parts)
    print(count)
    # part 2
    count = 0

    with open("./day_3/input.txt") as file:
        parts: list[set] = []
        for line in file:
            parts.append(set(line.strip()))
            if len(parts) < 3:
                continue
            count += parse_rucksack(parts=parts)
            parts = []
    print(count)


if __name__ == "__main__":
    main()
