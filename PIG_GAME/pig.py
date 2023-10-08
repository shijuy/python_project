import random


def roll():
    min_value = 1
    max_value = 6
    num = random.randint(min_value, max_value)

    return num


while True:
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid, try again.")

max_score = 100
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    for i in range(players):
        print("\nPlayer number", i + 1, "turn has just started!")
        currentvalue = 0

        while True:
            doroll = input("Would you like to roll (y)? ")
            if doroll.lower() != "y":
                break

            value = roll()
            if value == 1:
                currentvalue -= 10
                print("Oops You rolled a 1! Sorry Turn done! and Your value was subract by 10")
                break
            else:
                currentvalue += value
                print("You rolled a:", value)

            print("Your score is:", currentvalue)

        player_scores[i] += currentvalue
        print(player_scores[i])
        print("Your total score is:", player_scores[i])

max_score = max(player_scores)
winner = player_scores.index(max_score)
print("Player number", winner + 1,"is the winner with a score of:", max_score)