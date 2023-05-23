import random

COLORS = ["R", "G", "B", "Y", "W", "O"]
TRIES = 10
CODE_LENGTH = 4


def generate_code():
    return random.choices(COLORS, k=CODE_LENGTH)


def get_guess():
    while True:
        guess = input("Guess: ").upper().split()

        if len(guess) != CODE_LENGTH:
            print(f"You must guess {CODE_LENGTH} colors.")
            continue

        if not all(color in COLORS for color in guess):
            print("Invalid colors. The valid colors are:", *COLORS)
            continue

        return guess


def check_guess(guess, code):
    correct_pos = sum(guess[i] == code[i] for i in range(CODE_LENGTH))
    incorrect_pos = sum(guess.count(color) - code.count(color) for color in COLORS)

    return correct_pos, incorrect_pos


def play_game():
    print(f"Welcome to Mastermind! You have {TRIES} tries to guess the code.")
    print("The valid colors are:", *COLORS)

    code = generate_code()

    for attempt in range(1, TRIES + 1):
        guess = get_guess()
        correct_pos, incorrect_pos = check_guess(guess, code)

        if correct_pos == CODE_LENGTH:
            print(f"Congratulations! You guessed the code in {attempt} tries.")
            return

        print(f"Correct positions: {correct_pos} | Incorrect positions: {incorrect_pos}")

    print("Sorry, you ran out of tries. The code was:", *code)


if __name__ == "__main__":
    play_game()