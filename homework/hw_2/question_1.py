import time
def f_rec(n):
    out=0
    if(n>=5):
        out=out+f_rec(n-5)
    if(n>=2):
        out=out+f_rec(n-2)
    if(n>=1):
        out=out+f_rec(n-1)
    if(n==0):
        return 1
    else:
        return out

def f_memo(n):
    memo={n:0 for n in range(n+1)}
    memo[1]=1
    memo[2]=1
    memo[5]=1
    for i in range(2,n+1):
        if(i>5):
            memo[i]=memo[i]+memo[i-1]+ memo[i-2]+memo[i-5]
        else:
            memo[i]=memo[i]+memo[i-1]+ memo[i-2]
    return memo[n]

def f_it(n): 
    a=[9, 5, 3, 2, 1]
    b=0
    if(n<=5):
        return a[5-n]
    for i in range(6,n+1):
        b=a[0]+a[1]+a[-1]
        a=[b]+a[0:-1]
    return a[0]
def time_function(f, d):
    t = time.process_time() 
    f_time=f(**d) 
    elapsed_time_c = time.process_time() - t
    print("{0} on {1}\n time: %0.10f; result: %d".format(f.__name__, d) % (elapsed_time_c, f_time))
time_function(f=f_rec, d={"n":10})
time_function(f=f_memo, d={"n":10})
time_function(f=f_it, d={"n":10})
time_function(f=f_rec, d={"n":25})
time_function(f=f_memo, d={"n":25})
time_function(f=f_it, d={"n":25})
time_function(f=f_memo, d={"n":50})
time_function(f=f_it, d={"n":50})
time_function(f=f_memo, d={"n":100})
time_function(f=f_it, d={"n":100})

