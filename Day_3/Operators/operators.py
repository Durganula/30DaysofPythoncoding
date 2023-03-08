# Declare your age as integer variable

age = 10

# Declare your height as a float variable
height = 5.6

# Declare a variable that store a complex number
variable = 1+1j

# Write a script that prompts the user to enter base and height of the triangle and 
# calculate an area of this triangle (area = 0.5 x b x h).

base = input("Enter the base")
height = input('Enter the height')

area = 0.5 * base * height

# Write a script that prompts the user to enter side a,
#  side b, and side c of the triangle. 
# Calculate the perimeter of the triangle (perimeter = a + b + c).

a = input('enter the side a')
b = input('Enter the side b')
c = input('Enter the side c')
perimeter = print(a+b+c)
print("Perimeter of the trainge is ", perimeter)

# Find the length of 'python' and 'dragon' and make a falsy comparison statement.

x = len('python')
y = len('dragon')

if x != y:
    print('False')
else:
    print('True')

# Use and operator to check if 'on' is found in both 'python' and 'dragon'

if 'on' in x and 'on' in y:
    print("'on' is present in both x and y")
else:
    print("False")

# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.

z = "I hope this course is not full of jargon"

if "jargon" in z:
    print("Jargon is present")
else:
    print("False")

# Find the length of the text python and convert the value to float and convert it to string

var = len(x)
result = float(var)
print(result,"length and float conversion")


# Even numbers are divisible by 2 and the remainder is zero.
#  How do you check if a number is even or not using python?

even = input("Enter the number")
if even%2==0:
    print("The number is even")
else:
    print("The number is odd")

# Check if type of '10' is equal to type of 10
if type('10') == type(10):
    print("True")
else:
    print("False")

# Check if int('9.8') is equal to 10
if int('9.8') == 10:
    print("True")
else:
    print("False")

# Writ a script that prompts the user to enter hours and rate per hour.
#  Calculate pay of the person?

hours = input("Enter the hours")
rate = input("Enter the rate per hour")
payday =  hours * rate
print("Payday is ",payday)

# Write a script that prompts the user to enter number of years.
#  Calculate the number of seconds a person can live. 
# Assume a person can live hundred years

years = input("Enter the number of years")

seconds_per_day = 86400

per_year = 86400*365

per_100_years = 86400*365*100

print(per_100_years)


# Write a Python script that displays the following table

'''
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
'''

print(1, 1, 1, 1, 1, end='\n')
print(2, 1, 2, 4, 8, end='\n')
print(3, 1, 3, 9, 27, end='\n')
print(4, 1, 4, 16, 64, end='\n')
print(5, 1, 5, 25, 125, end='\n')
