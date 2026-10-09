from collections import deque

def water_jug(capacity1, capacity2, target):
    queue = deque([(0, 0)])
    visited = set()

    while queue:
        a, b = queue.popleft()

        if (a, b) in visited:
            continue
        visited.add((a, b))

        print("Jug 1:", a, "Jug 2:", b)

        if a == target or b == target:
            print("Target reached!")
            return

        states = [
            (capacity1, b),
            (a, capacity2),
            (0, b),
            (a, 0),
            (a - min(a, capacity2 - b), b + min(a, capacity2 - b)),
            (a + min(b, capacity1 - a), b - min(b, capacity1 - a))
        ]

        for state in states:
            if state not in visited:
                queue.append(state)

water_jug(4, 3, 2)
