
from mpi4py import MPI
import numpy as np

## i think one needs to use non-blocking but with a lot of wait statemnts so it is equivelent to blocking, which is needed

def worker_node(rank,size):
    src=rank-1  ## where input comes from
    req = comm.Irecv(buf, source=src) ## receive input
    req.Wait() ## blocking wait statement (so same as com.wait())
    buf[0] += rank**2 ## adds square of it's own rank to the buffer
    dest = (rank + 1)%size ## calculates where to send it's output, use modulus size so that final rank sends to process 0.
    comm.Isend(buf, dest=dest) ##sends value without explicit blocking. 
def terminal_node(rank, size):
    dest=  (rank + 1)%size ## calculates where to send it's output, use modulus size so that final rank sends to process 0.
    comm.Isend(buf, dest=dest) ## sends initial buffer to process one 
    src=size-1 ## sets source to final rank
    req = comm.Irecv(buf, source=src) ## takes final value 
    req.Wait() ## blocking statement 
    print("Terminal Value  : {0}".format(buf[0])) ## prints output
 


comm = MPI.COMM_WORLD ## initialize communicator
size = comm.Get_size()
rank = comm.Get_rank() 
buf = np.zeros(1)  # buffer with a single integer variable initialized to zero
if rank > 0: ## worker node condition 
    worker_node(rank,size)
if rank == 0: ## terminal node condition 
    terminal_node(rank, size)
