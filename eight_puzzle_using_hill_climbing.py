
class EightPuzzleHillClimbing:
    def __init__(self, start_state, goal_state):
        """
        :param start_state: Initial state of the puzzle (3x3 list)
        :param goal_state: Goal state of the puzzle (3x3 list)
        """
        self.start_state = start_state
        self.goal_state = goal_state
        self.goal_positions = self.get_positions(goal_state)

    def get_positions(self, state):
        """Map each tile to its position for quick lookup."""
        positions = {}
        for i in range(3):
            for j in range(3):
                positions[state[i][j]] = (i, j)
        return positions

    def manhattan_distance(self, state):
        """Calculate Manhattan Distance heuristic."""
        distance = 0
        for i in range(3):
            for j in range(3):
                tile = state[i][j]
                if tile != 0:  # Skip the blank tile
                    goal_x, goal_y = self.goal_positions[tile]
                    distance += abs(i - goal_x) + abs(j - goal_y)
        return distance

    def get_neighbors(self, state):
        """Generate all valid neighbor states."""
        neighbors = []
        # Find the blank tile (0)
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    x, y = i, j

        # Define moves: (dx, dy)
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                # Create a new state by swapping blank tile with the neighbor
                new_state = [row[:] for row in state]
                new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
                neighbors.append(new_state)
        return neighbors

    def steepest_ascent_hill_climbing(self):
        """Solve the puzzle using steepest ascent hill climbing."""
        current_state = self.start_state
        current_heuristic = self.manhattan_distance(current_state)
        steps = [current_state]

        while True:
            # Generate neighbors and calculate their heuristic values
            neighbors = self.get_neighbors(current_state)
            neighbor_heuristics = [(self.manhattan_distance(neighbor), neighbor) for neighbor in neighbors]

            # Find the neighbor with the lowest heuristic
            best_neighbor_heuristic, best_neighbor = min(neighbor_heuristics, key=lambda x: x[0])

            # If no better neighbor exists, stop (local maximum or goal state)
            if best_neighbor_heuristic >= current_heuristic:
                break

            # Move to the best neighbor
            current_state = best_neighbor
            current_heuristic = best_neighbor_heuristic
            steps.append(current_state)

            # If the goal state is reached, stop
            if current_heuristic == 0:
                break

        return steps

    def display_board(self, state):
        """Display the 3x3 board."""
        for row in state:
            print(' '.join(str(cell) for cell in row))

    def run(self):
        """Run the steepest ascent hill climbing algorithm to solve the puzzle."""
        print("Initial State:")
        self.display_board(self.start_state)
        print()

        solution_steps = self.steepest_ascent_hill_climbing()
        print("\nSolution Steps:")
        for step, state in enumerate(solution_steps):
            print(f"Step {step}:")
            self.display_board(state)
            print()

        if solution_steps[-1] == self.goal_state:
            print("Goal state reached!")
        else:
            print("Local maximum reached, but goal state not found.")


# Define start and goal states
start_state = [
    [1, 2, 3],
    [0, 4, 6],
    [7, 5, 8]
]

goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Create an instance of the EightPuzzleHillClimbing class and solve it
puzzle = EightPuzzleHillClimbing(start_state, goal_state)
puzzle.run()
