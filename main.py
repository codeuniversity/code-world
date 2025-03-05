welcome_message = """Welcome to CODE World Campus!

You can navigate with directions such as 'east'.
You can look around with 'look'.
You can exit the game with 'exit'.

~~~~~~~~~~~~~~~~~~~~~
"""

locations = {
  "entrance": "You are in the entrance area. Behind you is a broken elevator. In front of you a leather couch. The hallway continues to the [east].",
  "hallway1": "You are in a hallway with a table. The table has a bowl of apples on it. Maybe you can [take] one? The way returns [west]."
}

current_location = locations["entrance"]

print(welcome_message)
print(current_location)

while True:
  user_input = input("> ")

  if user_input == "exit":
    print("Thanks for playing!")
    break
  elif user_input == "look":
    print(current_location)
  elif current_location == locations["entrance"] and user_input == "east":
    current_location = locations["hallway1"]
    print(current_location)
  
  elif current_location == locations["hallway1"] and user_input == "west":
    current_location = locations["entrance"]
    print(current_location)
  
  else:
    print("Please enter a valid command.")

