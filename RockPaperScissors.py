
round = int(input("How many rounds do you want to play: "))
for i in range (1,round+1):
    print("Round ", i)
    player1 = input("Player 1, enter your choice: ")
    player2 = input("Player 2, enter your choice: ")
    if player1 == player2:
        print("It's a tie! play again")
    elif player1 == "rock":
        if player2 == "scissors":
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")
    elif player1 == "scissors":
        if player2 == "paper":
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")
    elif player1 == "paper":
        if player2 == "rock":
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")

print("Game Over...!!")