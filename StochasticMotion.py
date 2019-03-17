# --------------
# USER INSTRUCTIONS
#
# Write a function called stochastic_value that 
# returns two grids. The first grid, value, should 
# contain the computed value of each cell as shown 
# in the video. The second grid, policy, should 
# contain the optimum policy for each cell.


delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>'] # Use these when creating your policy grid.

# ---------------------------------------------
#  Modify the function stochastic_value below
# ---------------------------------------------

def stochastic_value(grid,goal,cost_step,collision_cost,success_prob):

    def cost_function(x, y, action_no, value_grid):
        steps = [(action_no + 1) % 4, action_no, action_no - 1]
        # left, up, right
        result = cost_step
        for step in steps:
            step_x = x + delta[step][0]
            step_y = y + delta[step][1]
            if (step_x < 0 or step_x >= len(grid) or step_y < 0 or step_y >= len(grid[0]) or grid[step_x][step_y] == 1):
                result += (failure_prob * collision_cost)
            else:
                if step == action_no:
                    result += (success_prob * value_grid[step_x][step_y])
                else:
                    result += (failure_prob * value_grid[step_x][step_y])
        return result

    failure_prob = (1.0 - success_prob)/2.0 # Probability(stepping left) = prob(stepping right) = failure_prob
    value = [[collision_cost for col in range(len(grid[0]))] for row in range(len(grid))]
    policy = [[' ' for col in range(len(grid[0]))] for row in range(len(grid))]
    policy[goal[0]][goal[1]] = '*'
    value[goal[0]][goal[1]] = 0
    change_occured = True

    while change_occured:
        change_occured = False
    
        for x in range(len(grid)):
            for y in range(len(grid[0]) - 1, -1, -1):
                if (x != goal[0] or y != goal[1]) and grid[x][y] != 1:
                    for i in range(len(delta)):
                        next_x = x + delta[i][0]
                        next_y = y + delta[i][1]
                        if (next_x >= 0 and next_x < len(grid) and next_y >= 0 and next_y < len(grid[0]) and grid[next_x][next_y] != 1):
                                cost = cost_function(x, y, i, value)
                                if cost < value[x][y]:
                                    value[x][y] = cost
                                    policy[x][y] = delta_name[i]
                                    change_occured = True
    return value, policy

# ---------------------------------------------
#  Use the code below to test your solution
# ---------------------------------------------

grid = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 1, 1, 0]]
# grid = [[0, 0, 0],
#         [0, 0, 0]]
goal = [0, len(grid[0])-1] # Goal is in top right corner
cost_step = 1
collision_cost = 1000
# collision_cost = 100
success_prob = 0.5

value,policy = stochastic_value(grid,goal,cost_step,collision_cost,success_prob)
for row in value:
    print(row)
for row in policy:
    print(row)

# Expected outputs:
#
#[471.9397246855924, 274.85364957758316, 161.5599867065471, 0],
#[334.05159958720344, 230.9574434590965, 183.69314862430264, 176.69517762501977], 
#[398.3517867450282, 277.5898270101976, 246.09263437756917, 335.3944132514738], 
#[700.1758933725141, 1000, 1000, 668.697206625737]


#
# ['>', 'v', 'v', '*']
# ['>', '>', '^', '<']
# ['>', '^', '^', '<']
# ['^', ' ', ' ', '^']