from random import sample
import time

#  Set up constants and select code
guesses = 0
WAIT = 5
incorrect = 0
COLOURS = ["red", "orange", "yellow", "green", "blue", "purple"]
code = sample(COLOURS, k=4)


# Blank resets the screen
def blank():  # Resets the screen
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()


def red(text):  # Converts text to said colour
    return "\033[91m{}\033[0m".format(text)


def green(text):
    return "\033[92m{}\033[0m".format(text)


def yellow(text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(255, 255, 0, text)


def blue(text):
    return "\033[94m{}\033[0m".format(text)


def orange(text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(255, 165, 0, text)


def purple(text):
    return "\033[95m{}\033[0m".format(text)


def colours_text(move):  # Assumes three letter format, sets a string to it's corresponding colour
    if move == "pur":
        move = purple(move)
    if move == "red":
        move = red(move)
    if move == "ora":
        move = orange(move)
    if move == "yel":
        move = yellow(move)
    if move == "gre":
        move = green(move)
    if move == "blu":
        move = blue(move)
    return move


def board(colour1, colour2, colour3, colour4):  # Prints the board, which is the users colours in three letters
    print("                                                             ", colours_text(colour1[0:3]), " ",
          colours_text(colour2[0:3]), " ", colours_text(colour3[0:3]), " ", colours_text(colour4[0:3]), end="")
    print("      ", correctColour, "-", correctSpot)
    print("------------------------------------------------------------------------------------------------------")


print("--Welcome to MasterMind!--")
time.sleep(WAIT)
blank()
print("I have chosen a code made out of four separate colours, a combination of", red("red,"), orange("orange,"),
      yellow("yellow,"), green("green,"), blue("blue,"), "and", purple("purple."))
print("You have six tries to guess the code. If you guess it within six tries you win, if not, I win.")
print(
    "After each guess I will tell you how many of the colours you guess are correct, and how many colours are correct in in the correct spot in the list")
time.sleep(WAIT + 3)
blank()
print("Okay, I have my code. Start guessing.")
print("Your guess must be in proper format; all lowercase, no commas. Example: red blue green yellow")
time.sleep(WAIT + 2)
blank()

while guesses < 6:  # Main loop of code that runs the game
    correctSpot = 0
    correctColour = 0
    move = input("Your guess:")
    move = move.split()
    for h in range(0, len(move)):  # Finding invalid move
        if move[h] == 'red' or move[h] == 'orange' or move[h] == 'yellow' or move[h] == 'green' or move[h] == 'blue' or move[h] == 'purple':
            continue
        else:
            incorrect = 1
            print("Invalid input. Please try again")
            break
    if incorrect == 1 or len(move) > 4:
        incorrect = 0
        continue
    for i in range(0, 4):  # Logic
        if move[i] == code[i]:
            correctSpot += 1
        for j in range(0, 4):
            if move[j] == code[i] and j != i:
                correctColour += 1
    c1 = move[0]
    c2 = move[1]
    c3 = move[2]
    c4 = move[3]
    print(correctColour, "colours right,", correctSpot, "in the right spot")
    board(c1, c2, c3, c4)
    if move == code:
        time.sleep(WAIT - 2)
        blank()
        print("You guessed my code. Good job, you won!")
        break
    guesses += 1

if guesses >= 6:
    time.sleep(WAIT)
    blank()
    print("You ran out of guesses. You lose!")
    print("The code was:", code)
    time.sleep(WAIT)
