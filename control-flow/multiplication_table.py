# Prompt the user for a number
number = int(input("Enter a number to see its multiplication table: "))

# Generate and print the multiplication table
print(f"Multiplication Table for {number}:")
for i in range(1, 11):  # Loop from 1 to 10
    product = number * i
    print(f"{number} * {i} = {product}")

