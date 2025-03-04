#print 1-100 numbers
n=int(input("Enter a number:"))
for i in range(1,n+1):
    print(i)
    
Time Complexity-O(n)
----------------------------------------------------------

#sum of first n natural numbers
n=int(input("Enter a number:"))
sum=0
for i in range(1,n+1):
    sum=sum+i
print(sum)

Time Complexity-O(n)
--------------------------------------------------------------

#Approach2
n=int(input("Enter a number:"))
sum=(n*(n+1)/2)
print("Sum of first ",n,"natural numbers is",sum)

Time Complexity-O(1)


----------------------------------------------------------------

#1-50 even using while loop
num=1
while num<=50:
    if num%2==0:
        print(num)
    num+=1

Time Complexity-O(n)

-------------------------------------------------------------------
# Multiplication table of a number
num=int(input("enter a number:"))
i=1
while i<=20:
    print( num,"*",i,"=",num*i)
    i+=1

Time Complexity-O(n)
--------------------------------------------------------------------

#sum of each digit

num=int(input("Enter a number:"))
temp=num
sum=0
while temp>0:
    rem=temp%10
    temp=temp//10
    sum+=rem
print(sum)

Time Complexity-O(logn)

-------------------------------------------------------------------------
#count digits in a number

num=int(input("Enter a number:"))
temp=num
count=0
while temp>0:
    rem=temp%10
    temp=temp//10
    count+=1
print(count)

Time complexity-O(logn)

--------------------------------------------------------------------------
#ask user input until negative number is entered

n=int(input("Enter a number:"))
while n>0:
    n=int(input("Enter a number:"))
    if n<0:
        print("You entered a negative number")


Time complexity-O(n)

------------------------------------------------------------------------

Check a given number is positive, negative, or zero:
num = input("Enter a number")
if num > 0:
    print(num, "is positive")
elif num < 0:
    print(num, "is negative")
else:
    print(num, "is equal to zero")

Time Complexity-O(1)

---------------------------------------------------------------------------

# Determine if a number is odd or even:

num = input("Enter a number")
if num % 2 == 0:
    print(num, "is an even number")
else:
    print(num, "is an odd number")

Time Complexity-O(1)


 --------------------------------------------------------------------------

#  Check if a person is eligible to vote (age>=18):

age = input("Enter the age")
result = "Eligible to vote" if age>=18 else "Not Eligible to vote"
print(result)

Time Complexity-O(1)

 ----------------------------------------------------------------------------------

# find the greatest of two numbers

num1 = input("Enter first number")
num2 = input("Enter second number")
result = "num1 is greater" if num1>num2 else "num2 is greater"
print(result)

Time Complexity-O(1)


 ----------------------------------------------------------------------------------

#  print pass if a student scores more than 40 marks. Otherwise, print "Fail":

marks = input("Enter the marks")
if marks>'40':
    print("Pass")
else:
    print("Fail")

Time Complexity-O(1)


----------------------------------------------------------------------------------

#  Write a program to display the day of the week based on a number input (1 for Monday, 2 for Tuesday etc)

number = input("Enter a number")
if number == '1':
    print("Monday")
elif number == '2':
    print("Tuesday")
elif number == '3':
    print("Wednesday")
elif number == '4':
    print("Thursday")
elif number == '5':
    print("Friday")
elif number == '6':
    print("Saturday")
elif number == '7':
    print("Sunday")
else:
    print("Not valid")
    
Time Complexity-O(1)

----------------------------------------------------------------------------------

#  Implement a simple calculator to perform addition, subtraction, multiplication, and division:

num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))
inp = input("Enter an operation").lower()
if inp in ['add', '+']:
    print(num1+num2)
elif inp in ['sub', '-']:
    print(num1-num2)
elif inp in ['mul', '*']:
    print(num1*num2)
elif inp in ['div', '/']:
    if num2 == 0:
        print("Div with 0 is not possible")
    else:
        print(num1/num2)
else:
    print("Invalid Input")

Time Complexity-O(1)

 ----------------------------------------------------------------------------------

# program to display the name of a month based on the month number:

month = int(input("Enter a number"))
if month == 1:
    print("January")
elif month == 2:
    print("February")
elif month == 3:
    print("March")
elif month == 4:
    print("April")
elif month == 5:
    print("May")
elif month == 6:
    print("June")
elif month == 7:
    print("July")
elif month == 8:
    print("August")
elif month == 9:
    print("September")
elif month == 10:
    print("October")
elif month == 11:
    print("November")
elif month == 12:
    print("December")

Time Complexity-O(1)

----------------------------------------------------------------------------------

#  Write a program to find the greatest of three numbers:

num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
num3 = int(input("Enter third number"))
if num1 > num2 and num1 > num3:
    print(num1, "is greater number")
elif num2>num1 and num2 > num3:
    print(num2, "is greater number")
elif num3 > num1 and num3 > num2:
    print(num3, "is greater")
else:
    print("All three are equal numbers")

Time Complexity-O(1)

----------------------------------------------------------------------------------

#  check if a year is leap or not:

year = int(input("Enter a year"))
if ((year % 4 == 0) and (year % 100 != 0)) or ((year % 400 == 0) and (year % 100 == 0)):
    print("Leap Year")
else:
    print("Not a Leap year")
Time Complexity-O(1)

 ----------------------------------------------------------------------------------

#   classify a character entered by the user as a vowel, consonant, or neither:

def alphabet(char):
    vowels = "aeiouAEIOU"
    if char.isalpha():
        if char in vowels:
            return "Vowel"
        else:
            return "Consonant"
    else:
        return "neither"
    
char = input("Enter a single character")
if len(char) == 1:
    result =alphabet(char)
    print(result)
else:
    print("Enter single character only")
Time Complexity:-O(1)

----------------------------------------------------------------------------------

#  grade of a student based on the marks they score:

marks = int(input("Enter marks"))
if marks >= 90 and marks <=100:
    print("Grade A")
elif marks >= 80 and marks <=89:
    print("Grade B")
elif marks >= 70 and marks <=79:
    print("Grade C")
elif marks < 70:
    print("Fail")
else:
    print("Not a number")
    
Time Complexity-O(1)


 ----------------------------------------------------------------------------------

#  Write a program to check if three sides length form a valid triangle:

a = int(input("Enter the length of side 1: "))
b = int(input("Enter the length of side 2: "))
c = int(input("Enter the length of side 3: "))
if (a+b) > c and (b+c) > a and (a+c) > b:
    print("It will form a valid triangle")
else:
    print("It will not form a valid triangle")

Time Complexity-O(1)











