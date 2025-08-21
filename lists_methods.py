#l = [12,23.4,"string", True, 2,3,4]
#print(l)
#print(l + 1) = add only list not integer print(l + [1])
#print(l*2) = it multiple the each valuein the list
#print(type(l)) = class 'list'
#print(l[0]) = 12 index is available 
#slicing
#l[start: end : step]
#print(l[0:5]) = [ 12 - 2 index output]
#print(l[ : :-1]) = the indexing of umbers will reverse in direction.

#s ="python"
#print(list(s)) = p,y,t,h,o,n is the outpur string can be convert into list

#s= (2,3,54,2,4)
#print(list(s)) = [2,3,4,54] = set can be convert into list
#print(list(s)) = [2,3,54,2,4] = tupple also into list
#s={"name": "john"}
#print(list(s)) = ['name'] = dictionary into list

#s = 100
#print(list(s)) = integer is not iterable in list

#lists methods
#1. replace method
#l = [10,30,29,40,59]
#l[3] = 100 = [10,30,29,100,59] = the 3 rd position got replaced by 100 

#insert method
#l.insert(3, 100)= 100 value is get add at 3 rd position and 40 will shift

#append method
#l.append(200)= if you want to add value at the end of the list use this method
#l.append(100,300) = it only can add only one.

#extend method = it can add multiple number byt giving value in the another list
#s= (100,399,500)
#l.extend(s)

#index method
#print(l.index(40)) = 3 it gives the index of the value

#pop method = it always remove last element from the list
#l.pop()

#remove method - to remove given value from the list
#l.remove(10)

#delete method = to delete the index value from the list
#del l[2]

#reverse method - to reverse complete list
#l.reverse()

#sort method 
#l.sort() - it sort in ascending order
#l.sort(reverse=True) = to shift in decending order

#l = [ 10,30,20,45]

#max/min method
#print(max(l)) = error str and int cannot be support to find maximum value
#print(max(l)) = 45
#print(min(l)) = 10

#l = ["Python", "apple", "Zebra", "Add", "Good"]
#print(max(l)) = apple
#print(min(l)) = add 
#ASqi code = it has the serial number for a-z in numbers for string to convert words into numbers

#copy method
#l1 = l.copy()
#print(l)
#print(l1)

#add method
#l1 = [1,2,3]
#l2= [4,5,6]
#l3 = [7,8,9]

#l4 = l1+l2+l3 = it store in the one list
#l4=[l1,l2,l3] = it store in the nested list with bracket in the one list

#l4=[l1,l2,l3]
#a = l4[1]
#print(a[2]) = 6

#print(l4[1][2]) = 6 output in the list intonested from.
#clear method = to clear all the value
#l4.clear()
#print(l4)




