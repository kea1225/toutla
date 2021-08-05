def fibo_num():
    ''' This function design explicitly for Fiboncci numbers'''
    limit = 55
    fst_val = 0
    sec_val = 1
    limit_count = 0
    fib_list = []
    while True : 
       fib_seq = fst_val + sec_val
       fib_list.append(fib_seq)
       fst_val = sec_val
       sec_val = fib_seq
       print(" This is an interesting concept {}".format(fib_list))
       if fib_seq == limit: break #return fib_seq
    print(end='\n')   
    print(f"{fib_list}, This is the expected list")
fibo_num()

