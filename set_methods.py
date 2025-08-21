
#s = {10, 2 , 4, 3, 5, 2, "Hello", 34.5,}
#print(s) = it ouput the entire set in the change of sequence and without duplicate numbers
#print(s[0])= output as error cause indexing is not awailable in set.

#add method
#s.add(400) = it adds the given value in the set
#print(s)
#s.add(20,30,40) = set add takes exactly one argument( 3 given)= it can strictly add only one value
#you cannot include set in another set

#to add multiple elements.= only tupple
#s1 =(10,20,30,40,50)
#s.add(s1)

#update method
#s.update(s1) = to get value in multiple numberswithout brackt include.it canadd set list tupple format
#print(s)

#d = {"key":"value"} = in dictionary format only add first letter that is key not values.
#s.update(d)

#d = ["Google"]
#s.update(d)= for string the word get count as separate element
#s.update(d) = for add the entire word as one you need put the value into squate bracket
#print(s)


#17/7/25
#copy method
#s = {10, 2 , 4, 3, 5, 2, "Hello", 34.5,}
#print(s)
#s1 = s.copy()
#print(s1)

#pop method
#s.pop() = remove the first element after the output print in the terminal
#print(s)

#remove method - to remove perticular element
#s.remove(34.5)

#discard method -  to discard the action
#s.discard(100)
#print(s)

#clear method - to remove all the elemets
#s.clear()
#print(s)

#s = {"name":"john", }
#r = set(s)
#print(r)

#s = {10,30,30,4,5,6}
#s1 = {1,2,30,4,7,8,10,5,6}

#print(s.intersection(s1)) = {4,30} = common elements 
#print(s.union(s1)) = {1,2,4,5,6,7,8,10,30}

#print(s.symmetric_difference(s1)) = {1,2,5,6,7,8,10}
#print(s1.difference(s)) = {8,1,2,7} = differant element in both set
#print(s.issubset(s1)) = false to check the element present from s in s1

