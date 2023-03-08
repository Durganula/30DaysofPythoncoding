# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.

var = 'Thirty' + ' ' + 'Days' + ' ' + 'of' + ' ' + 'python'
print(var)

## Concatenate the string 'Coding', 'For', 'All' to a single string, 'Coding For All'.

var_1 = "coding" + " " + "For" + " "+ "All"
print(var_1)

# Declare a variable named company and 
# assign it to an initial value "Coding For All".

var_1

# Print the variable company using print().

print(var_1)

# Print the var_1 string using len() method and print().

print(len(var_1))

# Change all the characters to uppercase letters using upper() method.

print(var_1.upper())

# Change all the characters to lowercase letters using lower() method.

print(var_1.lower())

# Use capitalize(), title(), swapcase() methods
#  to format the value of the string Coding For All.

print(var_1.capitalize())
print(var_1.title())
print(var_1.swapcase())

# Cut(slice) out the first word of Coding For All string.
result = var_1[0:6]
print(result)

# Check if Coding For All string contains a 
# word Coding using the method index, find or other methods.
var = "Coding for all"
print(var.find('Coding'))
print(var.index('Coding'))

# Replace the word coding in the string 'Coding For All' to Python.
var = 'Coding For All'
print(var.replace('Coding','Python'))

# Change Python for Everyone to
#  Python for All using the replace method or other methods.
var = 'Python for Everyone'
print(var.replace('Everyone','All'))

# Split the string 'Coding For All' 
# using space as the separator (split()) .
var = 'Coding for All'
print(var.split(' '))

# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" 
# split the string at the comma.

var_2= "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(var_2.split(","))

## What is the character at index 0 in the string Coding For All.
# 'C'

# What is the last index of the string Coding For All.
# 13

# What character is at index 10 in "Coding For All" string.
#space

# Use index to determine the position 
# of the first occurrence of C in Coding For All.
var = "Coding For All"
print(var.index('C'))

## Use index to determine the position of the first 
# occurrence of F in Coding For All.

print(var.index('F'))

# Use rfind to determine the position of the
#  last occurrence of l in Coding For All People
print(var.find('l'))

# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'
var = "You cannot end a sentence with because because because is a conjunction"

print(var.find('because'))

# Use rindex to find the position of the last occurrence of the 
# word because in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'

print(var.rfind('because'))

'''Happy Learning''' 
