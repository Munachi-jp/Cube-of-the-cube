# Define function to calculate cube
def cube(number):
    return number * number * number

# Define a function which will execute cube function
# if the user-entered number is divisible by 3
def by_three(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return 343

# Display result
print(by_three(7))  # Output: False
print(by_three(4))  # Output: False
