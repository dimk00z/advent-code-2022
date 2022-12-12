# A for Rock, B for Paper, and C for Scissors.
# A Y
# B X
# C Z

strategy: dict[str, dict[str, str | int]] = {
    "X": {"letter": "A", "value": 1, "beat": "C", "defeat": "B"},
    "Y": {"letter": "B", "value": 2, "beat": "A", "defeat": "C"},
    "Z": {"letter": "C", "value": 3, "beat": "B", "defeat": "A"},
}

cheats: dict = {"X": "lose", "Y": "draw", "Z": "win"}


def fight(opponent: str, you_choice: str) -> int:
    if strategy[you_choice]["letter"] == opponent:
        return strategy[you_choice]["value"] + 3
    if strategy[you_choice]["beat"] == opponent:
        return strategy[you_choice]["value"] + 6

    return strategy[you_choice]["value"]


def fight_with_tactics(opponent: str, you_choice: str) -> int:
    match cheats[you_choice]:
        case "lose":
            for key in strategy:
                if strategy[key]["defeat"] == opponent:
                    you_choice = key
                    break
        case "win":
            for key in strategy:
                if strategy[key]["beat"] == opponent:
                    you_choice = key
                    break
        case "draw":
            for key in strategy:
                if strategy[key]["letter"] == opponent:
                    you_choice = key
                    break
    return fight(opponent, you_choice)


def main():
    score: int = 0
    cheated_score: int = 0
    test = ("A Y", "B X", "C Z")
    for line in test:
        opponent, you_choice = line.split()
        fight_score: int = fight(opponent, you_choice)
        score += fight_score
        cheated_fight: int = fight_with_tactics(opponent, you_choice)
        cheated_score += cheated_fight
        print(cheated_fight)

    print(score, cheated_score)
    score = 0
    cheated_score = 0
    with open("./day_2/input.txt") as file:
        for line in file:
            opponent, you_choice = line.strip().split()
            score += fight(opponent, you_choice)
            cheated_fight: int = fight_with_tactics(opponent, you_choice)
            cheated_score += cheated_fight

    print(score, cheated_score)


if __name__ == "__main__":
    main()
