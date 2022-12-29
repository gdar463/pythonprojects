# I don't have the input for this
#
# Forgot to save it ;)
import lib
import random

BOARD_SIZE = 10

# Represents a player's board
class Board:
    def __init__(self):
        # Initialize empty board
        self.grid = [[' ' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        # Initialize empty list of ships
        self.ships = []

    def place_ship(self, length):
        # Generate random ship position and orientation
        row = random.randint(0, BOARD_SIZE - 1)
        col = random.randint(0, BOARD_SIZE - 1)
        orientation = random.choice(['horizontal', 'vertical'])

        # Check if there is enough space for the ship
        if orientation == 'horizontal':
            if col + length > BOARD_SIZE:
                return False
        elif orientation == 'vertical':
            if row + length > BOARD_SIZE:
                return False

        # Place the ship on the board
        for i in range(length):
            if orientation == 'horizontal':
                self.grid[row][col + i] = 'S'
            elif orientation == 'vertical':
                self.grid[row + i][col] = 'S'

    # Add ship to list of ships
        self.ships.append((row, col, length, orientation))
        return True

    def attack(self, row, col):
        # Check if the attack hit a ship
        for ship in self.ships:
            r, c, length, orientation = ship
            if orientation == 'horizontal':
                if r == row and c <= col < c + length:
                    self.grid[row][col] = 'H'
                    return True
                elif orientation == 'vertical':
                    if c == col and r <= row < r + length:
                        self.grid[row][col] = 'H'
                    return True
        self.grid[row][col] = 'M'
        return False

    def all_sunk(self):
    # Check if all ships have been sunk
        for ship in self.ships:
            r, c, length, orientation = ship
            for i in range(length):
                if orientation == 'horizontal':
                    if self.grid[r][c + i] != 'H':
                        return False
                elif orientation == 'vertical':
                    if self.grid[r + i][c] != 'H':
                        return False
        return True

# Represents a player in the game
class Player:
    def __init__(self, name):
        self.name = name
        self.board = Board()

    def attack(self, row, col):
        return self.board.attack(row, col)

# Start a new game
def start_game():
    # Create two players
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    # Place ships for each player
    for player in (player1, player2):
        for length in (5, 4, 3, 3, 2):
            placed = False
            while not placed:
                placed = player.board.place_ship(length)

    # Game loop
    current_player = player1
    other_player = player2
    while True:
        # Print board for current player
        print(f"Your board:")
        print_board(current_player.board.grid)

        # Get attack coordinates from player
        row = int(input("Enter row to attack: "))
        col = int(input("Enter col to attack: "))

        # Attack and check if the attack was a hit
        hit = other_player.attack(row + 1, col + 1)
        lib.clearconsole()
        if hit:
            print("Hit!")
        else:
            print("Miss!")
        
        input()

        # Check if all ships have been sunk
        if other_player.board.all_sunk():
            print(f"{other_player.name} has lost the game!")
            break

        # Switch players
        if current_player == player1:
            current_player = player2
            other_player = player1
        else:
            current_player = player1
            other_player = player2

# Print the board to the console
def print_board(board):
    print("  " + " ".join([str(i + 1) for i in range(BOARD_SIZE)]))
    for i, row in enumerate(board):
        print(i + 1, " ".join(row))

# Start the game
start_game()
