#Q1. =  program for swap two number 
#def swap_num(a,b):
#    print("value of a :",a)
#    print("value of b :",b)
#    temp =  a
#    a = b
#    b = temp
#    print("value of a :",a)
#    print("value of b :",b)
#swap_num(10,20)

#Q 10 = program for multiplication table of a given number
#for i in range(1,11):
#   print(a,"x",i,"=",n*i)

#tablenum = int(input("multiplication table")) 
#for i in range(1,11):
#    a = tablenum*i
#    print(tablenum," * ",i,"=", a)

#Q3 = program to findsum of all elenents in the list
#l =  [100,300,855,9595]
#total = 0
#for i in l :
#    total += i
#print(total)
#output= 10850

#Q 5 = program for implement simple calculator
#n1 = int(input("enter first number :"))
#n2 = int (input("enter second number :"))

#def addition(a,b):
#    print("addition:", a + b )     
#addition(n1,n2)

#def substraction(a,b):
#    print("substraction:", a - b )     
#substraction(n1,n2)

#def multiplication(a,b):
#    print("multiplication:", a * b )     
#multiplication(n1,n2)

#def division(a,b):
#    print("division:", a / b )     
#division(n1,n2)

#Q 7 = python function to count the occurance of character in a string
#args = *s
#kwargs = **l

#s = "hello world"
#def count(*s,**l):
#    ***this function is about count the occurance of letter "l" in "hello world".
#    return s.count("l")
#print(count("l"))
#output = 1

#Q6 = to reverse a given string
s = "hello"
r = reverse(s)
#print(s[::-1])  
# Output: olleh
def reverse(s):
    return(s[::-1])
print(f"Original: {s}")
print(f"reverse: {r}")

#Q2 = program for to check given number is prime.
#n = int(input("Enter a number: "))
#if n > 1:
#	for i in range(2, int(n/2)+1):
#		if (n % i) == 0:
#			print(n, "is not a prime number")
#	else:
#		print(n, "is a prime number")   

#Q4 Python program to check if a string is a palindrome 
#s = "Python" = no
#s = "madam"  = yes
#if s == s[::-1]:
#    print("Yes")
#else:
#    print("No")

#Q 8 write a python program to calculate simple intrest
#principal = int(input("Enter the principal amount (rs):"))
#rate = int(input("Enter the interest rate (%): "))
#time = int(input("Enter the time (years): "))

#si = (principal * rate * time) / 100

#print("Simple Interest:", si)

#Q9 write python program to check if a number is divisible by 5 and 11
#n = int(input("Enter a number : "))
#if n % 5 == 0 and n % 11== 0:
#   print(" divisible by both 5 and 11:", n)
#else:
#  print("  not divisible by both 5 and 11:", n)