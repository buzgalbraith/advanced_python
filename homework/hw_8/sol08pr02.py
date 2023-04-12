from mpi4py import MPI
import numpy as np
import sys




comm = MPI.COMM_WORLD
def parse_xy():
    for line in sys.stdin: ## read line in from standard input 
        try: ## try to convert to float
            x=float(line)
        except: ## if this does not work return an error message and abort program 
            print("x should be real number")  
            comm.Abort()      
        if(x==0): ## if x is 0 return an error message and abort program 
            print("x can not equal 0")
            comm.Abort()
        else:
            break
    for line in sys.stdin: ## does the same for y 
        try:
            y=float(line)
        except:
            print("y should be real number")  
            comm.Abort()      
        if(y==0):
            print("y can not equal 0")
            comm.Abort()
        else:
            break
    return x,y
def process_0(X):
        X[2]=X[2]*X[0] ## change the value of p 
        comm.Send(X, dest=1) ## send to rank 1, with blocking
        comm.Recv(X, source=1) ## receive from rank 1 with blocking 
        return X ## return buffer
def process_1(X):
    comm.Recv(X, source=0) ## receive from rank 0 with blocking
    X[2]=X[2]/X[1] ## update p value
    comm.Send(X, dest=0) ## send to rank 1 
    if(i==4):  ## if terminal case end
        print("terminal value : {0}".format(X[2])) ## print value
    return X ## return 

rank = comm.Get_rank()
X=np.zeros(3) ## initialize buffer of form [x,y,p]
X[2]=1 ## set p to initial value of 1. 
for i in range(5): # loop 5 times 
    if(rank==0): ## rank 0 case 
        if(i==0): ## is the first process so needs to initialize x,y
            X[0],X[1]=parse_xy() ## function to pase x,y and do some exception handling then set them 2 the x[0], x[1] val
        X=process_0(X) ## process 1 function set to buffer
    else: ## rank 1 case
        X=process_1(X) ## process 2 function set to buffer
    
