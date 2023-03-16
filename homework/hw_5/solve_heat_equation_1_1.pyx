import numpy as np
from itertools import product
import matplotlib.pyplot as plt

def build_grid(n):
    '''defines the grid'''
    G = np.zeros((n, n))
    return G

def set_boundary_grid(G):
    '''set the boundary values'''
    n = G.shape[0]
    G[:,  0] = 1.0
    G[0,  :] = 1.0
    G[-1, :] = 1.0
    G[:, -1] = 1.0

def plot_grid(G):
    img = plt.imshow(G)
    img.set_cmap('rainbow')
    plt.axis('off')
    plt.show()

# using iterators to traverse the grid
def iteration_gen(G):
    n = G.shape[0]
    indices = product(range(1, n-1), repeat=2)
    for e in indices:
        G[e]=(G[e[0] + 1, e[1]] + G[e[0] - 1, e[1]] + G[e[0], e[1] + 1] + G[e[0], e[1] - 1])/4
    

# using numpy built-in functions to compute the error
def calc_error_np(G1, G2):
    error = np.square(np.subtract(G1, G2)).mean()
    return(error)

# deep copy of G1 to G2
def copy_array(G1, G2):
    G2[:, :] = G1[:, :]

    

def iteration_gen_nonhomogeneous(G):
    """the iteration function in hw05"""
    n = G.shape[0]
    indices = product(range(1, n-1), repeat=2)
    for e in indices:
        current_indecies=np.array( [[e[0] + 1, e[1]],   [e[0] - 1, e[1]], [e[0], e[1] + 1], [e[0], e[1] - 1]])
        current_indecies=np.exp(-1*abs(current_indecies[:,0]-current_indecies[:,1])/np.sqrt(n))
        G[e]=np.dot(np.array([G[e[0] + 1, e[1]], G[e[0] - 1, e[1]], G[e[0], e[1] + 1] ,G[e[0], e[1] - 1]]) , current_indecies) / np.sum(current_indecies)


        
def solve_heat_nonhomogenous_equation4(n):
    '''changing to both calc_error_np and iteration_gen functions'''
    G = build_grid(n)
    set_boundary_grid(G)
    
    G_prev = build_grid(n)
    copy_array(G, G_prev)
    
    error = np.float("inf")
    while error > 1e-7:
        iteration_gen_nonhomogeneous(G)
        error = calc_error_np(G, G_prev) 
        copy_array(G, G_prev)          
    return(G)