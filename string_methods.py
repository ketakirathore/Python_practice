# string  the length of the value store in the variables it calculate the whole length including space as 1.
#s = "hello world" = 11 
#print(len(s)) =11

#print(s+1)= error
#In string, the addition required bot double quoted values.
#string value + integer= error
#"1"+ "1"=2

#print(s*1)= hello world
#in multiplicaton, it multiply the given value.

#Indexing- position of your alphabet in the given values 
#s = "python is easy to learn"
#positive indexing - starts from 0 position from left to right
#negative indexing - starts from -1 position from right to left
#print(s[index number of position of alphabet])
#print(s[1])= p

#*Slicing- portion of the whole value store in variables.
#it perform by help with indexing
#print(s[start:end])
#start- starting position of the sentence alphabet
#end - stop on the positon of the alphabet
#print(s[0:5])= pytho
#0 = start 6= end
#it gives all the elements mentioned in the given range= pytho but it doesnt consider the end value it will shown 
#previous value.
#print(s[:6])= it start with 0 by default
#print(s[:])= it gives the all value mention in the variables.
#print(len(s))=23
#print(s[-4:-1])= the direction should be left to right = ear dont count the last index.

# s[start:end:step]
#print(s[0:8:1])= python i
#print(s[0:8:2])= pto  it calculate the step of 2 values in the sentence 0=p step2= ulteranate text 
#step= jump on the positon on text

#strip method is use for removig space in the value.

#s.rstrip= right side space removig
#s.lstrip = left side space removig

#input function = always data type is string. data mention should be string only
#s = input("enter your age :") = the result in the terminal give the senntence where you have to add the data ans save.
#r = int(s) = to convert the data from string to integer.
#print(type(r))= by result it convert the data type to integer
#print(r + 20) = in terminal we have save age 21 and add 20 it gives 41.

#s = float(input("enter your age :")) = to convert the data by direct method
#print(type(s))
#print(s + 20)


#Find method = to find value from given data
#s="pythondatapythondata"
#print(s.find("ata")) = 7 index answer represents the position of 'ata'
#print(s.find("p")) = 0 is gives the positon of p
#print(s.count("ata")) = 2 it gives the count of value in the data.

#s="python data python data"
#split method = to split every word of sentence.
#print(s.split(" "))= ['python', 'data','python', 'data'] = list data type result came in outcome

#s = "python is hard to learn"
#result = s.replace("hard", "easy") = python is easy to learn
#replace method = isused for replace some data from given data.
#print(result)

#s = "python is hard to learn python is hard to learn python is hard to learn"
#n = 'easy'
#result = s.replace("hard", n, 1)= it change only change the first sentence.
#print(result)

#t = ("c", "c++", "python","hello")
#s = "world".join(t)= join method to use join every value in a single value.
#print(s)

#s = "Hello world...."
#print(s.upper()) = It change the text into upper case
#print(s.lower()) = It change the text into lower case
#print(s.title()) =  it change the first letter of every word into upper case
#print(s.capitalize()) = it change first letter of each sentence into  capital case
#print(s.swapcase()) = interchange the lower case to upper case


#center method = it positioned the given value into center where you have to provide the width/length inthe formula
#s = "python"
#print(len(s)))
#r = s.center(20,"*") = 20 is length and "*"= it shows the position of the value
#print(r)
#print(len(r))

#is method= output is always in boolean which is true or false
#s = "Learning"
#print(s.isalpha()) = if the alphabets (a-z) is include in the text or not
#print(s.islower())/ print(s.isupper()) = if the lower/upper case is include all text
#print(s.isalnum()) = if the alphate and number include in the tex 
#print(s.isspace()) = if space is mentioned in the text or not required entire empty string
#print(s.title()) = first letter is capital or not
#print(s.isdigit()) = only number mentioned in the string or not

#membership operator in or not in = output always in true/false
#s= "Hello world"
#print("H" not in s) = to check the given value in string
#print(s.startswith("H")) = to check does the sentece starts with the given value.
#print(s.endswith("world")) = to check weather the sentece ends with given value.
#print(s.index("l")) = to check the index value or length for a given value always give the first appearance value.
#this method is use while we login intosome portal
#ex Gmail- (.com, .in) and username,password(captal letter, symbols)