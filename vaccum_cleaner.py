
# Vacuum Cleancleaer Agent

def vacuum_cleaner_agent(room_a, room_b, position):
    print("Initial State:")
    print("Room A:", room_a)
    print("Room B:", room_b)
    print("Vacuum Cleaner Position:", position)
    print()

    # Continue until both rooms are clean
    while room_a == "Dirty" or room_b == "Dirty":

        if position == "A":
            if room_a == "Dirty":
                print("Vacuum is in Room A -> Suck")
                room_a = "Clean"
            else:
                print("Room A is already clean -> Move to Room B")
                position = "B"

        elif position == "B":
            if room_b == "Dirty":
                print("Vacuum is in Room B -> Suck")
                room_b = "Clean"
            else:
                print("Room B is already clean -> Move to Room A")
                position = "A"

    print("\nFinal State:")
    print("Room A:", room_a)
    print("Room B:", room_b)
    print("Vacuum Cleaner Position:", position)
    print("Goal Achieved: Both rooms are clean!")


# Input
room_a = input("Enter status of Room A (Clean/Dirty): ").capitalize()
room_b = input("Enter status of Room B (Clean/Dirty): ").capitalize()
position = input("Enter vacuum cleaner position (A/B): ").upper()

# Run the agent
vacuum_cleaner_agent(room_a, room_b, position)
