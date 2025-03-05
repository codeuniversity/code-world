welcome_message = """Welcome to CODE World Campus!

You can navigate with directions such as 'east'.
You can look around with 'look'.
You can exit the game with 'exit'.

~~~~~~~~~~~~~~~~~~~~~
"""

current_location = "You are in the entrance area. Behind you is a broken elevator. In front of you a leather couch. The hallway continues to the [east]."

print(welcome_message)
print(current_location)

while True:
  user_input = input("> ")

  if user_input == "exit":
    print("Thanks for playing!")
    break
  elif user_input == "look":
    print(current_location)
  else:
    print("Please enter a valid command.")

