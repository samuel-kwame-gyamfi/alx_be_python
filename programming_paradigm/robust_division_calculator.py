def safe_divide(numerator, denominator):
    try:
        # Attempt to convert inputs to floats
        num = float(numerator)
        denom = float(denominator)

        # Attempt the division
        result = num / denom
        return f"The result is: {result:.2f}"

    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

    except ValueError:
        return "Error: Both numerator and denominator must be numeric values."