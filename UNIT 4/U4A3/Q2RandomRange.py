# NAME OF AUTHOR: Matthew F
# NAME OF THE PROGRAM:  Q2RandomRange
# DATE OF CREATION: 01/17/2022
# PURPOSE OF PROGRAM: Generating numbers with a given range

# VARIABLE DEFINITION
start = 0
end = 0


# INPUT
print("This program generates a random number from your given range.")
print("Enter a starting number")
start = int(input())
print("Now, enter an ending number (Greater than start)")
end = int(input())

# PROCESSING
import random
from random import randint
num = randint(start, end)

# OUTPUT
print(num)

