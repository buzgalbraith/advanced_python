#####
# overlap communication
#####

import numpy
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

randNum = numpy.zeros(1) 

if rank == 1:
#         randNum = numpy.random.random_sample(1)
        randNum = numpy.array([50], dtype=numpy.float64) ## makes the number specfic instead of random
        print("Process", rank, "drew the number", randNum[0]) ## drew the number which will always b 50
        
        comm.Isend(randNum, dest=0) ## i send this to zero 
         
        randNum[0] /= 10 # overlap communication ## do some data modivaction not caring about what rank data has recived
        print("Process", rank, "number in overlap communication =", randNum[0]) ## 
         
        req = comm.Irecv(randNum, source=0)
        req.Wait()
        print("Process", rank, "received the number", randNum[0]) ## should out put the input devided by 5

if rank == 0:
        print("Process", rank, "before receiving has the number", randNum[0])
        req = comm.Irecv(randNum, source=1) ## i recive from the other thing 
        req.Wait()
        print("Process", rank, "received the number", randNum[0]) 
        randNum *= 2 ## then we multiply by 2 qne w3ne it back
        comm.Isend(randNum, dest=1)
