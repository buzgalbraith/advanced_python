
from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD ## initialize communicator
rank = comm.Get_rank()  ## get the rank of each worker 
num_moments=15 ## save the total number of moments we want to calculate
m_moment = np.zeros((1)) ## buffer to hold each moment as we calculate them   
for m in range(1, num_moments+1): ## goes from the 1st the nth moment. 
    if rank == 0: ##initialize range
        n = 16    ## size n 
        X_range = np.linspace(0, 1000,n*1000)  ## 1 interval between 1 and 1000 of length 16,000
        X_range= X_range.reshape(16,-1) ## the interval subdivided into 16 intervals of length 1,000
    else: 
        X_range=None ## initialize buffer for non-zero rank workers 
    chunk_range = comm.scatter(X_range, root=0) ## scatter the range to all the workers
    dt=chunk_range[1]-chunk_range[0] ## find the width parameter dt
    chunk_int = np.sum(np.power(chunk_range, m) * np.exp(-chunk_range) * dt) ## numerically calculate each chunks integral 
    comm.Reduce(chunk_int,m_moment,op= MPI.SUM,root= 0) ## sum all integrals to get a total integral over the range (ie the moment )
    if rank == 0: ## terminal case 
        print('moment',m ,"=", m_moment[0]) ## output result
