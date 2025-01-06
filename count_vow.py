# Create a program that asks the user for a sentence (or any string of text) and then counts how many vowels (a, e, i, o, u) are in that sentence. Print the total number of vowels found.


# Step 1: Prompt the user to enter a sentence
sentence = input("Enter a sentence: ")
# What I am doing: The input() function asks the user to type a sentence and captures it as a string. The captured string is stored in the sentence variable.
# Why it is used? The program needs the user's input to perform the vowel counting.

# Step 2: Convert the sentence to lowercase to make checking easier (so that 'A' and 'a' are treated the same)
sentence = sentence.lower()
# What I am doing: The lower() method converts all characters in the string to lowercase. 
# Why it is used? To ensure that the program treats uppercase and lowercase vowels equally, making the vowel counting more accurate. Vowel checks are case-insensitive (ex. "A" and "a" are both vowels). This step avoids having to explicitly check for uppercase vowels.

# Step 3: Initialize a counter variable to 0 for counting vowels
vowel_count = 0
#  Initializing a variable is like giving it a starting point so the program knows how to work with it.
# What I am doing: This variable will keep track of how many vowels are found in the sentence. It starts at 0 because no vowels have been found yet.
# Why it is used? It's like a counter that keeps track of how many vowels are in the sentence.

# Step 4: Loop through each character in the sentence. For each character, check if it is a vowel (a, e, i, o, u). If it is, increase the counter by 1
for char in sentence:
    if char in "aeiou":  
        vowel_count += 1  
# Iterates over each character in the string one by one. The for loop checks each character in the sentence. If the character matches any in "aeiou", the counter is increased by 1.
# Why it is used? It's like checking each letter in the sentence to see if it's a vowel. If it is, it adds 1 to the counter.This condition ensures that only vowels are counted, ignoring consonants, spaces, and punctuation.
# You can use any character in the string "aeiou" to check for vowels. For example, you could also use "y" to include "y" as a vowel.
# += 1 is a shorthand way to add 1 to a variable. It's like saying "add 1 to the vowel_count variable."

# Step 5: Print the total number of vowels
print("The total number of vowels in your sentence is:", vowel_count)
# What I am doing: This prints the final count of vowels in the sentence with a descriptive message.
# Why it is used? It provides the user with the result of the vowel counting, making the program more informative and user-friendly.