
import random

moves = ["rock", "paper", "scissors"]

player_score = 0
ai_score = 0
player_history = []

def get_ai_move():
    return random.choice(moves)

def determine_winner(player, ai):
    if player == ai:
        return "tie"
    elif (
        (player == "rock" and ai == "scissors") or
        (player == "scissors" and ai == "paper") or
        (player == "paper" and ai == "rock")
    ):
        return "player"
    else:
        return "ai"

print("=== ROCK, PAPER, SCISSORS ===")

while True:
    player = input("\nChoose Rock, Paper, or Scissors (or type quit): ").lower().strip()

    if player == "quit":
        break

    if player not in moves:
        print("Invalid choice! Please choose Rock, Paper, or Scissors.")
        continue

    ai = get_ai_move()

    print("You chose:", player.capitalize())
    print("AI chose:", ai.capitalize())

    player_history.append(player)

    winner = determine_winner(player, ai)

    if winner == "tie":
        print("It's a tie!")
    elif winner == "player":
        print("You win this round!")
        player_score += 1
    else:
        print("The AI wins this round!")
        ai_score += 1

    print("\n--- SCOREBOARD ---")
    print("Player:", player_score)
    print("AI:", ai_score)

print("\n=== FINAL SCORE ===")
print("Player:", player_score)
print("AI:", ai_score)

if player_score > ai_score:
    print("Congratulations! You won the game!")
elif ai_score > player_score:
    print("The AI won the game!")
else:
    print("The game ended in a tie!")

print("Thanks for playing!")
