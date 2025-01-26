import heapq

class EightPuzzle:
    def __init__(self, start_state, goal_state):
        """
        :param start_state: Initial state of the puzzle (3x3 list)
        :param goal_state: Goal state of the puzzle (3x3 list)
        """
        self.start_state = start_state
        self.goal_state = goal_state
        self.goal_position = self.get_positions(goal_state)

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
                    goal_x, goal_y = self.goal_position[tile]
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

    def a_star(self):
        """Solve the puzzle using A* algorithm."""
        open_list = []
        closed_set = set()

        # Initial state: (f, g, state, path)
        start = (self.manhattan_distance(self.start_state), 0, self.start_state, [])
        heapq.heappush(open_list, start)

        while open_list:
            # Pop state with the lowest f(n)
            _, g, current_state, path = heapq.heappop(open_list)
            closed_set.add(tuple(tuple(row) for row in current_state))

            # Goal test
            if current_state == self.goal_state:
                return path + [current_state]

            # Generate neighbors
            for neighbor in self.get_neighbors(current_state):
                neighbor_tuple = tuple(tuple(row) for row in neighbor)
                if neighbor_tuple not in closed_set:
                    new_g = g + 1
                    new_f = new_g + self.manhattan_distance(neighbor)
                    heapq.heappush(open_list, (new_f, new_g, neighbor, path + [current_state]))

        return None

    def display_board(self, state):
        """Display the 3x3 board."""
        for row in state:
            print(' '.join(str(cell) for cell in row))

    def run(self):
        """Run the A* algorithm to solve the puzzle."""
        print("Initial State:")
        self.display_board(self.start_state)

        solution = self.a_star()
        if solution:
            print("\nSolution:")
            for step, state in enumerate(solution):
                print(f"Step {step}:")
                self.display_board(state)
                print()
        else:
            print("No solution found.")


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

# Create an instance of the EightPuzzle class and solve it
puzzle = EightPuzzle(start_state, goal_state)
puzzle.run()