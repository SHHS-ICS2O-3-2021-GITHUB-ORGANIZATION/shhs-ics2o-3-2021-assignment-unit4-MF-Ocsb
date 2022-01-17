# NAME OF AUTHOR: Matthew F
# NAME OF THE PROGRAM: Q3Addition
# DATE OF CREATION:  January 14th 2022
# PURPOSE OF PROGRAM: To generate addition problems and solve

# VARIABLE DEFINITION
num1 = 0
num2 = 0
ans = 0

# INPUT
print("Press enter to generate an equation")
input()
import random
from random import randint
num1 = int(randint(1, 100))
num2 = int(randint(1, 100))
print(num1)
print(num2)

# PROCESSING
ans = num1 + num2

# OUTPUT
print(), print(num1), print("+"), print(num2), print("="), print(ans)