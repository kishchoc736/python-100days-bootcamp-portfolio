import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# the images in a list
set_of_choices = [rock, paper, scissors]


# get user choice or input and convert to integer
user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors:\n"))
computer_choice = random.randint(0,2)


# print the choices of the user and the computer
print("You chose\n")
print(set_of_choices[int(user_choice)] + "\n")
print("The computer chose: \n")
print(set_of_choices[computer_choice])

# check if both the choices are the same
# if so it is a draw
if user_choice == computer_choice:
    print("It is a draw")

# work out all the other combinations
elif user_choice == 0 and computer_choice == 1:
    print("You lose")

elif user_choice == 0 and computer_choice == 2:
    print("You win")

elif user_choice == 1 and computer_choice == 0:
    print("You win")

elif user_choice == 1 and computer_choice == 2:
    print("You lose")

elif user_choice == 2 and computer_choice == 0:
    print("You lose")

elif user_choice == 2 and computer_choice == 1:
    print("You win")



