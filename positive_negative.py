# Python Program to Check if a Number is Positive, Negative or 0

# In this example, you will learn to check whether a number entered by the user is positive, negative or zero. 
# This problem is solved using if...elif...else and nested if...else statement.

# Source Code: Using if...elif...else
num = float(input("Enter a number: "))
if num > 0:
   print("Positive number")
elif num == 0:
   print("Zero")
else:
   print("Negative number")

    
# Source Code: Using Nested if
num = float(input("Enter a number: "))
if num >= 0:
   if num == 0:
       print("Zero")
   else:
       print("Positive number")
else:
   print("Negative number")
