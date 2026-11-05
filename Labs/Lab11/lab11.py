import numpy as np
import matplotlib.pyplot as plt

from adaptive_quad import eval_composite_trap, eval_composite_simpsons, eval_gauss_quad, adaptive_quad

#Problem 4.2
def driver():
    f = lambda x: np.sin(1 / x)
    a, b = 0.1, 2.0
    tol = 1e-3
    N = 5

    for name, method in [
        ("Trapezoid", eval_composite_trap),
        ("Simpson", eval_composite_simpsons),
        ("Gaussian", eval_gauss_quad),]:
        I, nodes, nintervals = adaptive_quad(a, b, f, tol, N, method)
        print(name, "integral:", I, "intervals:", nintervals)


if __name__ == "__main__":
    driver()


# The method with the least number of intervals is Gaussian quad, then Simpson's, then Trapezoid.
# Gaussian is the most efficient because it needs fewer intervals to achieve the same accuracy.
