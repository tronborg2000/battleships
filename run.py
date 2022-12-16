import random 

#make the 5x5 grid
grid = [[' ' for _ in range(5)] for _ in range (5)]

#main game loop

while True:
  # Place a battleship at a random position
  x = random.randint(0, 4)
  y = random.randint(0, 4)
  grid[x][y] = 'B'

  # Print the grid
  for row in grid:
    print(' '.join(row))
  print()

  # Get the player's guess
  x = int(input("Enter the x coordinate of your guess: "))
  y = int(input("Enter the y coordinate of your guess: "))


  # Check if the guess is a hit or a miss
  if grid[x][y] == 'B':
    print("Hit!")
    grid[x][y] = 'X'
  else:
    print("Miss.")

  # Check if the player has won
  if not any('B' in row for row in grid):
    print("You won!")
break
