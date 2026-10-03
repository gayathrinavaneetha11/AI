# Vacuum Cleaner Problem

rooms = ["Clean", "Dirty"]
positions = ["A", "B"]

state = 1

for A in rooms:
    for B in rooms:
        for pos in positions:

            print("\nState", state)
            print("Room A:", A)
            print("Room B:", B)
            print("Vacuum:", pos)

            cost = 0

            if A == "Dirty":
                cost += 1
            if B == "Dirty":
                cost += 1

            print("Total Cost:", cost)

            if A == "Clean" and B == "Clean":
                print("Goal State")

            state += 1

print("\nTotal States:", state - 1)
print("Goal: Both rooms Clean")
