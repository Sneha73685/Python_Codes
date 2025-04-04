import random
x = random.randint(1,6)

y = random.random()

myList = ['rock' , 'scissor', 'paper']

z = random.choice(myList)
print(z)
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'K', 'Q', 'J', 'A']
random.shuffle(cards)
print(cards)import random

# Generate a random integer between 1 and 6
x = random.randint(1, 6)
print(f"Random integer: {x}")

# Generate a random float between 0 and 1
y = random.random()
print(f"Random float: {y}")

# Define a list of game options
myList = ['rock', 'scissor', 'paper']

# Select a random option from the list
z = random.choice(myList)
print(f"Random game option: {z}")

# Define a list of cards
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'K', 'Q', 'J', 'A']

# Shuffle the cards
random.shuffle(cards)
print(f"Shuffled cards: {cards}")