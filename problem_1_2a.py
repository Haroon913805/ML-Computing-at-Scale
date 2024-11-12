import random
from math import pi
import time

def sample_pi(n):
    """ Perform n steps of Monte Carlo simulation for estimating Pi/4.
        Returns the number of sucesses."""
    s = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        if x**2 + y**2 <= 1.0:
            s += 1
    return s


def compute_pi(steps):
    """Computes pi and prints results"""
    
    start_serial_a: int = time.time()
    
    random.seed(1)
    n_total  = steps

    end_serial_a: int = time.time()

    #Parallel Execution
    start_parallel: int = time.time()
    s_total = sample_pi(n_total)
    end_parallel: int = time.time()
    
    start_serial_b: int = time.time()
    
    pi_est = (4.0*s_total)/n_total
    print(" Steps\tSuccess\tPi est.\tError")
    print("%6d\t%7d\t%1.5f\t%1.5f" % (n_total, s_total, pi_est, pi-pi_est))

    end_serial_b: int = time.time()
    
    #Serial Time Took
    serial_time: float = (end_serial_a - start_serial_a) + (end_serial_b - start_serial_b)

    parallel_time: float = end_parallel - start_parallel
    #Total time took
    total_time: float = parallel_time + serial_time

    serial_fraction: float = serial_time / total_time

    print("\nPT\tST\tTT\tSF")
    print("%1.5f\t%1.5f\t%1.5f\t%1.5f" % (parallel_time, serial_time, total_time, serial_fraction))

    return serial_fraction



if __name__ == "__main__":
    ### NOTE: The main clause will not be graded  
    ### TODO: Add/change test case to your convenience
    steps = 1000
    
    serial_fraction = compute_pi(steps)


