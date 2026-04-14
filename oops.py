# class Animal:
#     def __init__(self, name,age):
#         self.name=name
#         self.age=age
    
#     def life(self):
#         print(self.age,"is the lifespawn of ",self.name)
        
# dog=Animal("dog",11)
# dog.life()

# cat=Animal("cat",66)
# cat.life()


# class Animal:
#     def __init__(self,name):
#         self.name=name
        
#     def makesound(self):
#         print(self.name,"makes sound .....")
        
        
# dog=Animal("dog")
# dog.makesound()

# cat=Animal("cat")
# cat.makesound()

# class A:
#     def new(self):
#         print("hiiiiii")
        
# class b(A):
#     def neww(self):
#         print("hlooooo")
# class c(b,A):
#     def last(self):
#         print("brooooooo")
# c=c()
# c.neww()
# c.new()
# c.last()


# class parent:
#     def add(self):
#         print("hiiiiiiii")
        
# class child(parent):
#     def add(self):
#         print("broooo")
        
# class grandchild(child):
#     def add(self):
#         print("mmmmmmmmm")
        
# a=parent()
# b=child()
# c=grandchild()
# a.add()
# b.add()
# c.add()

# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.__age=age
        
#     def getvalue(self):
#         return self.__age
        
#     def setter(self, age):
#         if age>0:
#             self.__age=age
#         else:
#             print("enter valied num")
        
        
# c=person("manhar",21)

# print(c.name)
# print(c.getvalue())
# c.setter(0)
# print(c.getvalue())
# # print(c._person__age)
# a=person("nabeeel",55) 
 
# print(a.name)
# print(a.getvalue())
# a.setter(5)
# print(a.getvalue())











# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.__age=age

#     def get(self):
#         return self.__age
    
#     def setter(self,age):
#         if age > 0:
#             self.__age=age

# c=Person("manhar",22)
# print(c.name)
# print(c.get())
# c.setter(8)
# print(c.get())





# print(list(zip(a,b)))
# res={k,v for k,v in zip(keys,values)}

# class Animal():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
        
#     def namee(self):
#         print(self.name,"is aa  animal ",self.age,"yearlive")
    
# a=Animal("dog",10)
# a.namee()
    
# class Animal:
#     def animall(self):
#         print("makesound")
        
# class Dog(Animal):
#     def sound(self):
#         print("dog make osund")
#     def old(self):
#         print("dog live 20 year")
        
# c=Dog()
# c.sound()
# c.old()
# c.animall()

# from abc import ABC,abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass
# class Dog(Animal):
#     def sound(self):
#         print("dog barks")
        
# c=Dog()
# c.sound()
    
# class Person():
#     def __init__(self,name,age):
#         self.name=name
#         self.__age=age
        
#     # def get(self):
#     #     return self.__age
        
# c=Person("manhar",22)
# print(c._Person__age)
# # print(c.get())




def decor():
    return "hello worldd"
print(decor())



















    



# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.__age=age
#     def getval(self):
#         return self.__age
        
#     def setter(self,age):
#         if age > 0:                     #encapsul
#             self.__age=age
#         else:
#             print("plese enter valaid ageee")
    

# c=Person("manhar",21)   
# print(c.name)
# # print(c._Person__age)#name mangling
# print(c.getval())

# c.setter(8)
# print(c.getval())


# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
