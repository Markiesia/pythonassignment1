# Create a program that asks the user for a positive number `n` and then prints the sum of all the numbers from 1 up to `n`. For example, if `n` = 5, the program should print the sum 1+2+3+4+5 = 15.

# Step Step 1: Prompt the user to input a positive integer
n = int(input("Enter a positive integer: "))
# What I am doing: The input() function collects the user's input as a string. Wrapping it in int() converts the string to an integer so that it can be used in calculations.
# Why it is used? The program needs a numeric value to calculate the summation, so converting the input to an integer is important.

# Step 2: Initialize a variable `total` to 0. This will hold the running sum:
total = 0
# What I am doing: This variable will accumulate the sum of numbers from 1 to n. total = 0 creates a variable to store the running sum of numbers as the loop progresses.
# Why it is used? It's a common practice to initialize a variable to 0 when you want to accumulate a value over time. Starting with 0 ensures that the addition begins with a clean slate, and the variable is ready to hold the cumulative sum.

# Step 3: Use a `for` loop or `while` loop to add each number from 1 to `n` to the total
for i in range(1, n + 1):  
    total += i  
# The range(1, n + 1) generates numbers from 1 to n. The += operator adds each number (i) to the 'total'. The for loop iterates over a sequence of numbers from 1 to n (inclusive). 
# Why it is used? To add up all the numbers from 1 to n, the loop processes each number in the range sequentially.
# Adding numbers to total:
# Each iteration of the loop adds the current number (i) to the total. This process continues until all numbers from 1 to n have been added to the total.
#  This step updates the total variable to include the next number in the sequence, building up the sum incrementally.

# Step 4: Print the result
print("The sum of numbers from 1 to " + str(n) + " is " + str(total))
# What I am doing: The print() function displays the result of the summation, including the value of n and the calculated total.
# Why it is used? To provide the user with the final result of the summation, making the program more informative and user-friendly.