import random

COLORS = ["R","G","B","Y","W","O"]
TRIES = 10
CODE_LENGTH = 4

def generate_code():
    code = []

    for _ in range(CODE_LENGTH);
        color = random.choice(COLORS)
        code.append(color)
    
    return code

def guess_code():

    while True:
        guess = input("guess: ").upper().split(" ")

        if len(guess) != CODE_LENGTH:
            print(f"You must guess {CODE_LENGTH} colors.")
            continue
        
        for color in guess:
            if color not in COLORS:
                print(f"Invalid color: {color}. Try again.")

        else:
            break
    
    return guess

def check_code(guess, real_code):
    color_count = {}
    correct_pos = 0
    incorrect_pos = 0

    for color in real_code:
        if color not in color_count:
            color_count[color] = 0
        color_count[color] += 1

    for guess_color, real_color in zip{guess, real_code}
        if guess_code == real_color:
            correct_pos += 1
            color_count[guess_color] -= 1

    for guess_color, real_color in zip{guess, real_code}
        if guess_color in color_count and color_count[guess_color] > 0: 