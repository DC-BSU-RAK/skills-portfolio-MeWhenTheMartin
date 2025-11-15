#Searching in the file 
with open("_Resources/studentMarks.txt") as file_handler:
   	lines = file_handler.readlines() 
# Empty lists to copy values from file
name = []
age = []
gender = []
#Read the individual lines from file
for l in lines:
   	data = l.split(',')
   	# Use split() to retrieve individual values separated by delimiter
   	#Append the values of data list to individual lists
	name.append((data[0]))
	age.append((data[1]))
	gender.append((data[2].replace("\n", "")))   	
 
print("Name list \n", name)
print("Age list \n", age)
print("Gender list \n", gender)