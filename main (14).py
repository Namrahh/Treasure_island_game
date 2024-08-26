from art import logo1
print(logo1)
print("Welcome to the treasure island.")

print("Your mission is to find the treasure.")

choice1 = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'.").lower()

if choice1 == "left":
  print("Let's go")
else:
  print("You fell into hole. Game over.")
  exit()

choice2 = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.").lower()

if choice2 == "wait":
  choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, one blue. which color do you choose?").lower()
  if choice3 == "red":
    print("It's a room full of fire. Game over.")
  elif choice3 == "yellow":
    print("You found the treasure! You win!")
  elif choice3 == "blue":
    print("You enter a room of beasts. Game over.")
  else:
    print("You chose a door that doesn't exist. Game over.")
else:
  print("You get attacked by an angry trout. Game over.")