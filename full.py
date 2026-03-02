# # class Animal:
# #     def __init__(self, name,age):
# #         self.name=name
# #         self.age=age
    
# #     def life(self):
# #         print(self.age,"is the lifespawn of ",self.name)
        
# # dog=Animal("dog",11)
# # dog.life()

# # cat=Animal("cat",66)
# # cat.life()


# # class Animal:
# #     def __init__(self,name):
# #         self.name=name
        
# #     def makesound(self):
# #         print(self.name,"makes sound .....")
        
        
# # dog=Animal("dog")
# # dog.makesound()

# # cat=Animal("cat")
# # cat.makesound()

# # class A:
# #     def new(self):
# #         print("hiiiiii")
        
# # class b(A):
# #     def neww(self):
# #         print("hlooooo")
# # class c(b,A):
# #     def last(self):
# #         print("brooooooo")
# # c=c()
# # c.neww()
# # c.new()
# # c.last()


# # class parent:
# #     def add(self):
# #         print("hiiiiiiii")
        
# # class child(parent):
# #     def add(self):
# #         print("broooo")
        
# # class grandchild(child):
# #     def add(self):
# #         print("mmmmmmmmm")
        
# # a=parent()
# # b=child()
# # c=grandchild()
# # a.add()
# # b.add()
# # c.add()

# # class Person:
# #     def __init__(self,name,age):
# #         self.name=name
# #         self.__age=age
# #     def getval(self):
# #         return self.__age 
        
# #     def setter(self,age):
# #         if age > 0:
# #             self.__age=age
# #         else:
# #             print("plese enter valaid ageee")
    

# # c=Person("manhar",21)   
# # print(c.name)
# # print(c.getval())

# # c.setter(8)
# # print(c.getval())


# from abc import ABC,abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def makesound(self):
#         pass
# class Dog(Animal):
#     def makesoun(self):
#         print("hyyy")
        
# c=Dog()
# c.makesoun()
        
# # from abc import ABC,abstractmethod  


# # class Animal(ABC):
# # @abstractmethod
# #     def sound(self):
# #         pass
# # class dog(Animal):
# #     def soun(self):
# #         print("hyyyy")
        
# # c=dog()
# # c.soun()
# # def decor (func):
# #     def wrapper():
# #         text=func()
# #         res=""
# #         for i,x in enumerate(text):
# #             if i%2==0:
# #                 res +=x.upper()
# #             else:
# #                 res +=x.lower()
# #         return res
        
# #     return wrapper
# # @decor
# # def new():
# #     return "good morning"
    
# # print(new())



# # stud={"name":"manhar","age":22}
# # print(stud)
# # print(type(stud))

# # stud["pincode"]=6763011
# # stud.update({"pin":6760232,"plce":"tirurrrrrrrrrrrrrrrrr"})

# # stud.pop("plce")
# # stud.popitem()
# # stud.popitem()
# # print(stud)

# # aa={x:x for x in range(10)if x%2==0}
# # print(aa)


# # for i in stud.items():
# #     print(i)

# # a={1,2,3,4}
# # b={1,2,3,4,5,6,7,8}
# # # a^=b
# # print(a<=(b))

# # a-=b
# # print(a)
# # print(a-b)
# # print(a)
# # print(a)
# # a-=b
# # # # print(a | b)

# # print(a)


# # a=[1,2,3,4,5,6,7,8]
# # square=[x*x for x in a]
# # print(square)
# # # print(list[x for x in a ])

# # aa=[ x for x in range(10)if x%2==0]
# # print(aa)













# # aa=[1,2,3,4,55]
# # square=[x*x for x in aa]
# # print(square)

# # from abc import ABC,abstractmethod

# # class Animal(ABC):
# #     @abstractmethod
# #     def makesound(self):
# #         print("sound makes")
        
# # class dog(Animal):
# #     def makesound(self):
# #         print("make sound")
        
# # d=dog()
# # d.makesound()    


# # txt="manhar gurukkal c k"
# # # print(txt.title())
# # # print("".join(txt))
# # # upper lower capitalize title strip replace
        
# # print(txt.replace(" ",""))
# # # print(txt[::-1])
# # # print(txt.replace("har","HAR"))
# # print(txt[:])


# # def new(n):
# #     if n==0:
# #         return
# #     print(n)
    
# #     new(n-1)
    
# # new(5)
        
# # class Animal():
# #     def __init__(self,name,age):
# #         self.name=name
# #         self.age=age
# #     def sound(self):
# #         print(self.name,"is a animal live" , self.age,"old and make sounds" )
        
        
# # c= Animal("cat",21)  
# # c.sound()

# # d=Animal("dog", 50)
# # d.sound()


# # class Animal:
# #     def __init__(self, weight):
# #         self.weight = weight

# #     def __add__(self, other):
# #         return self.weight + other.weight

# # a1 = Animal(20)
# # a2 = Animal(30)

# # print(a1 + a2)


# # class Animal:
# #     def __init__(self, name):
# #         self.name = name

# #     def __str__(self):
# #         return f"Animal name is {self.name}"

# # a = Animal("Tiger")
# # print(a)
  
        



# class Animal:
#     def __init__(self,weight):
#         self.weight=weight
#     def __init__(self,weight,place=None,old=None):
#         self.weight=weight
#         self.place=place
#         self.old=old
        
#     def __add__(self,other):
#         return self.weight +other.weight
# c=Animal(10,"tirir",45)
# d=Animal(20,"mlp",34)

# print(c+d)


# class Animal:
#     def __init__(self, weight):
#         self.weight = weight
        
        
#     def __add__(self, other):
#         return self.weight + other.weight

# c = Animal(10)
# d = Animal(20)

# print(c + d)


# class Animal():
#     college="abc"#class variable
#     def __init__(self,name):
#         self.name=name # instance variable obj own variable
        
#     def sound(self):
#         print(self.name,"make sound")
#         #local var method uiilil mathram exixt cheyyum
# c=Animal("cat")
# c.sound()
# d=Animal("dog")
# d.sound()


# class Animal():
#     def parent(self):
#         print("iam parent")
        
# class Child(Animal):
#     def child(self):
#         super().parent()
#         print("iam child")
        
# c=Child()
# c.child()
# c.parent()

# class Animal():
#     def sound(self):
#         print("makesoud")
        
# class Dog(Animal):
#     def sound(self):
#         print("bow")
# class Cat(Animal):
#     def sound(self):
#         print("meoww")
        
# def makesound(x):
#     x.sound()

# makesound(Dog())    
# makesound(Cat())    
        
# a=Animal()
# a.sound()
# b=Dog()
# b.sound()
# c=Cat()
# c.sound()
        



# class Child(Child):
#     pass

# class Parent(Child):
#     def m1(self):
#         print("Method 1")

#     def m2(self):
#         print("Method 2")

#     def m3(self):
#         print("Method 3")

#     def m4(self):
#         print(" method 4")
    


# class Child(Parent):
#     # Block the 4th method
#     def m4(self):
#         raise AttributeError("This method is not available for Child class")
#     def c4(self):
#         print("child meth 1")


# p = Parent()
# p.m4()   # 
# p.c4()
# c = Child()
# c.m1()            # 
# c.m4()   # 












