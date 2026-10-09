from heapq import heappush, heappop

start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

def heuristic(state):
    return sum(state[i] != 0 and state[i] != goal[i]
               for i in range(9))

def solve(start):
    queue = []
    heappush(queue, (heuristic(start), 0, start, []))
    visited = set()

    while queue:
        _, cost, state, path = heappop(queue)

        if state == goal:
            for step in path + [state]:
                for i in range(0, 9, 3):
                    print(step[i:i+3])
                print()
            print("Total Cost:", cost)
            return

        if state in visited:
            continue
        visited.add(state)

        zero = state.index(0)
        row, col = divmod(zero, 3)

        for move in [-3, 3, -1, 1]:
            new = zero + move

            if not 0 <= new < 9:
                continue
            if move == -1 and col == 0:
                continue
            if move == 1 and col == 2:
                continue

            next_state = list(state)
            next_state[zero], next_state[new] = next_state[new], next_state[zero]
            next_state = tuple(next_state)

            if next_state not in visited:
                heappush(queue, (
                    cost + 1 + heuristic(next_state),
                    cost + 1,
                    next_state,
                    path + [state]
                ))

solve(start)
