import random
rock = ('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')

paper = ('''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
''')

scissors = ('''
   _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if (user==0):
    print(rock)
elif (user==1):
    print(paper)
elif (user==2):
    print(scissors)

   

computer = random.randint(0,2)
print("Computer choose")
if (computer==0):
    print(rock)
elif (computer==1):
    print(paper)
elif (computer==2):
    print(scissors)
    
if user>=3 or user<0:
    print("You chose an invalid number!!")
elif user==0 and computer ==2:
    print("You win!!")
elif computer==0 and user==2:
    print("You lose")
elif computer>user:
    print("You lose")
elif user>computer:
    print("You win!!")
elif computer==user:
    print("It's a draw")
    
    

    
    

