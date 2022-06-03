# ----------*CHALLENGE 102*----------* 
# Ask the user to enter the name, age and shoe size for four people. 
# Ask for the name of one of the people in the list and display their age and shoe size.

dictionary = {}
for each_people in range(0,4):
    name = input("Enter the name: ")
    shoe_size = input("Enter the shoe's size: ")
    age = int(input("Enter the age: "))
    
    dictionary[name] = {"shoe size":shoe_size, "age":age}

print(dictionary)
