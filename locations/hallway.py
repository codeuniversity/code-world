apple_count = 0

def look():
  return "You are in a hallway with a table. The table has a bowl of apples on it. Maybe you can [take] one? The way returns [west]."

def west():
  return "You go west."

def take():
  global apple_count
  apple_count = apple_count + 1

  if apple_count > 5:
    return "There are no more apples left."
  else:
    return f"You take one apple. You now have {apple_count} apple."

hallway = {
  "look": {
    "output": look,
    "next_location_id": None
  },
  "west": {
    "output": west,
    "next_location_id": "entrance"
  },
  "take": {
    "output": take,
    "next_location_id": None
  },
}