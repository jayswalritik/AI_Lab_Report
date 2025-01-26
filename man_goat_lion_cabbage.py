from collections import deque

class RiverCrossing:
    def __init__(self):
        # Define the initial and goal states
        self.initial_state = (0, 0, 0, 0)  # (man, goat, lion, cabbage) all on the starting side
        self.goal_state = (1, 1, 1, 1)  # All on the destination side

    def is_valid_state(self, state):
        # Check if the state is valid (no rule violation)
        man, goat, lion, cabbage = state
        # Goat and cabbage left alone -> goat eats cabbage
        if goat == cabbage != man:
            return False
        # Lion and goat left alone -> lion eats goat
        if lion == goat != man:
            return False
        return True

    def successors(self, state):
        # Generate all possible valid successor states
        man, goat, lion, cabbage = state
        succ = []

        # Man takes himself only
        new_state = (1 - man, goat, lion, cabbage)
        if self.is_valid_state(new_state):
            succ.append(new_state)

        # Man takes the goat
        if man == goat:
            new_state = (1 - man, 1 - goat, lion, cabbage)
            if self.is_valid_state(new_state):
                succ.append(new_state)

        # Man takes the lion
        if man == lion:
            new_state = (1 - man, goat, 1 - lion, cabbage)
            if self.is_valid_state(new_state):
                succ.append(new_state)

        # Man takes the cabbage
        if man == cabbage:
            new_state = (1 - man, goat, lion, 1 - cabbage)
            if self.is_valid_state(new_state):
                succ.append(new_state)

        return succ

    def bfs(self, initial_state, goal_state):
        # Use BFS to find the solution
        open_queue = deque([(initial_state, [initial_state])])  # Queue of states with paths
        visited = set()  # Set of visited states

        while open_queue:
            current_state, path = open_queue.popleft()
            visited.add(current_state)

            # Goal test
            if current_state == goal_state:
                return path

            # Generate successors
            for succ in self.successors(current_state):
                if succ not in visited:
                    open_queue.append((succ, path + [succ]))

        return None

    def run(self):
        # Solve the problem
        result = self.bfs(self.initial_state, self.goal_state)
        if result is None:
            print("No solution found!")
        else:
            print("Solution found! Steps:")
            for step in result:
                print(step)


# Create an instance of the RiverCrossing class and run it
river_crossing = RiverCrossing()
river_crossing.run()