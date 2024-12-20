# rock paper scissors game
import random
items=["Rock","Paper","Scissors"]
user_choice=input("Enter your move Rock Paper Scissors- ")
comp_choice=random.choice(items)

print(f"User choice is {user_choice} and computer choice is {comp_choice}")
if user_choice==comp_choice:
    print("Both are same match is tie ")
elif user_choice=="Rock":
    if comp_choice=="scissors":
        print("You win Rock smashes Scissors")
    else:
        print("computer wins Paper covers rock")
elif user_choice=="Scissors":
    if comp_choice=="Paper":
        print("You win Scissors cuts paper")
    else:
        print("computer rock smashes scissors")
elif user_choice=="Paper":
    if comp_choice=="Rock":
        print("You win paper covers rock")
    else:
        print("computer win scissors cuts the paper")