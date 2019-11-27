#########################################################################
# Imports
#########################################################################
import random
import importlib

#########################################################################
# Functions provided, you don't have to touch these.
#########################################################################

def updateScore(score):
    """Increments the score by one (you don't need to change this)"""
    return score + 1

def prettyPrint(cubes, player, score, gridSize=5):
    """Prints the board state (you don't need to change this)"""
    assert(0 <= player[0] < gridSize)
    assert(player[1] == gridSize - 1)
    square = u" \u25A0 "
    triangle = u" \u25B2 "
    space = "   "
    toRet = "\n+" + "---+"*gridSize + "\n"
    for y in range(gridSize):
        toRet += "|" + "|".join([triangle if [x,y] == player else (space if [x,y] not in cubes else square) for x in
            range(gridSize)]) + "|\n"
        toRet += "+" + "---+"*gridSize + "\n"
    print(toRet)

def reload():
    """Don't change this!  This lets you reload your file by typing `reload()`"""
    import cubegame
    importlib.reload(cubegame)
    exec("from cubegame import *")

def updateCubes(cubes):
    """ 
    input: list of cubes 
    output: the updated list of cubes 
    """
    for i in cubes:
        i[1] += 1
    new = random.sample(range(5),3)
    for i in new:
        cubes.append([i,0])
    return cubes

def updatePlayerLocation(player, direction):
    """ 
    input: player location & direction to move 
    output: updated player location 
    """
    if direction == "left":
        if player[0] == 0:
            print("Invalid move! You just lost your turn")
        else:
            player[0] -= 1
    elif direction == "right":
        if player[0] == 4:
            print("Invalid move! You just lost your turn")
        else:
            player[0] += 1
    elif direction == "stay":
        pass
    return player

def collision(cubes, player):
    """ Take as input the list of cube locations and the player location.
        Return True if there is a collision between the player and a cube, False otherwise.
    """
    if player in cubes:
        return True
    else:
        return False

def runGame():
    """Contains the main loop for running the game"""
    # Game state
    player = [2,4]                # initial location of the player
    score = 0                     # initial score
    cubes = [[0,0], [3,0], [4,0]] # initial cube locations

    print("Welcome to cubes!  Quit by typing 'quit'")
    prettyPrint(cubes, player, score)

    # Main loop
    while True:
        direction = raw_input("Input 'left', 'right', 'stay', or 'quit': ")
        if direction=='quit':
            print("You quit!  Score was", score)
            break
        if direction !='left' and direction != 'right' and direction != 'stay':
            continue
        player = updatePlayerLocation(player, direction)
        cubes = updateCubes(cubes)
        score = updateScore(score)
        print(player)
        prettyPrint(cubes, player, score)

        if collision(cubes, player):
            print("You lose!  Score was", score)
            break
    
runGame()