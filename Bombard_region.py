import numpy as np

# Example map
grid = np.array([
    [1,0,0,0,1],
    [1,0,1,1,1],
    [1,1,0,1,1],
    [1,0,1,1,0],
    [0,1,0,1,1]
])

n = grid.shape[0]   # size of grid
m = 3               # blast size (odd number)


#Doubt 