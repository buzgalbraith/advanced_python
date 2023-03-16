import cython
from cython.cimports.dishes import spamdish, sausage

@cython.cfunc
def prepare(d: cython.pointer(spamdish)) -> cython.void:
    d.oz_of_spam = 42
    d.filler = sausage

def serve():
    d: spamdish
    prepare(cython.address(d))
    print(f'{d.oz_of_spam} oz spam, filler no. {d.filler}')
# import cython
# from itertools import product
# import numpy as np
# import matplotlib.pyplot as plt
# from cython.cimports.dishes import spamdish, sausage
# #from cython.cimports.module import  numpy as np # need to import special compile-time information

# def iteration_gen_nonhomogeneous(G):
#     """the iteration function in hw05"""
#     n:cython.int = G.shape[0]
#     indices = product(range(1, n-1), repeat=2)
#     current_indecies:np.ndarray=np.ndarray(shape=(4,2), dtype=int)
#     out_indecies:np.ndarray=np.ndarray(shape=(4,1))
#     for e in indices:
#         current_indecies[0]=[e[0] + 1, e[1]]
#         current_indecies[1]=[e[0] - 1, e[1]]
#         current_indecies[2]= [e[0], e[1] + 1] 
#         current_indecies[3]=[e[0], e[1] - 1]
#         #print(np.exp(-1*abs(current_indecies[:,0]-current_indecies[:,1])/np.sqrt(n)))
#         out_indecies=np.exp(-1*abs(current_indecies[:,0]-current_indecies[:,1])/np.sqrt(n))
#         G[e]=np.dot(np.array([G[e[0] + 1, e[1]], G[e[0] - 1, e[1]], G[e[0], e[1] + 1] ,G[e[0], e[1] - 1]]) , out_indecies) / np.sum(out_indecies)


# def build_grid(n):
#     '''defines the grid'''
#     G:np.ndarray = np.zeros((n, n))
#     return G

# def set_boundary_grid(G):
#     '''set the boundary values'''
#     n:cython.int = G.shape[0]
#     G[:,  0] = 1.0
#     G[0,  :] = 1.0
#     G[-1, :] = 1.0
#     G[:, -1] = 1.0

# def plot_grid(G):
#     img = plt.imshow(G)
#     img.set_cmap('rainbow')
#     plt.axis('off')
#     plt.show()


# # using numpy built-in functions to compute the error
# def calc_error_np(G1, G2):
#     error:cython.int = np.square(np.subtract(G1, G2)).mean()
#     return(error)

# # deep copy of G1 to G2
# def copy_array(G1, G2):
#     G2[:, :] = G1[:, :]

    
# def solve_heat_nonhomogeneous_equation4(n):
#     '''changing to both calc_error_np and iteration_gen functions'''
#     np.ndarray: G = build_grid(n)
#     set_boundary_grid(G)
#     G_prev: np.ndarray  = build_grid(n)
#     copy_array(G, G_prev)
    
#     error:cython.int = np.float("inf")
#     while error > 1e-7:
#         iteration_gen_nonhomogeneous(G)
#         error = calc_error_np(G, G_prev) 
#         copy_array(G, G_prev)          
#     return(G)