'''Various forms of function arguments'''

#1. Required function argument
#2. Optional/Default argument
#3. keyword argument
#4. Var arg / orbitary parameter
#5. Key Vararg

# def printname(fname,lname):
# (lname="",fname):   /  default parameter can't be followed as mendatory

# def printname(fname,lname=""):
#     print(f"Hello {fname} {lname}")
# # printname("james","Bond")g
# printname("Sumit")

# def printname(fname,mname=".",lname="."):
#     print(f"Hello {fname} {mname} {lname}")
# printname("james",lname="bond")  # lname="bond" call the fucntion.

# # def add(*para):
# def add(**para): #for keyword argument
#     # print(sum(para))   #print(para)
#     print(sum(para.values()))

# add()
# add(1)
# add(1,2)
# add(1,2,3)
# add(1,2,3,4)
# add(1,2,3,4,5,6,7,6,5,4,5,5,3,5,3)

# add(a=1)
# add(a=1,b=2)
# add(a=1,b=2,c=3)

def greet():
    return "Hello World"
# res=greet()
# print(res)
res=greet
print(res())

'''
1. We can assign address of function to a var
2. We can pass function as a parameter to another function
3. We can return function from another function body
4. We can save function in any ds just like normal values
'''



