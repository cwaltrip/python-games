# Dungeon Escape

# Originally written for the Coursera/Rice University course
# 'An Introduction to Interactive Programming in Python (Part 1)'

import random

# Define 2d list that holds the dungeon
CELLS = [(0, 0), (0, 1), (0, 2),
         (1, 0), (1, 1), (1, 2),
         (2, 0), (2, 1), (2, 2)]

# Randomize start locations for player, monster, door
def get_locations():
  monster = random.choice(CELLS)
  door = random.choice(CELLS)
  start = random.choice(CELLS)
  if monster == door or monster == start or door == start:
    return get_locations()  
  return monster, door, start

# Translate player move to 2d position change  
def move_player(player, move):
  # Get the player's current location
  x, y = player
  if move == 'LEFT':
    y -= 1
  if move == 'RIGHT':
    y += 1
  if move == 'UP':
    x -= 1
  if move == 'DOWN':
    x += 1
  return x, y

# Get legal moves from current position
def get_available_moves(player):
  available_moves = ['UP', 'DOWN', 'LEFT', 'RIGHT']
  if player[0] == 0:
    available_moves.remove('UP')
  if player[0] == 2:
    available_moves.remove('DOWN')
  if player[1] == 0:
    available_moves.remove('LEFT')
  if player[1] == 2:
    available_moves.remove('RIGHT')
  return available_moves

# Draw the dungeon 'map' 
def draw_map(player):
  print(' _ _ _')
  tile = '|{}'
  for idx, cell in enumerate(CELLS):
    if idx in [0, 1, 3, 4, 6, 7]:
      if cell == player:
        print(tile.format('X'), end = '')
      else:
        print(tile.format('_'), end = '')
    else:
      if cell == player:
        print(tile.format('X|'))
      else:
        print(tile.format('_|'))
  print('')

# Start game
monster, door, player = get_locations()
print("Welcome to the dungeon!")

# Main game loop
while True:
  moves = get_available_moves(player)
  print("\nYou're currently in room {}:".format(player))
  draw_map(player)
  print("You can move {}".format(moves))
  print("Enter QUIT to quit")
  move = input("> ").upper()
  if move == 'QUIT':
    break
  if move in moves:
    player = move_player(player, move)
  else:
    print("*BONK* Walls are hard, stop walking into them!")
    continue
  if player == door:
    print("You find the door and escape the dungeon! You win.")
    break
  elif player == monster:
    print("You are eaten by a grue! You lose.")
    break
  else:
    print("You take a careful step...")
    continue
