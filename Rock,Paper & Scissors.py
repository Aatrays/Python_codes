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

a = True

while a == True:

  user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

  if user == 0:
    print(rock)
  elif user == 1:
    print(paper)
  else:
    print(scissors)

  computer = [rock,paper,scissors]

  x = len(computer)

  choice = random.randint(0,x)

  if choice == 0:
    print(f"Computer Chose: {rock}")
  elif choice == 1:
    print(f"Computer Chose: {paper}")
  else:
    print(f"Computer Chose: {scissors}")

  if user == 0 and choice == 0:
    print("Result is: Draw")
  elif user == 1 and choice == 1:
    print("Result is: Draw")
  elif user == 2 and choice == 2:
    print("Result is: Draw")
  elif user == 0 and choice == 1:
    print("Result is: Computer Won")
  elif user == 0 and choice == 2:
    print("Result is: User Won")
  elif user == 1 and choice == 0:
    print("Result is: User Won")
  elif user == 1 and choice == 2:
    print("Result is: Computer Won")
  elif user == 2 and choice == 0:
    print("Result is: Computer Won")
  elif user == 2 and choice == 1:
    print("Result is: User Won")
