import random

while True:
    print("< ----------------- ROCK PAPER SCISSORS GAME ----------------- >")
    number = input(
        "Choose: \n 1. for rock \n 2. for paper \n 3. for scissors \n 0. for quit \n"
    )

    myChoice = "exit"
    if number == "1":
        myChoice = "rock"
    elif number == "2":
        myChoice = "paper"
    elif number == "3":
        myChoice = "scissors"

    if myChoice == "exit":
        break

    if myChoice != "rock" and myChoice != "paper" and myChoice != "scissors":
        print("Please choose a correct answer")
        continue

    computer_answer = random.choice(["rock", "paper", "scissors"])
    print(f"Computer chose: {computer_answer}")

    if myChoice == computer_answer:
        print("Tied")
    elif myChoice == "paper" and computer_answer == "rock":
        print("You Won!")
        break
    elif myChoice == "rock" and computer_answer == "scissors":
        print("You Won!")
        break
    elif myChoice == "scissors" and computer_answer == "paper":
        print("You Won!")
        break
    else:
        print("You Lost, Try again!")
