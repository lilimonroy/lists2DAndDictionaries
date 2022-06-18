# ----------*CHALLENGE 102*----------* 
# Adapt program 102 to display the names and ages of all the people in the list but do not show their shoe size.


dictionary = {}
for each_people in range(0,4):
    name = input("Enter the name: ")
    shoe_size = input("Enter the shoe's size: ")
    age = int(input("Enter the age: "))
    
    dictionary[name] = {"age":age}

print(dictionary)
