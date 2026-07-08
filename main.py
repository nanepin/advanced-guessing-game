import random

score = 0

while True:

    print("Choose difficulty: easy / hard")
    mode = input("Mode: ")

    if mode == "easy":
        max_tries = 7
        max_number = 10
    else:
        max_tries = 5
        max_number = 20

    secret = random.randint(1, max_number)
    tries = 0

    print("Guess the number between 1 and", max_number)

    while tries < max_tries:
        guess = int(input("Your guess: "))
        tries = tries + 1

        if guess == secret:
            print("Correct!")
            score = score + 1
            break

        difference = abs(secret - guess)

        if difference <= 2:
            print("Very close!")
        else:
            print("Far away!")

        if guess < secret:
            print("Too small!")
        else:
            print("Too big!")

        print("Tries left:", max_tries - tries)

    if guess != secret:
        print("You lost. The number was", secret)

    print("Score:", score)

    again = input("Play again? yes/no: ")

    if again != "yes":
        print("Game over.")
        break
