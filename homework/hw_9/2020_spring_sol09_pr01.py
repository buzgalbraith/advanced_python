

from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD ## initialize communicator
rank = comm.Get_rank() ## get the rank of each worker. 
X_stats = np.zeros((2)) ## buffer to hold mean and std of our sample
if rank == 0: ## calculate points
    n = 256000    ## size n 
    X = np.random.uniform(low=0,high=1, size=n)  ## X is vector of random draws on uniform zero one of size n 
    # print(X.size)
    # print((X.reshape(16,-1).shape))
    X=X.reshape(16,-1) ## reshape X to be easily broken into chunks for each worker. 
#    X_stats_true = np.array([np.mean(X), np.std(X)])
else:
    X=None ## initialize buffer for non-zero rank workers 
chunk_x = comm.scatter(X, root=0) ## scatter X call it chunk x 
chunk_stats = np.array([np.mean(chunk_x), np.std(chunk_x)]) ## find summary stats for each buffer and store them in vector
# print(rank, chunk_stats) ###

comm.Reduce(chunk_stats, X_stats, MPI.SUM, 0) ## reduce the chunk stats with addition 
X_stats = X_stats/16 ## divide the chunk stats by the number of workers to get the true mean 
if rank == 0: ## terminal case 
    print('final stats of X:\nMean of X = {0}\nStandard Deviation of X = {1}'.format(X_stats[0],X_stats[1])) ## output result
#    print('true x stats =', X_stats_true)
