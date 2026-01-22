"""Advanced multiplication operations module."""

def multiply_multiple(*args):
    """Multiply multiple numbers together.
    
    Args:
        *args: Variable number of numeric arguments
        
    Returns:
        The product of all arguments
        
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
        scalar: Scalar value to multiply
        
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
    print("Advanced Multiplication Operations Demo")
    print("=" * 40)
    
    # Multiply multiple numbers
    print(f"Multiply 2, 3, 4: {multiply_multiple(2, 3, 4)}")
    
    # Multiply list
    print(f"Multiply list [2, 3, 4, 5]: {multiply_list([2, 3, 4, 5])}")
    
    # Power
    print(f"2 to the power of 8: {power(2, 8)}")
    
    # Factorial
    print(f"Factorial of 6: {factorial(6)}")
    
    # Square and Cube
    print(f"Square of 7: {square(7)}")
    print(f"Cube of 4: {cube(4)}")
    
    # Matrix scalar multiplication
    matrix = [[1, 2, 3], [4, 5, 6]]
    print(f"Matrix {matrix} multiplied by 3:")
    print(multiply_matrix_scalar(matrix, 3))