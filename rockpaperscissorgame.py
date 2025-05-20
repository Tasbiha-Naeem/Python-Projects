import random
print("ROCK-PAPER-SCISSOR-GAME")

item_list=["Rock","Paper","Scissor"]

user_choice=input("Enter your move:")
computer_choice=random.choice(item_list)

print(f"User choice:{user_choice}")
print(f"Computer choice:{computer_choice}")

if user_choice==computer_choice:
    print("Both chooses same")
    print("Match tie...")
elif user_choice=="Rock":
    if computer_choice=="Paper":
        print("Paper covers rock")
        print("Computer Win...")
    else:
        print("Rock smashes scissor")
        print("You win...")
elif user_choice=="Paper":
    if computer_choice=="Scissor":
        print("Scissor cut paper")
        print("Computer win...")
    else:
        print("Paper covers rock")
        print("You win...")
elif user_choice=="Scissor":
    if computer_choice=="Rock":
        print("Rock smashes scissor")
        print("Computer win...")
    else:
        print("Scissor cut paper")
        print("You win...")

