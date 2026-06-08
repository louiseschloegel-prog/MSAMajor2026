# Print Hello world
print("Hello World")

#create a variable to store my name
first_name = "Louise"

#create a variable for the name name
last_name = "Schloegel"

# write a python statement to display "My fullname is firstname lastname"
print("My full name is",first_name, last_name,sep="")

# print using the f string (string interpolation)
print(f"My full name is {first_name} {last_name}.")

# create  variables to store age and weight
age = 16
weight = 187.3
half_age = age / 2

#print a sentence with name, age, and weight
print(f"My Name is {first_name} {last_name}. \nI am {age} years old and I weigh {weight} lbs.")

#get and print the data type for age, weight, and half age
print("\nChecking Data Types\n------------------------------")
print(type(age))
print(type(weight))
print(type(half_age))

#write 3 statements using string interpolation (f string) to 
# print descriptive sentences for the data types
# "variable age is an int"
print(f"Variable age is a {(type(age))}.")
print(f"Variable weight is a {(type(weight))}.")
print(f"Variable half_age is a {(type(half_age))}.")

number_1 = "5"
number_2 = "7"
total = number_1 + number_2
print(f"Total: {total}")

