class WaterJugDFS:
    def __init__(self, initial_state=(0, 0), goal_state=(2, 0)):
        # Define the initial and goal states
        self.initial_state = initial_state
        self.goal_state = goal_state

    def successors(self, state):
        X, Y = state
        succ = []

        # Action 1: Fill Jug X
        if X < 4:
            succ.append((4, Y))

        # Action 2: Fill Jug Y
        if Y < 3:
            succ.append((X, 3))

        # Action 3: Empty Jug X
        if X > 0:
            succ.append((0, Y))

        # Action 4: Empty Jug Y
        if Y > 0:
            succ.append((X, 0))

        # Action 5: Pour from X to Y
        if X > 0 and Y < 3:
            transfer = min(X, 3 - Y)
            succ.append((X - transfer, Y + transfer))

        # Action 6: Pour from Y to X
        if Y > 0 and X < 4:
            transfer = min(Y, 4 - X)
            succ.append((X + transfer, Y - transfer))

        return succ

    def dfs(self, initial_state, goal_state):
        stack = [(initial_state, [initial_state])]  # Stack of states with paths
        visited = set()  # Set of visited states

        while stack:
            # Step 1: Pop from STACK
            current_state, path = stack.pop()
            visited.add(current_state)

            # Step 2: Goal test
            if current_state == goal_state:
                # Goal found; return the path
                return path

            # Step 3: Generate successors
            for succ in self.successors(current_state):
                if succ not in visited and all(succ not in p[0] for p in stack):
                    stack.append((succ, path + [succ]))

        return None

    def run(self):
        # Run DFS to find the solution
        result = self.dfs(self.initial_state, self.goal_state)
        if result is None:
            print("Goal not found")
        else:
            print("Goal found! Path:")
            for state in result:
                print(state)


# Create an instance of the WaterJugDFS class and run it
sol_dfs = WaterJugDFS()
sol_dfs.run()
