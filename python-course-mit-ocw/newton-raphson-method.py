def newton_raphson_cube_root(x, initial_guess=1.0, tolerance=1e-15, max_iter=10000000):
    """
    Newton-Raphson method to find the cube root of x.
    Solves f(g) = g^3 - x = 0.
    """
    g = initial_guess
    for i in range(max_iter):
        f = g**3 - x  # f(g)
        f_prime = 3 * g**2  # f'(g)
        print('it:', i, 'g:', g, 'f:', f, "f':", f_prime, "f/f':", f/f_prime)
        
        if abs(f) < tolerance:  # Check if the solution is close enough
            return g
        
        if f_prime == 0:  # Avoid division by zero
            raise ValueError("Derivative is zero. No solution found.")
        
        g = g - f / f_prime  # Update guess
    
    raise ValueError("Newton-Raphson method did not converge.")

# Example usage
if __name__ == "__main__":
    x = 10  # Find the cube root of 27
    initial_guess = 5
    result = newton_raphson_cube_root(x, initial_guess)
    print(f"Cube root of {x}: {result}")

