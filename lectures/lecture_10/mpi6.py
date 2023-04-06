
# this code is similar to mpi3.py, 
# but it uses Wait to block the processes
#####

import numpy
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

randNum = numpy.zeros(1)

if rank == 1:
        randNum = numpy.random.random_sample(1)
        print("Process", rank, "drew the number", randNum[0])
        
        req = comm.Isend(randNum, dest=0)
       # req.Wait() ## just having this one will make it 100% wrong. 
        ## wait only really makes sense when we are reciving something. when ever things are done asynchonalsly want to make sure you are not modifying hte same piece of data at teh same time.
        print('something here')
        
if rank == 0:
        print("Process", rank, "before receiving has the number", randNum[0])
        
        req = comm.Irecv(randNum, source=1) ## might not be recived it will just move on. this gives you flexability but want to be carefull. 
        #req.Wait() ## if wait here that will not move on with out it. 
        while not req.Test():
                print("waiting")
        print("Process", rank, "received the number", randNum[0])
