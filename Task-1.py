'''
Problem Statement: Write a Python program that does the following:
1.  Takes two numbers as input from the user.
2.  Performs the basic mathematical operations on these two
numbers:
o Addition
o Subtraction
o Multiplication
o Division

3.  Displays the results of each operation on the screen.
'''

f= input("Enter the first number: ")
s = input("Enter the second number: ")
f = int(f)
s = int(s)
Addition = f + s
Subtraction = f - s
Multiplication = f * s
Division = f / s
print('Addition: ', Addition)
print('Subtraction: ', Subtraction)
print('Multiplication: ', Multiplication)
print('Division: ', Division)
