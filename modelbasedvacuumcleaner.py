import random

class ModelBasedRoomCleanerAgent:
    def __init__(self, room_size=(10, 10)):
        self.room_size = room_size
        # Initialize the room as a 10x10 grid with random 0 (clean) and 1 (dirty) cells
        self.grid = [[random.choice([0, 1]) for _ in range(room_size[1])] for _ in range(room_size[0])]
        # Initialize the agent's position randomly
        self.current_position = (random.randint(0, room_size[0] - 1), random.randint(0, room_size[1] - 1))
        # Initialize a model of the environment to track visited cells
        self.visited = [[False for _ in range(room_size[1])] for _ in range(room_size[0])]

    def display_room(self):
        # Display the current status of the room grid
        for row in self.grid:
            print(" ".join("C" if cell == 0 else "D" for cell in row))
        print("\n")

    def perceive(self):
        # Perceive the cleanliness of the current cell
        x, y = self.current_position
        return self.grid[x][y]

    def act(self):
        # Perform action based on the perception (clean the cell if dirty)
        x, y = self.current_position
        if self.perceive() == 1:  # If the current cell is dirty (1)
            print(f"Cell ({x}, {y}) is Dirty. Cleaning...")
            self.grid[x][y] = 0  # Clean the cell (set to 0)
            print(f"Cell ({x}, {y}) is now Clean.")
        else:
            print(f"Cell ({x}, {y}) is already Clean.")

        # Update the model to mark the cell as visited
        self.visited[x][y] = True

    def move(self):
        # Use the model to find the nearest unvisited dirty cell
        x, y = self.current_position
        for i in range(self.room_size[0]):
            for j in range(self.room_size[1]):
                if self.grid[i][j] == 1 and not self.visited[i][j]:
                    self.current_position = (i, j)
                    return
        # If no unvisited dirty cells are found, stop moving
        self.current_position = None

    def is_room_clean(self):
        # Check if the entire room is clean
        return all(cell == 0 for row in self.grid for cell in row)

    def run(self):
        # Display initial status of the room
        print("Initial Room Status:")
        self.display_room()

        steps = 0
        while not self.is_room_clean():
            print(f"\nStep {steps + 1}:")
            self.act()
            self.move()
            steps += 1
            if self.current_position is None:
                print("No more dirty cells detected. Stopping.")
                break

        # Display final status of the room
        print("\nFinal Room Status:")
        self.display_room()
        print(f"Room cleaned in {steps} steps.")

# Create and run the Model-Based Room Cleaner Agent
agent = ModelBasedRoomCleanerAgent()
agent.run()