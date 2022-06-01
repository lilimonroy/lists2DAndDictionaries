# ----------*CHALLENGE 097* ----------* 
# Using the 2D list from program 096, ask the user to select a row and a column and display that value.
#     * 0    1    2
#   ****************
#   0 * 2    5    8
#   1 * 3    7    4
#   2 * 1    6    9
#   3 * 4    2    0

numbers = ([0,1,2],[0,2,5,8],[1,3,7,4],[2,1,6,9],[3,4,2,0])

row = int(input("Which row do you want? "))
column = int(input("Which column do you want? "))


print("The values is",numbers[row][column])
