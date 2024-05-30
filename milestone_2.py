import random

favorite_fruits = ["Apple", "Banana", "Durian", "Dragonfruit", "Elderberry"]

# Step 2: Assign the list to a variable called word_list
word_list = favorite_fruits

# Step 3: Print out the word_list
print(word_list)

word = random.choice(word_list)

print(word)

guess = input("Enter a single letter ")

# Step 1: Create an if statement to check the input
if len(guess) == 1 and guess.isalpha():
    # Step 2: Print a message if the input is valid
    print("Good guess!")
else:
    # Step 3: Print a message if the input is not valid
    print("Oops! That is not a valid input.")