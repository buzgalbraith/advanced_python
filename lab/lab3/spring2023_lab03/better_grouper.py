import resource

def better_grouper(inputs, n):
    iters = [iter(inputs)] * n
    return zip(*iters) ## srat means that each input of the list is a new paramter 
    ## same as zip(itter[0], itter[1])

for _ in better_grouper(range(100000000), 10): ##will repeate teh itteration n times 
    pass

## Comment out this line if on Linux machine
print("Memory Used(kB): ", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024)