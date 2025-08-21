  #to connect methods and class "self" parameter is used.
#class myclass :
#    def msg(self):
#        print("this is my first class")
#    def hello (self):
#        print("hello")
#m = myclass()
#m.msg()
#m.hello()

#without object class output wontshowup
#__init__
#class user :
#    def __init__(self,name,age):
#        self.name= name
#        self.age = age
        
#    def info(self):
#        print("my name is :", self.name)
#        print("my age is :", self.age)
#u = user("john", 21)        
#u.info()


#polymorphism - where *  has differant meaning in every structure.
#from random import *
#print(10*3)

#class cat:
#    def __init__(self, name):
 #       self.name = name
 #   def display (self):
  #      print("name of the cat :", self.name)
#c = cat("kitty")    

#class dog :
#    def __init__(self,name):
#        self.name = name
#    def display (self):
#        print("name of the dog:", self.name)    
#d = dog("sheru")

#def output(a):
#    a.display()
#output(c)    
#output(d)

# single inheritance(a)

#class Employee :
#    def __init__(self,name,age):
#        self.name = name
#        self.age = age

#   def display(self):
#        print("name of the employee :", self.name)
 #       print("age of the employee :", self.age)

#e =  Employee("john", 21) 
#e.display    
    
# multiple inheritance (b)
#class trainer(Employee) :
#    def __init__(self,name,age,role):
#        Employee.__init__ (self,name,age)
#        self.role = role

#    def display(self):
#        Employee.display(self)
#        print("role of the trainer is :", self.role)  
#t = trainer("john", 34, "trainer")
#t.display()
            
#multilevel inheritance
#class manager(trainer):
#    def __init__(self, name, age, role, salary):
#        trainer.__init__(self ,name,age,role)
#        self.salary = salary
#    def display(self):
#        print("salary of manager :", self.salary)
#        return super().display()    
    
#m = manager("john", 32, "manager", 34000) 
#m.display()   

#heirarchial inheritance :
#class father:
#    def __init__(self,eyes,hair):
#        self.eyes = eyes
#        self.hair = hair

#    def info(self):
#        print("eyes of father is :", self.eyes)
#        print("hairstyle of father :", self,hair)   

#class mother:
#    def __init__(self, height):
#        self.height = height
#    def info(self):
#        print("height of mother :", self.height)
        
#class son(father,mother):
#    def __init__(self, eyes, hair, height, talent):
#        father.__init__(self,eyes, hair)
#        mother. __init__(self,height)
#        self.name = name
#        self.talent= talent

#    def info(self):
#        father.info(self)
#        mother.info(self)
#        print("name of the son is :", self.name)
#        print("iq of the son :", self.talent)

#s = son("john", "brown", "curly","tall",250)
#s.info()

#multilevel inheritance
#class pet:
#    def __init__(self, pet_type,name):
#        self.pet_type = pet_type
#        self.name = name
#    def details(self):
#        print("i am pet")

#class cat (pet):
#    def __init__(self, pet_type, name, age):
#        super().__init__(pet_type, name)    
#        self.age = age    
#    def details(self):
#        print("i am ", self.pet_type)
#        return super().details()    

#class dog(pet):
#    def __init__(self, pet_type, name, bdate):
#        super().__init__(pet_type, name)
#        self.bdate = bdate
#    def details(self):
#        print("bday of dog is:", self.bdate)
#        return super().details()    

#c = cat ("cat", "kitty", 1)
#c.details()

#d = dog("dog","sheru",2)
#d.details()

#encapsulation

#class bank:
#    def __init__(self,name, acc_no, balance):
#        self.name= name
#        self.acc_no = acc_no
#        print("name :", self.name)
#        print("accoun no. : ", self.acc_no)
#        print("balace :", self.__balance)

#    def withdrawl(self,amt):
#        self.__balance -= amt   
#    def deposite(self,amt):
#        self.__balance += amt

#    def update_balance(self):
#        print("updated balance:", self.__balance)   
#b = bank("john", 12345,5000)
#b.info()
#b.balance =5
#b.info()
#b.deposite(2000)
#b.withdrawl(2000)
#b.update_balance()

# encapsulation = to provide security to data
#class encap :
#    def __init__ (self,a):
#        self.__a = a
#    def display(self):
#        print("value of a is :", self.__a)
#        print("id of a is :",id(self.__a))
#e = encap(10)
#e.display() 
#e.a = 25
#e.display()  


#abstraction = need to import = to hide theprocess use @abstractmethod = is called decorator
#decorator use when you need such process again and again to store in the methods

from abc import ABC, abstractmethod

class vehical(ABC):
    def __init__(self,brand,model,fuel_type):
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    def details(self):
        return f"{self.brand}{self.model} - fuel type : {self.fuel_type}"    
#f"{variable}"= formating string    
class car (vehical):
    def start_engine(self):
        print(f"{self.brand}{self.model} car engine has started")   

    def stop_engine(self):
        print(f"{self.brand}{self.model} car engine has stopped")    

class bike (vehical):
    def start_engine(self):
        print(f"{self.brand}{self.model} bike engine has started")   

    def stop_engine(self):
        print(f"{self.brand}{self.model} bike engine has stopped")    

c = car ("toyota", "cmary","petrol")
b = bike("bmw", "cmary","petrol")

print(c.details())
c.start_engine()
c.stop_engine()
print(b.details())
b.start_engine()
b.stop_engine()

