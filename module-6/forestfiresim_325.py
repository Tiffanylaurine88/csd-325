"""
forestfiresim_325.py

Forest Fire Sim, modified by Tiffany Davidson for CSD-325 Module 6.2
Original base file modified by Sue Sampson, based on a program by Al Sweigart.

Changes for Module 6:
- Added a WATER cell type that displays as blue and uses the '~' character.
- Added a centered lake created in createNewForest() using addLake().
- Lake cells act as a firebreak:
    * Fire does not spread into water.
    * Water cells never change once created.
"""

import random, sys, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Set up the constants:
WIDTH = 79
HEIGHT = 22

TREE = 'A'
FIRE = '@'
EMPTY = ' '
WATER = '~'  # New constant: water for the lake in the center

# (!) Try changing these settings to anything between 0.0 and 1.0:
INITIAL_TREE_DENSITY = 0.20  # Amount of forest that starts with trees.
GROW_CHANCE = 0.01  # Chance a blank space turns into a tree.
FIRE_CHANCE = 0.01  # Chance a tree is hit by lightning and burns.

# (!) Try setting the pause length to 1.0 or 0.0:
PAUSE_LENGTH = 0.5


def main():
    forest = createNewForest()
    bext.clear()

    while True:  # Main program loop.
        displayForest(forest)

        # Run a single simulation step:
        nextForest = {'width': forest['width'],
                      'height': forest['height']}

        for x in range(forest['width']):
            for y in range(forest['height']):
                # Do not modify water cells. They are a permanent firebreak.
                if forest[(x, y)] == WATER:
                    nextForest[(x, y)] = WATER
                    continue

                # If we've already set nextForest[(x, y)] on a
                # previous iteration, just do nothing here:
                if (x, y) in nextForest:
                    continue

                # Empty space may grow a tree:
                if ((forest[(x, y)] == EMPTY)
                    and (random.random() <= GROW_CHANCE)):
                    nextForest[(x, y)] = TREE

                # Tree may be hit by lightning:
                elif ((forest[(x, y)] == TREE)
                      and (random.random() <= FIRE_CHANCE)):
                    nextForest[(x, y)] = FIRE

                # Current tree is burning:
                elif forest[(x, y)] == FIRE:
                    # Loop through all the neighboring spaces:
                    for ix in range(-1, 2):
                        for iy in range(-1, 2):
                            neighbor = forest.get((x + ix, y + iy))

                            # Fire spreads only to neighboring trees,
                            # never into water or empty space.
                            if neighbor == TREE:
                                nextForest[(x + ix, y + iy)] = FIRE

                    # The tree has burned down now, so erase it:
                    nextForest[(x, y)] = EMPTY

                else:
                    # Just copy the existing object:
                    nextForest[(x, y)] = forest[(x, y)]

        forest = nextForest
        time.sleep(PAUSE_LENGTH)


def createNewForest():
    """Returns a dictionary for a new forest data structure."""
    forest = {'width': WIDTH, 'height': HEIGHT}

    # Start by filling the grid with trees and empty spaces:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if (random.random() * 100) <= INITIAL_TREE_DENSITY:
                forest[(x, y)] = TREE  # Start as a tree.
            else:
                forest[(x, y)] = EMPTY  # Start as an empty space.

    # After the base forest is created, carve out the lake.
    addLake(forest)

    return forest


def addLake(forest):
    """
    Add a lake roughly in the center of the display.

    The lake:
    - Uses WATER cells (character '~').
    - Is roughly centered.
    - Never changes during the simulation (handled in main()).
    - Acts as a firebreak because fire spreads only into TREE cells.
    """
    centerX = WIDTH // 2
    centerY = HEIGHT // 2

    # Size of the lake rectangle. You can tweak these to adjust size.
    halfLakeWidth = 7   # total width is about 15 cells
    halfLakeHeight = 3  # total height is about 7 cells

    minX = centerX - halfLakeWidth
    maxX = centerX + halfLakeWidth
    minY = centerY - halfLakeHeight
    maxY = centerY + halfLakeHeight

    for x in range(minX, maxX + 1):
        for y in range(minY, maxY + 1):
            # Make sure we stay in bounds.
            if 0 <= x < WIDTH and 0 <= y < HEIGHT:
                forest[(x, y)] = WATER


def displayForest(forest):
    """Display the forest data structure on the screen."""
    bext.goto(0, 0)
    for y in range(forest['height']):
        for x in range(forest['width']):
            cell = forest[(x, y)]
            if cell == TREE:
                bext.fg('green')
                print(TREE, end='')
            elif cell == FIRE:
                bext.fg('red')
                print(FIRE, end='')
            elif cell == WATER:
                bext.fg('blue')
                print(WATER, end='')
            elif cell == EMPTY:
                print(EMPTY, end='')
        print()
    bext.fg('reset')  # Use the default font color.
    print('Grow chance: {}%  '.format(GROW_CHANCE * 100), end='')
    print('Lightning chance: {}%  '.format(FIRE_CHANCE * 100), end='')
    print('Press Ctrl-C to quit.')


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.
