#john =  [ 500,1500,4000,3000]
#max = [4000,300,2003,5000]

#total_expense = 0
#for i in john :
#    total_expense += i
#print(total_expense)= 9000

#total_expense = 0
#for i in max :
#    total_expense += i
#print(total_expense)  = 11303  

#to create the block for repeted code use function
#1. function defination - first line if syntax to define function
#2. function execution - utput of the function
#3. function calling - to get output compulsory call the function
#def - define

#function syntax
#def function_name() :
#    line of execution
#function_name()    
# for running the same code we use function
# you can call your function as many times you need buut it is compulsory to callyour function

#def msg():
#    print("Hello world...")
#msg()  = Hello world...

#print(type(msg)) = type function

#def add():
#    """this function will return in addition"""  = dockstring (instruction for function for future ref)
#    print(10+20)
#add()    = 30

# a and b are the parameter
#arguments value should be in call statement.
#n = int(input("enter first no:"))
#def add(a,b):
#    print(a+b)
#add(10,20) = 30 a = 10, b=20

# function with return = the result come in return format in function name
#def hello(a,b,c,d):
#    return a,b,c,d
#print (hello(10,20,30,40)) = output in tuple (10,20,30,40)


 # function for even and odd numbers
#even_list = []
#odd_list = []
#def evenodd(*a):
#    for i in a :
#        if i % 2 == 0 :
#            even_list.append(i)
#        else :
#            odd_list.append(i)   
#    print(even_list)
#    print(odd_list)
#evenodd(20,30,23,45,32)   




#*args = *multiple arguments
#**kwargs = keyword argument, ** key value pair b="hello"

#def addlist(*a):
#    return a
#print(addlist(10,20,30,40,50)) to store multiple in number in single parameter

#def addlist(*a):
#    l =[]
#    for i in a :
#        l.append(i)
#    return l
#print (addlist(10,20,40,56,48))  = [10,20,40,50,48]  = output in list format

#def test(*a,**b):
#    print(b)
#    print(a)
#test(1,2,4,7,b= "hello")    = (1,2,4,7)= tuple  {'b': 'hello'}= dict

#b = 20 = global variable can use within the function and outside the function
#def msg():
#    a = 10 = local variable outside the function
#    print(a)
#    print (b)
#msg()



#annonymouse function - without name
#lambda - single condition

#def add(a,b):
#    print(a+b)
#add (10,30)    

#x = lambda a, b:a+b
#print(x(10,30)) = 40

#list comprehension
#t = (1,2,3,4,5)
#l =[]
#for i in t :
#    l.append(i)
#print(l)
#= [1,2,3,4,5]= converted into llist

#result = [i for i in t]
#print (result)

#def swap_num(a,b):
#    print("value of a :",a)
#    print("value of b :",b)
#    temp =  a
#    a = b
#    b = temp
#    print("value of a :",a)
#    print("value of b :",b)
#swap_num(10,20)
