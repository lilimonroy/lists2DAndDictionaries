# After gathering the four names, ages and shoe sizes, ask the user to enter the name of the person 
# they want to remove from the list. Delete this row from the data and display the other rows
# on separate lines.

dictionary = {}
for each_people in range(0,4):
    name = input("Enter the name: ")
    shoe_size = input("Enter the shoe's size: ")
    age = int(input("Enter the age: "))
    
    dictionary[name] = {"shoe size":shoe_size, "age":age}

print(dictionary)

removeItem = input("Which person do you want to remove from the list?: ")

del dictionary[removeItem]

print(dictionary)

for name in dictionary:
    print(name, ":", dictionary[name])