PIG GAME
    The goal of the game is to reach a maximum score of 100 points.
Players take turns rolling a six-sided die (with values from 1 to 6) and accumulating points.
Each player's score starts at 0.Who will be reach 100 points at first he is the winner of this game.
USAGE:
    For entertainment and Study
RULES AND DETAILS:
    The provided Python program is a simple dice rolling game for 2 to 4 players. Here's the concept of the program:

1. **Setting the Number of Players:**
   - The program starts by asking the user to enter the number of players, which should be between 2 and 4.
   - It checks if the input is valid (a digit between 2 and 4) and continues once a valid input is received.

2. **Game Logic:**
   - The goal of the game is to reach a maximum score of 100 points.
   - Players take turns rolling a six-sided die (with values from 1 to 6) and accumulating points.
   - Each player's score starts at 0.

3. **Player Turns:**
   - The program iterates through each player's turn in a loop.
   - For each player's turn, it displays a message indicating the player's turn number.
   - The player is given the option to roll the die (by typing 'y') or skip their turn (by typing anything else).
   - If the player chooses to roll, a random number between 1 and 6 is generated, and their current score is updated.
   - If the player rolls a 1, their current score is reduced by 10 points, and their turn ends.
   - The player's score is displayed after each roll.
   - The player can continue rolling until they choose to stop or roll a 1.

4. **Scoring:**
   - After each turn, the player's score for that turn is added to their total score.
   - The total score for each player is displayed.

5. **Winning Condition:**
   - The game continues until one of the players reaches or exceeds a maximum score of 100 points.
   - Once a player reaches the maximum score, the game ends, and the player with the highest score is declared the winner.
   - The program displays the winning player's number and their final score.

6. **Loop and Repetition:**
   - The game loop continues until a player wins, ensuring that each player takes turns until the game reaches its conclusion.

7. **Random Number Generation:**
   - The `random.randint` function is used to generate random numbers for the dice rolls.

8. **User Input Validation:**
   - The program validates user input to ensure that it meets the required criteria (e.g., the number of players, whether to roll the die).

Overall, this program implements a simple dice rolling game that allows multiple players to take turns and accumulate scores, with the first player to reach or exceed 100 points being declared the winner.