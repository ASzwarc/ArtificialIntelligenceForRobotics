forward = [[-1,  0], # go up
           [ 0, -1], # go left
           [ 1,  0], # go down
           [ 0,  1]] # go right
forward_name = ['up', 'left', 'down', 'right']

# action has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']

# EXAMPLE INPUTS:
# grid format:
#     0 = navigable space
#     1 = unnavigable space 
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]

init = [4, 3, 0] # given in the form [row,col,direction]
                 # direction = 0: up
                 #             1: left
                 #             2: down
                 #             3: right
                
goal = [2, 0] # given in the form [row,col]

#cost = 1
cost = [2, 1, 20] # cost has 3 values, corresponding to making 
                  # a right turn, no turn, and a left turn

delta_name = ['^', '<', 'v', '>']

# EXAMPLE OUTPUT:
# calling optimum_policy2D with the given parameters should return 
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
# ----------

# ----------------------------------------
# modify code below
# ----------------------------------------

def optimum_policy2D(grid,init,goal,cost):

    def get_next_action(direction, move):
        if direction == move:
            return 1 #no turn
        else:
            if direction == 0: #up
                if move  == 1:
                    return 2
                elif move == 3:
                    return 0
            elif direction == 1: #left
                if move == 0: #up
                    return 0
                elif move == 2: #down
                    return 2
            elif direction == 2: #down
                if move == 1:
                    return 0
                elif move == 3:
                    return 2
            else: #right
                if move == 0:
                    return 2
                elif move == 2:
                    return 0
    
    def get_new_direction(direction, action):
        if action == 1: #no turn
            return direction
        elif direction == 0 and action == 0:
            return 3
        elif direction == 0 and action == 2:
            return 1
        elif direction == 1 and action == 0:
            return 0
        elif direction == 1 and action == 2:
            return 2
        elif direction == 2 and action == 0:
            return 1
        elif direction == 2 and action == 2:
            return 3
        elif direction == 3 and action == 0:
            return 2
        elif direction == 3 and action == 2:
            return 0

    value = [[99 for col in range(len(grid[0]))] for row in range(len(grid))]
    moves = [[0, goal[0], goal[1], "*"]]
    policy = [[' ' for col in range(len(grid[0]))] for row in range(len(grid))]
    while len(moves) != 0 :

        moves.sort()
        moves.reverse()
        val, x, y, mark = moves.pop()
        value[x][y] = val
        policy[x][y] = mark

        for action_no in range(len(forward)):
            next_x = x - forward[action_no][0]
            next_y = y - forward[action_no][1]
            if (next_x >= 0 and next_x < len(grid) and next_y >= 0 and next_y < len(grid[0]) 
                and grid[next_x][next_y] != 1):
                #evaluate cost of movement
                    moves.append([value[x][y] + cost, next_x, next_y, delta_name[action_no]])

    return value, policy

val, act = optimum_policy2D(grid, init, goal, cost)
for line in val:
    print(line)

for line in act:
    print(line)