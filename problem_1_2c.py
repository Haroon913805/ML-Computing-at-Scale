import random
from math import pi

def sample_pi(n, seed):
    """Perform n steps of Monte Carlo simulation for estimating Pi/4.
       Returns the number of successes."""
    random.seed(seed)  # Seed the random number generator
    s = 0
    for _ in range(n):
        x, y = random.random(), random.random()
        if x**2 + y**2 <= 1:
            s += 1
    return s

def compute_pi(steps, seed):
    """Compute the Pi estimate and print results."""
    s_total = sample_pi(steps, seed)  # Use sample_pi with given steps and seed
    pi_est = (4.0 * s_total) / steps  # Calculate Pi estimate
    error = pi - pi_est
    print(" Steps\tSuccess\tPi est.\tError")
    print("%6d\t%7d\t%1.5f\t%1.5f" % (steps, s_total, pi_est, error))

if __name__ == "__main__":
    steps = 1000000
    seed = 42
    compute_pi(steps, seed)
