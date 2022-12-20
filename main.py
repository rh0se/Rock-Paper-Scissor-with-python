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

#Write your code below this line 👇
game = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors \n"))
if game > 2 and game < 0:
   print("You typed an invalid number, You lose.")
elif game == 0:
  print(rock)
elif game == 1:
  print(paper)
elif game == 2:
  print(scissors)

import random
project = [rock, paper, scissors]
selection = random.choice(project)
chosen = print("Computer chose:\n" + selection)


if game == 0 and selection == scissors:
  print("You win")
elif game == 1 and selection == rock:
  print("You win")
elif game == 2 and selection == paper:
      print("You win")
elif game == 0 and selection == rock:
  print("It's a draw")
elif game == 2 and selection == scissors:
  print("It's a draw")
elif game == 1 and selection == paper:
    print("It's a draw")
else:
  print("You Lose.")
