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

cost = [2, 1, 20] # cost has 3 values, corresponding to making 
                  # a right turn, no turn, and a left turn
#cost = [1, 1, 1]
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

    def is_move_forbidden(direction, move):
        if ((direction == 0 and move == 2) 
            or (direction == 1 and move == 3) 
            or (direction == 2 and move == 0) 
            or (direction == 3 and move == 1)):
            return True
        else:
            return False

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


    action = [[' ' for col in range(len(grid[0]))] for row in range(len(grid))]

    g, x, y = -1, -1, -1
    moves = [[0, *init, ' ']]

    while (x != goal[0] or y != goal[1]) and len(moves) != 0:
        moves.sort(reverse = True)
        g, temp_x, temp_y, dir, action_sym = moves.pop()
        moves = []

        action[x][y] = action_sym
        x, y = temp_x, temp_y
        #print("Evaluating move {} {} in direction {}, with cost {}".format(x, y, dir, g))
        for i in range(len(forward)):
            x2 = x + forward[i][0]
            y2 = y + forward[i][1]
            if (x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and grid[x2][y2] != 1
                and not is_move_forbidden(dir, i)):
                next_action = get_next_action(dir, i)
                new_value = g + cost[next_action] + (abs(goal[0] - x2) + abs(goal[1] - y2))
                g2 = new_value
                moves.append([g2, x2, y2, get_new_direction(dir, get_next_action(dir, i)), action_name[next_action]])

    action[goal[0]][goal[1]] = "#"
    return action

act = optimum_policy2D(grid, init, goal, cost)

for line in act:
    print(line)