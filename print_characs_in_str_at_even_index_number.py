# Exercise 3: Print characters from a string that are present at an even index number
# Write a program to accept a string from the user and display characters that are present at an even index number.

# pseudocode
# user input
string = input("Enter a word: ")
#printing original string
print(f"The original word is {string}.")
print("Printing only even index characters")
# for loop to print the even characs in separate line
for i in string[::2]:
    print(i)