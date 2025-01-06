# Create a program that asks the user for their name and then prints a personalized greeting. The program should also show them the length of their name and display their name in uppercase letters.

#Step 1: Prompting for User Input()
name = input("Enter your name: ")  
# What I am doing: When I use the input() function with the name variable, it pauses the program and waits for the user to type or enter their name. Once the user press Enter, the program captures the name that was entered and stores it as a string. This means the user can interact with the program by providing information that it needs to use later, like the name in this case. It’s a simple way for the program to ask the user for input and respond based on what the user provides.
# Why it is used? We need the user's name to create a personalized interaction. Storing the input in the variable name allows us to reuse it in subsequent steps.
# Whatever the user types becomes the value of the variable name, making it accessible to the rest of the code.

# Step 2: Printing a Greeting print()
print("Hello, " + name + "! Nice to meet you.")  
# What I am doing: The print() function displays text or the result of expressions to the screen. The message includes the user's name, which is retrieved from the name variable.
# Why it is used? To greet the user in a friendly way, making the program engaging and interactive. The concatenation (+) combines the specified text with the variable name to create a single message and prints it to the screen.

# Step 3: Calculating Length of Name len()
length_of_name = len(name)  
print("Your name has " + str(length_of_name) + " characters.")  
# What I am doing: The len() function counts the number of characters in a string, including spaces and special characters and prints a message informing the user of their name's length. The result is stored in the length_of_name variable.
# Why it is used? To provide information about the length of the user's name, which can be useful for various purposes, such as formatting or validation.

# Step 4: Converting to Uppercase upper()
print("In uppercase, your name looks like: " + name.upper())  
# What I am doing: The upper() method converts all letters in the string to uppercase, and we display this result to the user.
# Why it is used? To provide a standardized format for the user's name, which can be useful for various purposes, such as displaying in a specific format or comparing names. Storing results in variables makes the code cleaner, more readable, and reusable if needed later.
# Another way to use uppercase is to just capiatlize the name input by the user, but this is not the same as uppercase.