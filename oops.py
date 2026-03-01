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

class person:
    def __init__(self,name,age):
        self.name=name
        self.__age=age
        
    def getvalue(self):
        return self.__age
        
    def setter(self, age):
        if age>0:
            self.__age=age
        else:
            print("enter valied num")
        
        
c=person("manhar",21)

print(c.name)
print(c.getvalue())
c.setter(0)
print(c.getvalue())
# print(c._person__age)
a=person("nabeeel",55) 
 
print(a.name)
print(a.getvalue())
a.setter(5)
print(a.getvalue())

    



class Person:
    def __init__(self,name,age):
        self.name=name
        self.__age=age
    def getval(self):
        return self.__age
        
    def setter(self,age):
        if age > 0:                     #encapsul
            self.__age=age
        else:
            print("plese enter valaid ageee")
    

c=Person("manhar",21)   
print(c.name)
print(c.getval())

c.setter(8)
print(c.getval())
