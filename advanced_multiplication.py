"""Advanced multiplication operations module."""

def multiply_multiple(*args):
    """Multiply multiple numbers together.
    
    Args:
        *args: Variable number of arguments to multiply
        
    Returns:
        The product of all numbers
        
    Example:
        >>> multiply_multiple(2, 3, 4)
        24
    """
    if not args:
        return 0
    
    result = 1
    for num in args:
        result *= num
    return result

def multiply_list(numbers):
    """Multiply all numbers in a list.
    
    Args:
        numbers: List of numbers to multiply
        
    Returns:
        The product of all numbers in the list
        
    Example:
        >>> multiply_list([2, 3, 4, 5])
        120
    """
    if not numbers:
        return 0
    
    result = 1
    for num in numbers:
        result *= num
    return result

def power(base, exponent):
    """Calculate base raised to the power of exponent.
    
    Args:
        base: The base number
        exponent: The exponent
        
    Returns:
        base raised to the power of exponent
        
    Example:
        >>> power(2, 3)
        8
    """
    return base ** exponent

def factorial(n):
    """Calculate factorial of n (n!).
    
    Args:
        n: Non-negative integer
        
    Returns:
        Factorial of n
        
    Raises:
        ValueError: If n is negative
        
    Example:
        >>> factorial(5)
        120
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def multiply_matrix_scalar(matrix, scalar):
    """Multiply a matrix by a scalar value.
    
    Args:
        matrix: 2D list representing a matrix
        scalar: Number to multiply each element by
        
    Returns:
        New matrix with all elements multiplied by scalar
        
    Example:
        >>> multiply_matrix_scalar([[1, 2], [3, 4]], 2)
        [[2, 4], [6, 8]]
    """
    return [[element * scalar for element in row] for row in matrix]

def square(n):
    """Calculate the square of a number.
    
    Args:
        n: Number to square
        
    Returns:
        n squared
        
    Example:
        >>> square(5)
        25
    """
    return n * n

def cube(n):
    """Calculate the cube of a number.
    
    Args:
        n: Number to cube
        
    Returns:
        n cubed
        
    Example:
        >>> cube(3)
        27
    """
    return n * n * n

# Example usage
if __name__ == "__main__":
    print("=== Advanced Multiplication Operations ===\n")
    
    # Multiply multiple numbers
    print(f"multiply_multiple(2, 3, 4, 5) = {multiply_multiple(2, 3, 4, 5)}")
    
    # Multiply list
    numbers = [2, 3, 4, 5]
    print(f"multiply_list({numbers}) = {multiply_list(numbers)}")
    
    # Power
    print(f"power(2, 8) = {power(2, 8)}")
    
    # Factorial
    print(f"factorial(5) = {factorial(5)}")
    
    # Square and cube
    print(f"square(7) = {square(7)}")
    print(f"cube(4) = {cube(4)}")
    
    # Matrix scalar multiplication
    matrix = [[1, 2, 3], [4, 5, 6]]
    scalar = 3
    print(f"\nOriginal matrix: {matrix}")
    print(f"Matrix * {scalar} = {multiply_matrix_scalar(matrix, scalar)}")