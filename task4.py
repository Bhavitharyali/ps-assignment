#print 1-100 numbers
'''n=int(input("Enter a number:"))
for i in range(1,n+1):
    print(i)'''
    
'''Time Complexity-O(n)
----------------------------------------------------------'''

'''#sum of first n natural numbers
n=int(input("Enter a number:"))
sum=0
for i in range(1,n+1):
    sum=sum+i
print(sum)

Time Complexity-O(n)
--------------------------------------------------------------
'''
'''#Approach2
n=int(input("Enter a number:"))
sum=(n*(n+1)/2)
print("Sum of first ",n,"natural numbers is",sum)

Time Complexity-O(1)
'''

'''----------------------------------------------------------------'''

num = 2
while num <= 50:
  print(num)
  num+=2
