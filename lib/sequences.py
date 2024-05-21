#!/usr/bin/env python3

def fibonacci(length):
    fib_sequence = [0, 1]
    while len(fib_sequence) < length:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def print_fibonacci(length):
    fib_sequence = fibonacci(length)
    if length == 0:
        print([])
    elif length == 1:
        print([fib_sequence[0]])
    else:
        print(fib_sequence)
    pass