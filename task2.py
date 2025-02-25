  #Check given number is Prime or not
n=int(input("enter a number"))
prime=True
if n==0 or n==1:
    print("either prime nor composite")
elif n>1:
   for i in range(2,n):
     if n%i==0:
        prime=False
        break
   if prime:
    print("it is a prime number")
   else:
    print("not prime")




#Factorial of a given number
n=int(input("enter a number:"))
i=1
while n>0:
    i=i*n
    n=n-1
print(i)




#Number divisible by 3 and 5
n=int(input("enter a number:"))
if n==0:
    print("zero error")
for i in range(1,n+1):
    if i%3==0 or i%5==0:
        print(i)
      



