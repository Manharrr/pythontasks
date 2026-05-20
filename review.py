txt="Bridgeon's AI Notetaker"

# txt.""join()
# print(txt.replace(" ","_"))
# print(txt)

# class A:
#     def show(self):
#         print("A")
# class B(A):
#     pass
# a=B()
# a.show()

# class A:
#     def show(self):
#         print("A")
# class B(A):
#     def one(self):
#         print("b")
# class C(B):
#     def two(self):
#         print("c")
# a=C()
# a.show()
# a.one()


# class A:
#     def show(self):
#         print("A")
# class B:
#     def one(self):
#         print("b")
# class C(A,B):
#     pass

# a=C()
# a.show()




# class A:
#     def show(self):
#         print("A")
# class B(A):
#     def one(self):
#         print("b")
# class C(A):
#     pass

# a=C()
# a.show()


# class A:
#     def show(self):
#         print("A")
# class B(A):
#     def one(self):
#         print("b")
# class C(A):
#     pass

# class D(B,C):
#     pass

# d=D()
# d.show()

# lst=[1,2,3,4,5,6,7,8,9,10] 

# fil=filter(lambda X :X%2==0,lst)
# print(list(fil))

# def new(name,age):
#     print(f"my name {name}and old i{age}") 
# new(name="manhar",age=22)

# class Test:
#     def __init__(self):
#         self.x = []

# a = Test()
# b = Test()

# a.x.append(1)

# print(a.x, b.x)



def decor(func):
    def wrapper():
        return func().upper()
    return wrapper
        
@decor
def new():
    return "good afternoon"
print(new())

def one ():
    print("This code defines a class Employee with a class variable raise_amount")
    

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


def new(name,age):
    print(f"my name {name}and old i{age}") 
new(name="manhar",age=22)

class Test:
    def __init__(self):
        self.x = []

