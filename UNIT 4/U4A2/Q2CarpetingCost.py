# NAME OF AUTHOR: Matthew F
# NAME OF THE PROGRAM: Carpet Cost Calculator
# DATE OF CREATION:  January 13 2022
# PURPOSE OF PROGRAM: Calculating carpet cost 

# VARIABLE DEFINITION
length = 0
width = 0
area = 0
cost = 0

# INPUT
print("Hello User! Please enter the length and width measurements to   calculate the cost.")
print("Please enter the length (Meters)")
length = int(input())
print("Please enter the width (Meters)")
width = int(input())

# PROCESSING
area = length * width
cost = area * 2.25

# OUTPUT
print("The cost of your carpet is:")
print(cost)