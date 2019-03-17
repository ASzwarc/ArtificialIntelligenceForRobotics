# ----------
# User Instructions:
# 
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal. 
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]

goal = [len(grid)-1, len(grid[0])-1]
cost = 1 # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def compute_value(grid,goal,cost):
    value = [[99 for col in range(len(grid[0]))] for row in range(len(grid))]
    moves = [[0, goal[0], goal[1], "*"]]
    policy = [[' ' for col in range(len(grid[0]))] for row in range(len(grid))]
    while len(moves) != 0 :

        moves.sort()
        moves.reverse()
        val, x, y, mark = moves.pop()
        value[x][y] = val
        policy[x][y] = mark

        for action_no in range(len(delta)):
            next_x = x - delta[action_no][0]
            next_y = y - delta[action_no][1]
            if (next_x >= 0 and next_x < len(grid) and next_y >= 0 and next_y < len(grid[0]) 
                and value[next_x][next_y] == 99 and grid[next_x][next_y] != 1):
                    moves.append([value[x][y] + cost, next_x, next_y, delta_name[action_no]])

    return value, policy

val, act = compute_value(grid, goal, cost)
for line in val:
    print(line)

for line in act:
    print(line)