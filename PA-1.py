# Programmers: Lamar Holloway
# Course: CS151
# Due Date: 2/18/26
# Lab Assignment: Lab 3
# Problem Statement: Our program finds points earned from a jumper on a ski jump based on hill type and jumper speed, the program then outputs a message based on points earned
# Data In: yes/no and expand/sell
# Data Out: business failed/survived, Final Cash and Final Business Value
# Credits: Based on Zybooks
# Business Simulator Game
# Cash = float
# Business Value = int
cash = 1000.0
value = 50
print("Welcome to the Business Simulator!")
print(f"Starting Cash: ${cash}")
print(f"Starting Business Value: {value}")
print("----------------------------------")

# 1. IDEA STAGE
print("Stage 1: Idea & Planning")
choice = input("Do market research? (yes/no): ").lower()

if choice.lower() == "yes":
    cash -= 500.0
    value += 10
else:
    value -= 5

# 2. FUNDING STAGE
print("\nStage 2: Funding")
choice = input("Take a loan? (yes/no): ").lower()

if choice == "yes":
    cash += 10000.0
    value += 15
else:
    cash += 2000.0
    value += 5

# 3. LAUNCH STAGE
print("\nStage 3: Launch")
choice = input("Invest in marketing? (yes/no): ").lower()

if choice == "yes":
    cash -= 2000.0
    value += 20
else:
    value -= 10

# 4. GROWTH STAGE
print("\nStage 4: Growth")
choice = input("Hire employees? (yes/no): ").lower()

if choice == "yes":
    cash -= 3000.0
    value += 25
else:
    value -= 5

# 5. CRISIS STAGE
print("\nStage 5: Crisis")
choice = input("Fix the problem quickly? (yes/no): ").lower()

if choice == "yes":
    cash -= 1500.0
    value += 10
else:
    value -= 30

# 6. EXPANSION OR SELL
print("\nStage 6: Final Decision")
choice = input("Expand or sell? (expand/sell): ").lower()

if choice == "expand":
    cash -= 5000.0
    value += 40
elif choice == "sell":
    cash += value * 100.0
    print("\nYou sold your business!")

print("\n===== FINAL RESULTS =====")
print(f"Final Cash: ${cash:.2f}")
print(f"Final Business Value: {value}")

if cash <= 0 or value <= 0:
    print("Your business failed.")
else:
    print("Your business survived!")
