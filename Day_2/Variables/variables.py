# Day 2: 30 Days of python programming

first_name = 'python'
last_name = 'programming'
full_name = 'Linkedin_leraning'
country_name = 'India'
city_name = 'kolkota'
age = 27
year = 2023
var_1,var_2,var_3 = 'India','in',2023

# Check the data type of all your variables using type() built-in function
print(type(first_name))
print(type(last_name))
print(type(var_1))

# Using the len() built-in function, find the length of your first name
print(len(first_name))

# Compare the length of your first name and your last name

a = len(first_name)
b = len(last_name)

if a>b:
    print('%s is larger than %s'%(first_name,last_name))
else:
    print('%s is larger than %s' % (last_name, first_name))

# Declare 5 as num_one and 4 as num_two

num_1 = 5
num_2 = 4

total = num_1 + num_2
print(total)

total = num_1 - num_2
print(total)

total = num_1 * num_2
print(total)

total = num_1 % num_2
print(total)

total = num_1 // num_2
print(total)

'''The radius of a circle is 30 meters.
Calculate the area of a circle and assign the value to a variable name of area_of_circle
Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
Take radius as user input and calculate the area.'''

r = 30
area = 3.14 * r * r
print("area of circle is ",area)

circumference = 2*3.14*r
print(circumference)

radius = input("Enter the radius:")
area = 3.14 * r * r
print(area)

