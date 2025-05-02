def gauss_seidel(a, b, tolerance=1e-10, max_iterations=100):
    n = len(a)
    x = [0.0 for _ in range(n)]

    print("Iteration results:")

    for iteration in range(1, max_iterations + 1):
        x_new = x.copy()

        for i in range(n):
            sum1 = sum(a[i][j] * x_new[j] for j in range(i))
            sum2 = sum(a[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - sum1 - sum2) / a[i][i]

        print(f"Iter {iteration}: {['%.6f' % xi for xi in x_new]}")

        if all(abs(x_new[i] - x[i]) < tolerance for i in range(n)):
            print("\nConverged in", iteration, "iterations.")
            return x_new

        x = x_new

    print("\nDid not converge within the maximum number of iterations.")
    return x

a = [
    [10, 2, 1],
    [1, 5, 1],
    [2, 3, 10]
]
b = [9, 5, 7]

solution = gauss_seidel(a, b)
print("\nSolution:", ["%.6f" % s for s in solution])
