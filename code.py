import tkinter as tk
import random

# Initialize main window
root = tk.Tk()
root.title("Rock, Paper, Scissors - Ultimate Edition")
root.geometry("600x600")
root.configure(bg="#282c34")

# Global variables
choices = ["Rock", "Paper", "Scissors"]
player_score = 0
ai_score = 0
wins_needed = 5
rounds_remaining = wins_needed
game_mode = "Classic"

# Game logic
def play_round(player_choice):
    global player_score, ai_score, rounds_remaining

    if player_score >= wins_needed or ai_score >= wins_needed:
        result_label.config(text="Game Over! Start a new game!", fg="yellow")
        return

    ai_choice = random.choice(choices)
    result = ""
    if player_choice == ai_choice:
        result = f"Draw! Both chose {ai_choice}."
        color = "gray"
    elif (player_choice == "Rock" and ai_choice == "Scissors") or \
         (player_choice == "Paper" and ai_choice == "Rock") or \
         (player_choice == "Scissors" and ai_choice == "Paper"):
        result = f"You win this round! {player_choice} beats {ai_choice}."
        color = "green"
        player_score += 1
    else:
        result = f"You lose this round! {ai_choice} beats {player_choice}."
        color = "red"
        ai_score += 1

    result_label.config(text=result, fg=color)
    update_scores()

    if player_score >= wins_needed:
        result_label.config(text="Congratulations! You won the game!", fg="green")
    elif ai_score >= wins_needed:
        result_label.config(text="You lost! The AI won the game!", fg="red")

def update_scores():
    score_label.config(text=f"Player: {player_score} | AI: {ai_score}")
    rounds_label.config(text=f"Rounds Remaining: {rounds_remaining}")

def reset_game():
    global player_score, ai_score, rounds_remaining, game_mode
    player_score = 0
    ai_score = 0
    rounds_remaining = wins_needed
    result_label.config(text="Make your move!", fg="white")
    update_scores()

def set_game_mode(mode):
    global game_mode, wins_needed, rounds_remaining
    game_mode = mode
    if game_mode == "Classic":
        wins_needed = 5
    else:
        wins_needed = 10
    rounds_remaining = wins_needed
    reset_game()
    toggle_mode_buttons()

def toggle_mode_buttons():
    if game_mode == "Classic":
        mode_5_rounds_button.config(state="disabled", relief="sunken")
        mode_10_rounds_button.config(state="normal", relief="raised")
    else:
        mode_10_rounds_button.config(state="disabled", relief="sunken")
        mode_5_rounds_button.config(state="normal", relief="raised")

# GUI Elements
tk.Label(root, text="Rock, Paper, Scissors - Ultimate Edition", font=("Helvetica", 20, "bold"), bg="#282c34", fg="white").pack(pady=20)

# Game mode selection
mode_frame = tk.Frame(root, bg="#282c34")
tk.Label(mode_frame, text="Select Game Mode:", font=("Helvetica", 14), bg="#282c34", fg="white").grid(row=0, column=0, padx=10)

mode_5_rounds_button = tk.Button(mode_frame, text="First to 5 Wins", font=("Helvetica", 12), bg="#61afef", fg="white", command=lambda: set_game_mode("Classic"))
mode_5_rounds_button.grid(row=0, column=1, padx=10)

mode_10_rounds_button = tk.Button(mode_frame, text="First to 10 Wins", font=("Helvetica", 12), bg="#61afef", fg="white", command=lambda: set_game_mode("Extended"))
mode_10_rounds_button.grid(row=0, column=2, padx=10)

mode_frame.pack(pady=10)

# Score display
score_label = tk.Label(root, text=f"Player: {player_score} | AI: {ai_score}", font=("Helvetica", 16), bg="#282c34", fg="white")
score_label.pack(pady=10)

rounds_label = tk.Label(root, text=f"Rounds Remaining: {rounds_remaining}", font=("Helvetica", 16), bg="#282c34", fg="white")
rounds_label.pack(pady=10)

# Result display
result_label = tk.Label(root, text="Make your move!", font=("Helvetica", 18), bg="#282c34", fg="white")
result_label.pack(pady=20)

# Player move buttons
button_frame = tk.Frame(root, bg="#282c34")
tk.Button(button_frame, text="Rock", font=("Helvetica", 14), bg="#98c379", fg="white", command=lambda: play_round("Rock")).grid(row=0, column=0, padx=20, pady=10)
tk.Button(button_frame, text="Paper", font=("Helvetica", 14), bg="#e5c07b", fg="white", command=lambda: play_round("Paper")).grid(row=0, column=1, padx=20, pady=10)
tk.Button(button_frame, text="Scissors", font=("Helvetica", 14), bg="#e06c75", fg="white", command=lambda: play_round("Scissors")).grid(row=0, column=2, padx=20, pady=10)
button_frame.pack(pady=20)

# Reset button
tk.Button(root, text="Reset Game", font=("Helvetica", 14), bg="#d19a66", fg="white", command=reset_game).pack(pady=20)

# Initialize the game in Classic mode
set_game_mode("Classic")

# Run the game
root.mainloop()
