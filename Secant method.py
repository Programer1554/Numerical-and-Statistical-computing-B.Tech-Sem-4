def f(x):
    return x**3 - x - 2

def secant_method(x0, x1, tol=1e-6, max_iter=100):
    """
    Secant Method for finding the root of a function f(x)
    
    Parameters:
    x0, x1     : Initial guesses
    tol        : Tolerance for stopping
    max_iter   : Maximum number of iterations
    
    Returns:
    Approximate root or message if convergence fails
    """
    print(f"{'Iteration':>10} | {'x_n':>12} | {'f(x_n)':>12}")
    print("-" * 40)

    for i in range(max_iter):
        f_x0 = f(x0)
        f_x1 = f(x1)

        if abs(f_x1 - f_x0) < 1e-12:
            print("Denominator too small; stopping to avoid division by zero.")
            return None

        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)

        print(f"{i+1:10d} | {x2:12.6f} | {f(x2):12.6f}")

        if abs(x2 - x1) < tol:
            print("\nConverged to a root.")
            return x2

        x0, x1 = x1, x2

    print("\nDid not converge within the maximum number of iterations.")
    return None

root = secant_method(1, 2)
if root is not None:
    print(f"\nApproximate root: {root:.6f}")
