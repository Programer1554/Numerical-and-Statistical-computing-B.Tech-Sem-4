import numpy as np

def jacobi(A, b, x0=None, tol=1e-10, max_iter=100):
    """
    Solve the linear system Ax = b using Jacobi's Method.
    
    Parameters:
    A        : Coefficient matrix (numpy array)
    b        : Right-hand side vector (numpy array)
    x0       : Initial guess (default is zero vector)
    tol      : Tolerance for convergence
    max_iter : Maximum number of iterations
    
    Returns:
    x        : Solution vector
    """
    n = len(b)
    if x0 is None:
        x = np.zeros(n)
    else:
        x = x0.copy()
    
    print(f"{'Iteration':>10} | {'x':>30}")
    print("-" * 45)
    
    for k in range(max_iter):
        x_new = np.zeros_like(x)
        
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - s) / A[i][i]
        
        print(f"{k+1:10d} | {x_new}")
        
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            print("\nConverged.")
            return x_new
        
        x = x_new
    
    print("\nDid not converge within the maximum number of iterations.")
    return x


A = np.array([[10., -1., 2., 0.],
              [-1., 11., -1., 3.],
              [2., -1., 10., -1.],
              [0.0, 3., -1., 8.]])
b = np.array([6., 25., -11., 15.])
initial_guess = np.zeros(len(b))

solution = jacobi(A, b, initial_guess)
print(f"\nApproximate solution:\n{solution}")
