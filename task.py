# a=("a","b")
# print(a)

# a=[1,2]

# print(1 in a)


# a="hello"

# b=a
# c="hello"
# print(a==c)
# print('b' in "sad")
# print('-------------------')
# print(a is b)
# print(a is c)

# a=[1,2,3]

# b=a
# c=[1,2,3]

# print(a is c)
# print(a==c)



# def new():
#     yield 1
#     yield 2

# g=new()

# print(next(g))
# print(next(g))



# stud={
#    "stud1":{ "name":"manhar"},
#    "stud2":{"name":"adhil","sasd":2},
#    "stud3":{"name":"arun"}
# }
# print(stud["stud2"]["sasd"])
# for key in stud:
#        print(key)


# def decorator(func):
#     def one(a,b):
#         return func(a,b)
#     return one
        
# @decorator
# def new(x,y):

# aa=(1,)
# print(type(aa))







aa=[1,2,[2,3,[4,5,6,[7,8,9]]]]
# print(aa)

# print(aa[-1][-1][-1][1])

    
#--------------------------------------------------------------------------------------------------


# students = {
#     "s1": {
#         "name": "Manhar", 
#         "age": 21,
#         "marks": {
#             "python": 85,
#             "sql": 78,
#             "ml": 90
#         }
#     },
#     "s2": {
#         "name": "Akhil",
#         "age": 22,
#         "marks": {
#             "python": 88,
#             "sql": 82,
#             "ml": 75
#         }
#     },
#     "s3": {
#         "name": "Rahul",
#         "age": 20,
#         "marks": {
#             "python": 70,
#             "sql": 65,
#             "ml": 60
#         }
#     }
# }


# print(students["s2"]["name"],students["s2"]["marks"]["sql"])



# def decorator(func):
#     def add(a,b):
#         ("printing numsss")
#         return func(a,b)

#     return add
    
# @decorator
# def new(a,b):
#     return a + b

# res=new(1,2)
# print(res)


# def decor(func):
#     def old(a,b):
#         print("sum of nummmm")
#         return func(a,b)
       
#     return old

# @decor
# def new(a,b):
#     return a + b
# print(new(12,5))


# def dec(func):
#     def one(a,b):
#         print("the sum is")
#         return func(a,b)
#     return one


# @dec
# def sum(a,b):
#     return a+b

# print(sum(2,5))


# class Exmp():
#     def one(self):
#         print("hiiii")

#         pass
#                               #innheritance
# class Child(Exmp):
#     def new(self):
#         print("brooooo")

# a=Child()
# a.new()
# a.one()


# def new():
#     yield 1
#     yield "hello iam mannnn"
#     yield 3

# a=new()
# print(next(a))
# print(next(a))
# print(next(a))

# a=[1,2,3,]

# b=iter(a)
# print(next(b))
# print(next(b))
# print(next(b))



# class Stud():
#     def __init__(self,name):
#         self.name=name

# s=Stud("manhar")
# print(s)
       
print("-----------------------------------------------")  


# a=10

# print(id(a))
# a=a+1
# print(id(a))


# a=[1,2,3]
# b=a

# print(a is b)
# print(a in b)


# name={"name":"manhar","age":21}

# print("manhar" in name.values())

# a = [1,2,3]
# b = [1,2,3]

# # print(a == b)  
# # print(a is b)   
# print(id(a))
# print(id(b))

# res=id(a) == id(b)
# print(res)

# a = []
# b = []
# (print(a==b))
# print(a is b)  

# new=[x for x in range(10)]
# print(new)


# a=(1,)
# print(type(a))
# aa=[1,2,[2,3,[4,5,6,[7,8,9]]]]
# print(aa)
# print(aa[-1][-1][-1][1])



# new=[1,2,[2,4,4,[3,4,5,5,],564,[1,2,6]]]
# # print(new[-1][7])                         #imppp
# print(new[-1][5][0])




# aa={
#     "one":{"name":"manhar","age":12},
#     "two":{"name":"shaad"}
# }

# print(aa["one"]["name"],aa["one"]["age"])
# print(aa.get("one").get("hyyy"))





# student={
#     "name":"manhar",
#     "age":21
   
# }

# student["aa"]="manharrrr"

# student.update({"placeee":"mlppp"})

# print(student)



# user = {
#     "id": 1,
#     "profile": {
#         "username": "manhar",
#         "city": "kochi"
#     }
# }

# print(user.get("id"))
# print(user.get("profile"))

# for i in range(1,11):
#     print(i)

# i=1
# while i<=20:
#  print(i)
#  i+=1
#  pass

# password = ""

# while password !="1234":                            #imppp
#     password=input("enter your passs")


# password=""

# while password !="aaa":
#     password=input("enter a passs::")

# aa=[1,2,[3,4,5,[7,7,8]]]

# print()
##########################################################

# new=[1,2,3,4,5,6,5,9]
# del new[-1]
# print(new)
# print(type(new))

# print(new.remove(1))

# print(new)



# new=[i*2 for i in range(10)if i %2==0]
# print(new)
    
# t=(1,2,3,4,4,5)
# print(t.index(4))
# print(len(t))


# new=list(t)
# new.append(100)    #changing tuple
# aa=tuple(new)
# print(aa)


# sett={1,2,3,3,4,55,55,6,7,8,6,7,8,9,11,11,22,33,44,33,22}
# # print(sett)
# print(sett.add("aa"))
# print(sett.update([1,2,3,4,5,99,88,77,66,77,88,9,"cc","zzzz"]))
# print(sett.remove("zzzz"))
# print(sett)

# sett = {"zzzz", 1, 2, 3, 4}

# for i in ["zzzz", 1, 2]:
#     sett.discard(i)

# sett.pop()
# print(sett)


# b={1,2,3,4,5}
# a={1,2,3}
# print(b.issuperset(a))







# d = {
#     "name": "Manhar",
#     "age": 21,
#     "course": "Python"
# }

# for k,v in d.items():
#     print(k,":",v)

# nums = [1, 2, 3, 4, 5, 6]

# new={x:x*x for x in nums}
# print(new)


# d = {"a": 1, "b": 2, "c": 3}

# swapped={b:a for a,b in d.items()}
# print(swapped)

# users = {
#  "a":20,
#  "b":15,
#  "c":25
# }
# print(users)

# ans={k:v for k,v in users.items() if v>=21 }
# print(ans)

# stud={
#     "one":{"name":"nhcjncjndc"},
#     "two":{"plave":"nfjfrjfrjfrf"}
# }
# print(stud["one"])


# stud={
#    "stud1":{ "name":"manhar"},
#    "stud2":{"name":"adhil","age":2},
#    "stud3":{"name":"arun"}
# }

# print(stud["stud2"]["age"])

# emp={
#     "emp1":{
#         "name":"manhar",
#         "age":21,
#         "place":{
#             "maths":10,
#             "phy":100,
#             "maths":50,
#             "maths":42,
#         }
        
#     }
# }
# print(emp["emp1"]["name"],emp["emp1"]["place"]["phy"])



# students = {
#     "s1": {
#         "name": "Manhar", 
#         "age": 21,
#         "marks": {
#             "python": 85,
#             "sql": 78,
#             "ml": 90
#         }
#     },
#       "s2": {
#         "name": "nabeel", 
#         "age": 21,
#         "marks": {
#             "python": 10,
#             "sql": 8,
#             "ml": 94
#         }
#     }
# }
# students["s1"]["name"]="shinas"
# students["s1"]["marks"].update({
#      "python": 35,
#             "sql": 7,
#             "ml": 56

# })
# print(students.get("s1"))

# print(students["s1"]["marks"]["ml"])
# print(students["s2"]["name"],students["s2"]["marks"]["python"])

# aa=[1,2,3,[4,5,6,[7,8],[9,10]]]

# print(aa[-1][3][0])

# def add(n):
#     if n==0:
#         return
#     print(n)
#     add(n-1)
# add(10)

# def decor(func):
#     def old(y,z):
#         print("sum is")
#         return func(y,z)
       
        
#     return old
# @decor
# def new(a,b):
#     return a+b
   
# print(new(5,6))


# def decor(func):
#     def sum(a,b):
#         print("sum isssss")
#         return func(a,b)
   
    
#     return sum


# @decor
# def add(a,b):
#     return a + b
# print(add(5,10))
# print(add(10,10))
# print(add(11,3))

# def decor(func):
#     def wrapper(a, b):
#         if a < 0 or b < 0:
#             print("Negative not allowed")
#         else:
#             return func(a, b)
#     return wrapper


# @decor
# def add(a, b):
#     return a + b


# print(add(5, 6))
# print(add(-3, 4))












# class Employee:
#     def __init__(self,name,place,address):
#         self.name=name
#         self.place=place
#         self.address=address
#     def details(self):
#         print(f"name: {self.name}")
#         print(f"address: {self.address}")
#         print(f"place: {self.place}")

#     def change(self,newaddress):
#         self.address=newaddress



# e1=Employee("manhar","tirur","dbbefhenrevn")
# e1.details()

# e1.change("changamplayyyy")
# e1.details()



# class AddNumbers:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     def add(self):
#         return self.a + self.b


# # object creation
# obj = AddNumbers(10, 20)

# # calling method
# print(obj.add())




# class Calculator:

#     def add(self, a, b):
#         return a + b

#     def sub(self, a, b):
#         return a - b

#     def mul(self, a, b):
#         return a * b

#     def div(self, a, b):
#         if b == 0:
#             return "Cannot divide by zero"
#         return a / b


# # Object creation
# c = Calculator()

# print("Add:", c.add(10, 5))
# print("Sub:", c.sub(10, 5))
# print("Mul:", c.mul(10, 5))
# print("Div:", c.div(10, 5))


# i=0
# while i<=5:
#     print(i)
#     i+=1


# li=[1,2,3,3,4,4,5,6,66,6,66,7,77,8]
# print(set(li))
# aa=li[0]=99
# print(aa)
# print(li)
# lii=[1,2,3,[4,5,6,[7,8,9,[1,2]]]]
# print(lii[-1][-1][2])





# aa=[1,2,[2,3,[4,5,6,[7,8,9]]]]
# # print(aa)

# new=[x for x in range(10)]
# print(new)                #list comphersion......

# new=(1,2,4,5,6,1,2,1)
# # aa=new.count(1) 
# # print(aa)
# print(new.count(1))###############
# print(new.index(1))##############


# # print(new)
# # print((1))
# print(new[-2])


# aa={1,2,3,3,4,1,2,3,4,5,6,7,7,6,89,99,11,11,1,11}
# # print(list(aa))
# # aa.update([1,2,3,44,33,22,11,55,66,65,45,76,87])
# # aa.discard(1000)
# # aa.discard(99)
# # aa.difference_update({1,2,3,4,5,6,7,89})
# aa.update({1,2,3,4})
# aa.difference_update({1,2,3,4,5,6,11})
# print(aa)


new={
    "stud1":{"name":"manhar","age":21,"place":"tirurr"},
    "stud2":{"name":"nabeel","age":21,"place":"kotakkal"},
    "stud3":{"name":"aaro","age":21,"place":"tirurrrrrrrrrrrr"},
    "stud4":{
        "name":"njn",
        "age":21,
        "place":"kerala"   #nested dicttttt
        }
    
}


new["stud2"]["name"]="broooooo"
print(new["stud2"]["name"])
print(new.get("stud3").get("place"))

aa={x:x+10 for x in range(10)}
print(aa)

# new["stud1"]["name"]='hashinnn'
# new["stud1"]["place"]='evideyoooo'
# new["stud1"].pop("name")
# print(new["stud1"])
# print(new["stud1"].keys())
# print(new["stud2"]["age"],new["stud4"]["name"])
# print(new["stud1"]["place"])

# print(new.get("stud1").get("place"),new.get("stud1").get("name"))


# new={x:x*x for x in range(1,15)if x%2==0}
# print(new)

# names = ["manhar","nabee","aaro"]
# aa={n: len(n) for n in names}
# print(aa)

# name="manhar"
# age=33
# print(f"name is:{name} and my age is {age}")




# def man(*args):
#     print(args)

# man(1,2,3,4,5,55)
# print(type(man))


# def man(n):
#     if n==5:
#         return    #recursion
#     print(n)
#     man(n+1)
# man(0)


# add=lambda a,b :a+b
# print(add(5,10))

# try:
#     a=100
#     b=0
#     res=print(a/b)
# except:
#     print("erroe occured")
# else:
#     print("the sum is:", res)
# finally:
#     print("thanks")

# d = {"a":10, "b":20, "c":30}
# aa=iter(d.items())
# print(next(aa))
# print(next(aa))
# print(next(aa))

# def gen():
#     yield "hello"
#     yield "okkke"
#     yield "bieee"

# g=gen()
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# nums=[1,2,3,4,5,6,7]
# ans=dict(map(lambda x:(x,x+10),nums))
# # ans=tuple(filter(lambda x :x%2 ==0,nums))
# print(ans)
# fil=filter(lambda x:x%2==0,nums)
# print(list(fil))

# names = ["manhar","aji","nabeel","an"]
# ans=list(filter(lambda x: len(x)>4,names))
# print(ans)




# from functools import reduce

# listt=[100,10000,55,46,78]

# out=reduce(lambda a,b:a+b,listt)
# print(out)

# names = ["manhar","nabeel","aaro"]
# ages = [21,22,20]

# a={k:v for k,v in zip(names,ages)}
# print(a)

# class Student:
#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return f"Student name is {self.name}"

# s = Student("Manhar")
# print(s)

# class Student:
#     def __init__(self, name):
#         self.name = name

#     def __repr__(self):
#         return f"Student('{self.name}')"

# s = Student("Manhar")
# print(s)


# def decor(func):
#     def add(a,b):
#         print("the sum")
#         return func(a,b)
#     return add
# @decor
# def new(a,b):
#     return(a+b)
# print(new(10,3))
    
    
# class Calculator:
#     def add(self,a,b):
#         return a+b
#     def minus(self,a,b):
#         return a-b

# c=Calculator()

# print("addition",c.add(5,6))


# text="hello world"
# print(text.split())

# for i in text.split():
#     if i=="world":
#         print(i)


# class parent():
#     def show(self):
#         print("hiiii")

# class child(parent):
#     def dis(self):
#         print("hiiiiihloooo")
# c=child()
# c.dis()
# c.show()


# class Animal():
#     def sound(self):
#         print("make sound")
# class dog(Animal):
#     def sound(self):
#         print("barkkk")
# class cat(Animal):
#     def sound(self):
#         print("meoww")

# c=cat()
# b=dog()
# a=Animal()
# a.sound()
# c.sound()
        

# class stud:
#     def __init__(self):
#         self.__mark=90
#     def show(self):
#         print(self.__mark)

# s=stud()
# s.show()

# print(s.__mark)


# from abc import ABC,abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass

# class Dog(Animal):
#     def sound(self):
#         print("boww")

# d=Dog()
# d.sound()

# from functools import reduce
# from abc import ABC,abstractmethod
# class animal(ABC):
#     @abstractmethod
#     def sound(self):
#         print("makeing sounds")


# class dog(animal):
#     def sound(self):
#         print("bowwwwwwwwwwwwwwwww")

# c=dog()
# c.sound()



# def decor(func):
#     def old(a,b):
#         print("summmmm")
#         return func(a,b)
#     return old


 

# def add(a,b):
#     return a+b
# # print(add(9,6))
# ans=add(2,5)
# print(ans)



# def new():
#     yield 1
#     yield "enddd"
# g=new()
# print(next(g))
# print(next(g))


aa=[1,2,3,4]
neww=filter(lambda x:x%2==0,aa)
print(list(neww))

gg=iter(aa)
print(next(gg))
print(next(gg))