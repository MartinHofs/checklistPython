def count_rooms(cave):
    """Count the room itself and every room reachable through its tunnels."""
    count = 1  # Count this room
    for tunnel in cave["tunnels"]:
        count += count_rooms(tunnel)  # Recursively count rooms in tunnels
    return count

def total_gold(cave):
    """Add the gold of the room and of every room reachable through its tunnels."""
    total = cave["gold"]  # Start with this room's gold
    for tunnel in cave["tunnels"]:
        total += total_gold(tunnel)  # Recursively add gold from tunnels
    return total

def find_room(cave, name):
    """Look for the room called name in this room or anywhere below it."""
    if cave["name"] == name:
        return cave  # Found the room
    for tunnel in cave["tunnels"]:
        found = find_room(tunnel, name)  # Recursively search tunnels
        if found is not None:
            return found  # Return the found room
    return None  # Room not found

def depth(cave):
    """How many rooms long the longest path is, counting the room itself."""
    if not cave["tunnels"]:
        return 1  # No tunnels means depth is 1
    max_depth = 0
    for tunnel in cave["tunnels"]:
        max_depth = max(max_depth, depth(tunnel))  # Recursively find max depth
    return 1 + max_depth  # Add this room to the depth of the deepest tunnel

CAVE_MAP = {
    "name": "Entrance", "gold": 0, "tunnels": [
        {"name": "Mushroom Hall", "gold": 15, "tunnels": []},
        {"name": "Crystal Gallery", "gold": 40, "tunnels": [
            {"name": "Echo Chamber", "gold": 5, "tunnels": []},
            {"name": "Dragon's Den", "gold": 200, "tunnels": [
                {"name": "Hidden Vault", "gold": 500, "tunnels": []},
            ]},
        ]},
        {"name": "Flooded Pit", "gold": 0, "tunnels": []},
    ],
}

def main(): # Prints the results of the functions on the CAVE_MAP
    print("Rooms:", count_rooms(CAVE_MAP))
    print("Gold:", total_gold(CAVE_MAP))
    print("Depth:", depth(CAVE_MAP))
    print(f"Found Room: {find_room(CAVE_MAP, 'Hidden Vault')['name']} with {find_room(CAVE_MAP, 'Hidden Vault')['gold']} gold")
    print(f"Missing Room: {find_room(CAVE_MAP, 'Nonexistent Room')}")

if __name__ == "__main__":
    main()