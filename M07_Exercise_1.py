# Program to check if numbers in a list are even or odd

# Create a list of 15 numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Loop through each number in the list
for number in numbers:
    # Check if the number is even
    if number % 2 == 0:
        print(str(number) + " is even")  # Print the number and "is even"
    else:
        print(str(number) + " is odd")   # Print the number and "is odd"
