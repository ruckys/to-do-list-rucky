def generate_fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)
    return fib_sequence

n_terms = 10  # You can change this number to generate a different number of terms
fibonacci_sequence = generate_fibonacci(n_terms)
print(f"Fibonacci Sequence (first {n_terms} terms): {fibonacci_sequence}")
