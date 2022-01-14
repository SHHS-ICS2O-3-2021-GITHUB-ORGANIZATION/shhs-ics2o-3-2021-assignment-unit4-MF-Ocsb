# NAME OF AUTHOR: Matthew F
# NAME OF THE PROGRAM: Volume Calculator
# DATE OF CREATION:  January 13th 2022
# PURPOSE OF PROGRAM: Calculating volume 

# VARIABLE DEFINITION
length = 0
width = 0
depth = 0
ans = 0

# INPUT
print("Hello User! Please input the length.")
length = int(input())
print("Please input the width.")
width = int(input())
print("Please input the depth.")
depth = int(input())

# PROCESSING
ans = length * width * depth

# OUTPUT
print("The volume of your rectangular prism is:")
print(ans)