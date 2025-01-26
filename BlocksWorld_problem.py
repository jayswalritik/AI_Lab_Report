class BlocksWorld:
    def __init__(self, start_state, goal_state):
        self.start_state = start_state  # Current state of blocks
        self.goal_state = goal_state    # Goal state of blocks

    def calculate_heuristic(self, state):
        """Calculate heuristic value e(p) for a given state."""
        heuristic_value = 0
        for i in range(len(state)):
            # Compare each block with the corresponding block in the goal state
            if state[i] == self.goal_state[i]:
                heuristic_value += 1  # Correct support structure
            else:
                heuristic_value -= 1  # Wrong support structure
        return heuristic_value

    def run(self):
        """Run heuristic calculation for the start state."""
        start_heuristic = self.calculate_heuristic(self.start_state)
        goal_heuristic = self.calculate_heuristic(self.goal_state)
        print(f"Start State: {self.start_state}, Heuristic Value: {start_heuristic}")
        print(f"Goal State: {self.goal_state}, Heuristic Value: {goal_heuristic}")


# Define the start and goal states
start_state = ["A", "D", "C", "B"]  # Top to bottom
goal_state = ["D", "C", "B", "A"]   # Top to bottom

# Create an instance of the BlocksWorld class
blocks_world = BlocksWorld(start_state, goal_state)

# Run the heuristic calculation
blocks_world.run()
