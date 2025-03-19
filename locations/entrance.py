def look():
  return "You are in the entrance area. Behind you is a broken elevator. In front of you a leather couch. The hallway continues to the [east]."

entrance = {
  "look": {
    "output": look,
    "next_location_id": None
  },
  "east": {
    "output": lambda: "You go east.",
    "next_location_id": "hallway1"
  },
}