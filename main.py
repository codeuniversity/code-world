welcome_message = """Welcome to CODE World Campus!

You can navigate with directions such as 'east'.
You can look around with 'look'.
You can exit the game with 'exit'.

~~~~~~~~~~~~~~~~~~~~~
"""

locations = {
  "entrance": {
    "look": {
      "output": "You are in the entrance area. Behind you is a broken elevator. In front of you a leather couch. The hallway continues to the [east].",
      "next_location_id": None
    },
    "east": {
      "output": "You go east.",
      "next_location_id": "hallway1"
    },
  },
  "hallway1": {
    "look": {
      "output": "You are in a hallway with a table. The table has a bowl of apples on it. Maybe you can [take] one? The way returns [west].",
      "next_location_id": None
    },
    "west": {
      "output": "You go west.",
      "next_location_id": "entrance"
    },
  }
}

current_location = locations["entrance"]

print(welcome_message)
print(current_location["look"]["output"])

while True:
  user_input = input("> ")

  if user_input == "exit":
    print("Thanks for playing!")
    break
  if user_input in current_location:
    output = current_location[user_input]["output"]
    next_location_id = current_location[user_input]["next_location_id"]
    
    print(output)

    if next_location_id:
      current_location = locations[next_location_id]
      print(current_location["look"]["output"])
    
  else:
    print("Please enter a valid command.")