# Programmers:  Lamar and kipalu
# Course:  CS151, Professor Ebert
# Due Date: March 24, 2026
# Programming Assignment:  Lab 8
# Problem Statement: Write a program to simulate rolling a pair of 6-sided dice based on how many times a user requests the dice to be rolled.
# Data In: We requested the amount of rolls the user wanted
# Data Out:  how many rolls, the sets from same rolls list
# Credits: Our code is based on a functioning pair of dice of being roll a amount of times
# Initial: none
import random

# Name: num_rolls
# Purpose: Ask the user how many times the pair of dice should be rolled
# Parameters: None
# Return: A positive integer given to use by the user.
def num_rolls():
    num = int(input("what is your number of rolls? "))
    while num <= 0:
        print("input invalid enter a valid positive integer")
        num = input("what is your number of rolls? ")
    return int(num)
# Name: Dice_1, Dice_2, total
# Purpose: Get the sums of Dice_1 + Dice_2
# Paramters:None
# Return: Sum of Dice_1 + Dice_2
def paired_dicerolls():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    return total
# Name: Star_set
# Purpose: return set_num amount of stars
# Parameters: set_num
# Return: return set_num amount of stars
def star_set(set_num):
    stars = "*" * set_num

    return stars
# Name: Main Function
# Purpose: find roll of pairs of dice wanted by user print result list, input rolls sets with stars
# Return: print result list, input rolls sets with stars
def main():
    set_list = [0]*13
    total_roll = num_rolls()
    for i in range(total_roll):
       set_list[paired_dicerolls()] += 1
    print(f"Rolling {total_roll} pairs of dice")
    print(set_list[2:])
    for i in range(len(set_list)):
      if set_list[i] != 0:
         set_num = set_list[i]
         stars = star_set(set_num)
         print(f"set of {i}: {stars}")
main()


