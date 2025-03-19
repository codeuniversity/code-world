def fallback(user_input):
  return f"You entered the command: {user_input}"

hall = {
  "look": {
    "output": lambda: "You are in a large room with many doors and numbers on them. Enter a number to pick the room you want to enter.",
    "next_location_id": None
  },
  "west": {
    "output": lambda: "You return to the hallway.",
    "next_location_id": "hallway1"
  },
  "fallback": {
    "output": fallback,
    "next_location_id": None
  },
}