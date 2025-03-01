#square or cube of a number

num=input("Enter power of a number:").lower()
while True:
    if num=="2" or num=="square":
        base=int(input("Enter a number:"))
        print("Square of a number:",base**2)
    elif num=="3" or num=="cube":
        base=int(input("Enter a number:"))
        print("Cube of a number:",base**3)
    elif num=="exit":
        print("Exited successfully")
        break
    else:
        print("invalid input")
    num=input("Enter power of a number:")
  --------------------------------------------------------------------

#palindrome

text=input("Enter a string:")
b=""
for i in text:
    b=i+b
if text==b:
    print(text,"is a palindrome")
else:
    print(text,"is not a palindrome")
------------------------------------------------------------------


#perfect number
n=int(input("enter a number: "))
sum=0
for i in range(1,n):
    if n%i==0:
        sum=sum+i
if n==sum:
    print("perfect number")
else:
    print("not perfect number")


------------------------------------------------------------------
#GCD
a=int(input("enter a number:"))
b=int(input("enter a number:"))
while b:
    temp=a%b
    a=b
    b=temp
gcd=a
print("gcd of a number:",gcd

--------------------------------------------------------------------

# LCM 
x = int(input("Enter the first number:"))
y = int(input("Enter the second number"))
if x > y:
    big = x
else:
    big = y
while True:
    if (big % x == 0) and (big % y == 0):
        LCM = big
        break
    big = big + 1
print("LCM of two numbers is:", LCM)

---------------------------------------------------------------------


#Palindrome Number

num = int(input("Enter a number to check palindrome or not"))
temp = num
rev = 0
while num > 0:
    rem = num % 10
    rev = rev * 10 + rem
    num = num // 10

if temp == rev:
    print("It is a Palindrome Number")
else:
    print("It is not a Palindrome Number")












