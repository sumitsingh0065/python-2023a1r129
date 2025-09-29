'''

2 #Tuple properties
3 # a)It is a sequence (it allow indexing and slicing)
4 #b)It is an ordered collection
5 #C)It is immutable(operations l1ke insertion updation and deletion are not i
6 # d)It may contains duplicate elements
f）It preserve the insertion order
8#
g)It may contains different type of objects

t=tuple() => when we want to covert an existing object in to tuple
t=(12,23,34)  /   t=1,2,3
print(t)
'''
'''
t=tuple()
t=(1,2,3)
print(t)
# t=1,2,3,4,5,6,7,8,9
t=(12)  #t=(12,)
print(type(t))

t=(10,20,30,40,50)
print(t.count(30))
print(t.index(30))
# print(t[2])
# tuple has only two functions count and index beause it is immutable

tup=10,20,30
print(tup)
a,b,c=tup
print(f"a={a} b={b} c={c}")
a,*b=tup
print(f"a={a} b={b}")
'''
'''
num1,num2 = int(input("num1")), int(input("num2"))
# num1= int(input("Enter first number: "))
# num2= int(input("Enter second number: "))
print(f"before swap num1={num1} and num2={num2}")
# temp = num1  
# num1 = num2
# num2 = temp
num1, num2 = num2, num1
print(f"after swap num1={num1} and num2={num2}")
'''
# 0  1  1  2  3  5  8 13 21

# num1=0
# num2=1
num1,num2=0,1
# print(num1,num2,end=" ")
for i in range(10):
    print(num1,end=" ")
    num1,num2=num2,num1+num2
    # num3=num1+num2
    # print(num3,end=" ")
    # num1=num2
    # num2=num3
# num1,num2=num2,num1+num2
# print(num1,num2,end=" ")

