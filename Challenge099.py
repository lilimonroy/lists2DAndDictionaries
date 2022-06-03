# ----------*CHALLENGE 099*----------* 
# Change your previous program to ask the user which row they want displayed. Display that
# row. Ask which column in that row they want displayed and display the value that is held
# there. Ask the user if they want to change the value. If they do, ask for a new value and change
# the data. Finally, display the whole row again.

#     * 0    1    2
#   ****************
#   0 * 2    5    8
#   1 * 3    7    4
#   2 * 1    6    9
#   3 * 4    2    0


numbers = ([0,1,2],[0,2,5,8],[1,3,7,4],[2,1,6,9],[3,4,2,0])

row = int(input("Which row do you want displayed? "))

print("The row is",numbers[row])

column = int(input("Which column in that row want displayed? "))

print("The value of the row",row,"and column", column,"is",numbers[row][column])

new_value_question = input("Do you want to change the value? [yes/no] ")
new_value_question = new_value_question.lower()
if new_value_question == 'yes':
    new_value = int(input("Enter the new value: "))
    numbers[row][column] = new_value
    print("The row now is",numbers[row])
elif new_value_question =='no':
    print("Thank you!")
else:
    print("Write a correct answer.")
