def safe_divide(numerator, denominator):
    """Perform division with error handling for division by zero and non-numeric inputs."""
    try:
        # Convert inputs to float
        numerator = float(numerator)
        denominator = float(denominator)

        # Division logic
        result = numerator / denominator
        return result

    except ZeroDivisionError:
        # Handle division by zero
        return "Error: Cannot divide by zero."
    except ValueError:
        # Handle non-numeric input
        return "Error: Both numerator and denominator must be numeric values."
