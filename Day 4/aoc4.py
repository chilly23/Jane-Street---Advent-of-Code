# --- Day 4: Printing Department ---
# You ride the escalator down to the printing department. They're clearly getting ready for Christmas; they have lots of large rolls of paper everywhere, and there's even a massive printer in the corner (to handle the really big print jobs).

# Decorating here will be easy: they can make their own decorations. What you really need is a way to get further into the North Pole base while the elevators are offline.

# "Actually, maybe we can help with that," one of the Elves replies when you ask for help. "We're pretty sure there's a cafeteria on the other side of the back wall. If we could break through the wall, you'd be able to keep moving. It's too bad all of our forklifts are so busy moving those big rolls of paper around."

# If you can optimize the work the forklifts are doing, maybe they would have time to spare to break through the wall.

# The rolls of paper (@) are arranged on a large grid; the Elves even have a helpful diagram (your puzzle input) indicating where everything is located.

# For example:

# ..@@.@@@@.
# @@@.@.@.@@
# @@@@@.@.@@
# @.@@@@..@.
# @@.@@@@.@@
# .@@@@@@@.@
# .@.@.@.@@@
# @.@@@.@@@@
# .@@@@@@@@.
# @.@.@@@.@.
# The forklifts can only access a roll of paper if there are fewer than four rolls of paper in the eight adjacent positions. If you can figure out which rolls of paper the forklifts can access, they'll spend less time looking and more time breaking down the wall to the cafeteria.

# In this example, there are 13 rolls of paper that can be accessed by a forklift (marked with x):

# ..xx.xx@x.
# x@@.@.@.@@
# @@@@@.x.@@
# @.@@@@..@.
# x@.@@@@.@x
# # .@@@@@@@.@
# .@.@.@.@@@
# x.@@@.@@@@
# .@@@@@@@@.
# x.x.@@@.x.
# Consider your complete diagram of the paper roll locations. How many rolls of paper can be accessed by a forklift?

# import numpy as np

# def part1(f):
#     lines = [line.rstrip('\n') for line in f]

#     w = len(lines[0])
#     if not all(len(line) == w for line in lines):
#         raise ValueError("Input grid is ragged (rows have different lengths)")

#     grid = np.array([list(line) for line in lines])
#     is_at = (grid == '@').astype(int)
#     p = np.pad(is_at, 1)
#     neighbors = (
#         p[:-2, :-2] + p[:-2, 1:-1] + p[:-2, 2:] +
#         p[1:-1, :-2] +                 p[1:-1, 2:] +
#         p[2:, :-2]  + p[2:, 1:-1]  + p[2:, 2:]
#     )
#     return np.sum((is_at == 1) & (neighbors < 4))


# if __name__ == "__main__":
#     with open("input4.txt") as f:
#         print(part1(f))

import numpy as np

def part2(puzzle_input):
    grid = np.array(
        [[c == '@' for c in line] for line in puzzle_input.splitlines()],
        dtype=np.uint8
    )

    def is_removable(grid):
        p = np.pad(grid, 1)
        neighbors = (
            p[:-2, :-2] + p[:-2, 1:-1] + p[:-2, 2:] +
            p[1:-1, :-2] +             p[1:-1, 2:] +
            p[2:, :-2]  + p[2:, 1:-1]  + p[2:, 2:]
        )
        return grid & (neighbors < 4)

    removed = 0
    rem = is_removable(grid)
    while rem.any():
        grid -= rem
        removed += rem.sum()
        rem = is_removable(grid)

    return int(removed)


if __name__ == "__main__":
    with open("input4.txt") as f:
        puzzle_input = f.read()

    print(part2(puzzle_input))
