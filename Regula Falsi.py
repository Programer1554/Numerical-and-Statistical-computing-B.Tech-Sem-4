def f(x):
    return x**3 - x - 2

def regula_falsi(a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        print("Invalid initial guesses. f(a) and f(b) must have opposite signs.")
        return None

    print("Iter\t\ta\t\tb\t\tc\t\tf(c)")
    
    for i in range(1, max_iter + 1):
        # Regula Falsi formula
        c = a - (f(a) * (b - a)) / (f(b) - f(a))

        print(f"{i}\t\t{a:.6f}\t{b:.6f}\t{c:.6f}\t{f(c):.6f}")

        if abs(f(c)) < tol:
            print(f"\nRoot found: {c:.6f} (after {i} iterations)")
            return c

        # Decide the side to repeat the steps
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    print("Method did not converge within the maximum number of iterations.")
    return None

a = 1
b = 2
regula_falsi(a, b)
