import task
print(task.stud["stud1"])
# def decor(func):
#     def style():
#         res=""
#         text=func()
#         for i, x in enumerate(text):
#             if i%2==0:
#                 res+=x.upper()
#             else:
#                 res+=x.lower()
#         return res
       
#     return style
        


# @decor
# def new():
#     return "good morning"
# print(new())



# class Student:

#     school = "GHSS Calicut"   #  Class Variable

#     def __init__(self, name, mark):
#         self.name = name      #  Instance Variable
#         self.mark = mark      #  Instance Variable

#     def display(self):
#         grade = "Pass"        #  Local Variable
#         print(self.name, self.mark, grade, Student.school)


# s1 = Student("Manhar", 90)
# s2 = Student("Rahul", 75)

# s1.display()
# s2.display()


# class Dog:
#     def sound(self):
#         print("Bark")

# class Cat:
#     def sound(self):
#         print("Meow")

# def make_sound(animal):
#     animal.sound()   # Duck typing

# d = Dog()
# c = Cat()

# make_sound(d)
# make_sound(c)


# lst=[1,3,4,5,6,9,8,5]

# a=filter(lambda x:x%2==0,lst)
# print(tuple(a))

# b=map(lambda x:x*5,lst)
# print(list(b))

# from functools import reduce

# c=reduce(lambda a,b:a+b,lst)
# print(c)
 

# age=21
# txt=f"the age of nabbeel {age} year oldddd"
# print(txt)

# name=(input("enter your age:"))
# print (f"your age is {name} is it correct ")

# def decor(func):
#     def edit():
#         text=func()
#         # print(text)
#         print(len(text))
#         return text
        
#     return edit
# @decor
# def one():
#     return "hello"
# print(one())
# text="manharrrrgrrurkkal"
# for i,x in enumerate(text):
#     print(i,x)

# lst=[1,2,3,4,5,6,"manhar","aa"]
# for i, x in enumerate(lst,start=1):
#     print(i,x)

# class Animal():
#     def __init__(self, name):
#         self.name=name
        
#     def makesound(self):
#         print(self.name,"making soundd")
        
# dog=Animal("dog")
# dog.makesound()

# cat=Animal("cat")
# cat.makesound()


a=min(12,2,45)
print(a)
ab=abs(-7.54)
print(ab)

x=pow(3,5)
print(x)



import math 
x=math.sqrt(25)  
print(x).math.ceil()   
    

# def decor(func):
#     def new(x):
#         return func(x.upper())
       
#     return new
         

# @decor
# def new(name):
#   return "my name is:-"+ name
# print(new("manhar"))

def decor(func):
    def inner():
        text=func() 
        res=""
        for x in text:
            if x in "aeiou":
                res+="*"
            else:
                res+=x.lower()
        return res
    return inner
        
@decor
def hy():
    return "goood morning"
    
print(hy())


def new(n):
    if n==0:
        print("completed")
        return
    print(n)
    
    new(n-1)
   
    
new(5)


a=[x for x in range(5)]
print(a)















