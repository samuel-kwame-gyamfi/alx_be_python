def safe_divide(numerator, denominator):
    """Perform division with error handling for division by zero and non-numeric inputs."""
    try:
        # Attempt to convert the arguments to floats
        numerator = float(numerator)
        denominator = float(denominator)

        # Perform the division
        result = numerator / denominator
        return result

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Both numerator and denominator must be numeric values."
