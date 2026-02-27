# stud={"name":"manhar","batch":57}

# stud["pincode"]=67601
# stud.update({"pin":676301})

# print(stud)



# print(aa.slice([2:]))

# s={1,2,3} b={3,4,5}

# print(set(a.union(b)))

# t=(1,)
# print(t)
# print(type(t))

# class 




# def new(func):
#     def wrapper():
#         text = func()

#         result = ""
#         upper = True

#         for ch in text:
#             if ch.isalpha():
#                 if upper:
#                     result += ch.upper()
#                 else:
#                     result += ch.lower()
#                 upper = not upper
#             else:
#                 result += ch

#         print(result)
#     return wrapper


# @new
# def aa():
#     return "goood afternoon"


# aa()


# text = "manhar gurukkal"
# print(text.capitalize())
# aa=text.replace("har","HAR")


# print(aa)



def decor(func):
    def new():
        text=func()
        result=""
        
        for i,x in enumerate(text):
            if i%2==0:
                result+=x.upper()
            else:
                result+=x.lower()
                
        return result
    return new
            
        
@decor
def one ():
    return "gooooood morninggg sir how are uuu"
    
print(one())


a="manhar gurukkal"

print(a.capitalize())
print(a[3:6])
print(a.upper())
print(a.lower())
print(a.title())
print(a.strip())
print(a.split())
print(a.swapcase())
print(a.count("a"))
print(a.find("g"))
print(a.title())

print(a[::-1])
print("".join(reversed(a)))
print(a.index("g"))


student={"name":"manhar","age":22}
student["pincode"]=676301
student.update({"pin":32411,"place":"tirurr"})
print(student)

print(student.get("name"))
print(student["place"])



print(student["name"])



a="manhar gurukkal"

b="ck"
print("the name is:",a+" "+b)
print(f"name is {a} {b}")
print(a+" "+b)



a=[1,2,3,4,4,]
a.append(9)
a.extend([0,8,7,6])
a.insert(0,11)
a.pop(0)
a.pop()
a.remove(7)
b=a.index(4)
c=a.count(4)
a.clear()
print(a)
print(b)
print(c)

print(a.count(4))
print(a.index(3))

a.reverse()
print(a)





# a={1,2,3,1,3,4,5}
# b={11,12,1,2,3,55,66}
# print(a)

# a&=b
# print(a)
# bb=[1,2,3,34,5,6,77]
# bb={"manharrr","nnnnn",1,2}
# aa.update(bb)
# print(aa)
# aa.update([99,88,77,66])
# aa.add("mm")
# aa.update({"abc","bbb"})
# aa.remove("abc")
# aa.discard(99)
# print(aa)


# a={1,2,3,1,3,4,5}
# b={11,12,1,2,3,55,66}

# print(a)
# a|=b
# print(a)
# print(a&b)
# a&=b
# print(a)
# print("..............")
# aa=a-b
# print(aa)
# print(a)
# a-=b
# print(a)
print(a<=b)
print(a>=b)