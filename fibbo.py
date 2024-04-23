def fibonacci_up_to_100():
    # Initialize variables to store the first two numbers of the Fibonacci sequence
    fib_seq = [0, 1]

    # Continue generating Fibonacci numbers until the last number is less than or equal to 100
    while fib_seq[-1] + fib_seq[-2] <= 100:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])

    # Print the Fibonacci sequence up to 100
    print("Fibonacci sequence up to 100:")
    print(fib_seq)

# Calling the function to generate Fibonacci sequence up to 100
fibonacci_up_to_100()
