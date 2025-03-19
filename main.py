from locations.entrance import entrance 
from locations.hallway import hallway

welcome_message = """Welcome to CODE World Campus!

You can navigate with directions such as 'east'.
You can look around with 'look'.
You can exit the game with 'exit'.

~~~~~~~~~~~~~~~~~~~~~
"""

locations = {
  "entrance": entrance,
  "hallway1": hallway
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

