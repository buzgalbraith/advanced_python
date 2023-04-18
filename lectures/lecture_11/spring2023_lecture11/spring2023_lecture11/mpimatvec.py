
from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

n = size * 2  
m = 5
if rank == 0:
    A = np.random.randn(n, m) ## n by m random numbers
    x = np.random.randn(m) ## x is m 

    ytarget = A.dot(x) # to check the result, the ground truth. 
    
    A = A.reshape(size, -1, m) ## reshape a into the matrix
else: 
    A = None ## does not overwirte A 
    x = np.zeros(m) ## sets x to a zero vector

Asmall = np.zeros((n // size, m)) ## a smaller version of

# Asmall = comm.scatter(A, root=0)
comm.Scatter(A, Asmall, root=0) ## we are scattering A so that each process gets a bit of A. dont have to tell how to send out the data i
# it will do that on it's own.  need to specfiy the ugger and the hroot tho 

# x = comm.bcast(x, root=0)
comm.Bcast(x, root=0) ## braodcast x becuase it is same for everyone 

print('rank', rank, ':', Asmall.shape, x.shape)

ysmall = Asmall.dot(x) ## a smal y

# y = comm.gather(ysmall, root=0)
y = np.zeros((size, n // size)) ## intilize y
comm.Gather(ysmall, y, root=0) ## gether 

if rank == 0:
    print(np.concatenate(y)) ## concat those fatherd
    print(ytarget) ## print them out. 
## ends up working out well. 
## 
