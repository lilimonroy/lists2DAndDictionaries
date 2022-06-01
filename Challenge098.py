# ----------*CHALLENGE 098* ----------* 
# Using the 2D list from program 096, ask the user which row they would like displayed and display
# just that row. Ask them to enter a new value and add it to the end of the row and display the row.
#     * 0    1    2
#   ****************
#   0 * 2    5    8
#   1 * 3    7    4
#   2 * 1    6    9
#   3 * 4    2    0

from numpy import append


numbers = ([0,1,2],[0,2,5,8],[1,3,7,4],[2,1,6,9],[3,4,2,0])

row = int(input("Which row do you want? "))

print("The row is",numbers[row])

newValue= int(input("Enter a new value for the row: "))

numbers[row].append(newValue)

print("The new value added in the row:",numbers[row])