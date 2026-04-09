# Programmers:  Lamar
# Course:  CS151, Professor Ebert
# Due Date: February 25, 2026
# Programming Assignment:  PA-2
# Problem Statement: make a game where you can go aginst a computer or player
# Data In: "fire", "water", "earth", "air", "lightning"
# Data Out:winner
# Credits: class and internet search


import random

elements = ["fire", "water", "earth", "air", "lightning"]

# Winning rules dictionary
wins_against = {
    "fire": ["air", "earth"],
    "water": ["fire", "lightning"],
    "earth": ["water", "lightning"],
    "air": ["water", "earth"],
    "lightning": ["air", "fire"]
}
# Name: get_computer_choice
# Purpose: return random elements from elements
# Parameters: None
# Return: random elements
def get_computer_choice():
    return random.choice(elements)
# Name: determine_winner
# Purpose:determine winner
# Parameters: None
# Return: number for player 1 or 2
def determine_winner(choice1, choice2):
    if choice1 == choice2:
        return 0  # tie
    elif choice2 in wins_against[choice1]:
        return 1  # player 1 wins
    else:
        return 2  # player 2 wins
# Name: get_human_choice
# Purpose:get human input for element
# Parameters: player_name
# Return: choice
def get_human_choice(player_name):
    while True:
        choice = input(f"{player_name}, choose {elements}: ").lower()
        if choice in elements:
            return choice
        print("Invalid choice. Try again.")
# Name: play_match
# Purpose:play the force of element game
# Parameters: none
# Return: winner
def play_match():
    print("Welcome to Elemental Clash!")
    
    # Choose match length
    while True:
        rounds = int(input("Enter an odd number for best-of match: "))
        if rounds % 2 == 1 and rounds > 0:
            break
        print("Please enter a positive odd number.")
    
    wins_needed = rounds // 2 + 1
    
    # Choose player types
    p1_type = input("Is Player 1 human or computer? ").lower()
    p2_type = input("Is Player 2 human or computer? ").lower()
    
    p1_score = 0
    p2_score = 0
    
    while p1_score < wins_needed and p2_score < wins_needed:
        # Player 1 choice
        if p1_type == "human":
            p1_choice = get_human_choice("Player 1")
        else:
            p1_choice = get_computer_choice()
            print(f"Player 1 (Computer) chose {p1_choice}")
        
        # Player 2 choice
        if p2_type == "human":
            p2_choice = get_human_choice("Player 2")
        else:
            p2_choice = get_computer_choice()
            print(f"Player 2 (Computer) chose {p2_choice}")
        
        # Determine winner
        result = determine_winner(p1_choice, p2_choice)
        
        if result == 1:
            print("Player 1 wins this round!")
            p1_score += 1
        elif result == 2:
            print("Player 2 wins this round!")
            p2_score += 1
        else:
            print("It's a tie!")
        
        print(f"Score → Player 1: {p1_score} | Player 2: {p2_score}\n")
    
    # Final winner
    if p1_score > p2_score:
        print("🎉 Player 1 wins the match!")
    else:
        print("🎉 Player 2 wins the match!")

play_match()
