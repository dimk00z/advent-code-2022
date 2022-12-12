def main():
    max_cals: int = 0
    current_cals: int = 0
    elves_cals: list[int] = []
    with open("./day_1/input.txt") as file:
        for line in file:
            if line.strip() != "":
                current_cals += int(line.strip())
                continue
            elves_cals.append(max(max_cals, current_cals))
            current_cals = 0
    print(max(elves_cals))
    print(sum(sorted(elves_cals, reverse=True)[:3]))


if __name__ == "__main__":
    main()
