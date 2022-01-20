# NAME OF AUTHOR: Matthew F
# NAME OF THE PROGRAM: Q2 Average 
# DATE OF CREATION: 20/01/2022
# PURPOSE OF PROGRAM: Finding sum and average of given numbers

# VARIABLE DEFINITION
given = 1
numbs = [0]
ans = 0

# INPUT
print("Please begin entering numbers. Enter 0 when you are finished")


# PROCESSING
while given != 0:
  numbs.append(given)
  given = int(input())
ans = sum(numbs) - 1
avg = ans / 2

# OUTPUT
numbs.remove(1)
print("Sum:")
print(ans)
print("Average:")
print(avg)