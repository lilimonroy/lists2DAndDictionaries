# ----------*CHALLENGE 101*----------* 
# Using program 100, ask the user for a name and a region. Display the relevant data. Ask
# the user for the name and region of data they want to change and allow them to make
# the alteration to the sales figure. Display the sales for all regions for the name they choose.
#        *  N      S      E      W
#   **********************************
#   John *  3056   8463   8441   2694
#   Tom  *  4832   6786   4737   3612
#   Anne *  5239   4802   5820   1859
#   Fiona*  3904   3645   8821   2451

sales = {'John':{'N':3056, 'S':8463, 'E':8441, 'W':2694},'Tom':{'N':4832, 'S':6786, 'E':4737, 'W':3612},'Anne':{'N':5239, 'S':4802, 'E':5820, 'W':1859},'Fiona':{'N':3904, 'S':3645, 'E':8821, 'W':2451}}
print(sales)
name = input("Enter the name you want to change: ")
region = input("Enter the region you want to change: ")
print(sales[name][region])
change_value = int(input("Enter the new value: "))
sales[name][region] = change_value

print(sales[name])