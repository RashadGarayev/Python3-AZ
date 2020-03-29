
def factorial_recursive(n):
    """
    Returns factorial of a given number using recursion.

    fact(1) -------> 1

    """
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)
