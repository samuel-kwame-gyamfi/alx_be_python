# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize a counter for the rows
row = 0

# Use a while loop to iterate through each row
while row < size:
    # Use a for loop to print asterisks for the current row
    for _ in range(size):
        print("*", end="")  # Print asterisks on the same line
    print()  # Move to the next line after the row is complete
    row += 1  # Increment the row counter

