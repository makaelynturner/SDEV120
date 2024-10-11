# Define the function greaterThan
def greaterThan(x, y):
    # Compare x and y
    return x > y

# Main section of the program
# Scenario 1: a = 2, b = 3
a = 2
b = 3
result = greaterThan(a, b)

# Print the result with a formatted message
print("The statement " + str(a) + " is greater than " + str(b) + " is " + str(result))

# Test Scenario 2: Change variables to a = 10, b = 6
a = 10
b = 6
result = greaterThan(a, b)

# Print the result with a formatted message
print("The statement " + str(a) + " is greater than " + str(b) + " is " + str(result))
