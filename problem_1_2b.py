import multiprocessing # See https://docs.python.org/3/library/multiprocessing.html
import random
from math import pi
import time

def sample_pi(n):
    """ Perform n steps of Monte Carlo simulation for estimating Pi/4.
        Returns the number of sucesses."""
    random.seed()
    s = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        if x**2 + y**2 <= 1.0:
            s += 1
    return s


def compute_pi(steps, num_worker):
    """ Return value should be the time measured for the execution """
    ### TODO: Add/change code below
    random.seed(1)

    #Dive steps among workers(num_worker) 
    steps_pro_worker = steps // num_worker

    #Start measuring time before multiprocessing
    start_t = time.time()
    with multiprocessing.Pool(num_worker) as pool:
        #Call our sample_pi function in each worker
        results = pool.map(sample_pi, [steps_pro_worker] * num_worker)
    
    #Sum results from multiprocessing
    s_total = sum(results)

    pi_est = (4.0*s_total)/steps
    #End time
    measured_time = time.time() - start_t
    print(" Steps\tSuccess\tPi est.\tError")
    print("%6d\t%7d\t%1.5f\t%1.5f" % (steps, s_total, pi_est, pi-pi_est))
    print(measured_time)
    ### TODO: Add/change code above
    return measured_time


if __name__ == "__main__":
    ### NOTE: The main clause will not be graded  
    ### TODO: Add/change test case to your convenience
    num_workers = 2
    steps = 1000
    measured_time = compute_pi(steps, num_workers)

 