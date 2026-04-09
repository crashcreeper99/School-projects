# Programmers:  Lamar and alula
# Course:  CS151, Professor Ebert
# Due Date: march 17, 2026
# Programming Assignment:  Lab 7
# Problem Statement:  Our code is an ATM that allows the user to deposit, withdraw, see their balance, or exit with function
# Data In: We requested the amount of money the user wanted to deposit or withdraw. We also asked the user is they wanted to see their balance or exit the program
# Data Out:  We displayed the balance after the deposit, the withdrawal, or just the balance alone
# Credits: Our code is based on a functioning ATM
# Initial balance 1000

def vaild_option():
    d_choice = input(str("(D)eposit \n(W)ithdraw \n(B)alance \n(E)xit ")).upper().strip()
    while d_choice != "D" and d_choice != "W" and d_choice != "B" and d_choice != "E":
        print("This is not a valid choice.")
        d_choice = input(str("(D)eposit \n(W)ithdraw \n(B)alance \n(E)xit ")).upper().strip()
    return d_choice


def valid_floatnum(action):
    d_input = input(f"enter a number for {str(action)}")
    input_new = d_input.replace(".", " ")
    while input_new.isdigit() == False or float(d_input) < 0:
        print("This is not a valid postive number.")
        d_input = input("enter a number")
        input_new = d_input.replace(".", " ")
    return d_input


# Output purpose and do priming read
def main():
    balance = 1000
    sentinel = 'E'
    print("This program is an ATM")
    choice = vaild_option()
    while choice != sentinel:

        # User chose deposit
        if choice == "D":
            deposit = valid_floatnum("deposit")
# keep asking for deposit amount until it's valid
            balance += float(deposit)
# Notify user if balance went negative
            if balance < 0:
                print("You have a negative balance, 5% charge will occur")
# user chose withdraw
        elif choice == "W":
# keep asking for withdrawal amount until it's valid
           withdraw = valid_floatnum("withdraw")
           balance -= float(withdraw)
# Notify user if balance went negative
           if balance < 0:
             print("You have a negative balance, 5% charge will occur")

        elif choice == "B":
         print(f"Balance is ${balance:.2f}")
        choice = vaild_option()
    print("Thanks for banking")

main()
