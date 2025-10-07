'''def message():
    print("Hello World")
 
for i in range(5):
    message()'''

    # with parametre with return value

# def add():
    # num1,num2=map(int,input().split(" "))
    # print(f"sum of {num1} and {num2} = {num1+num2}")
# def add(num1,num2):
#     print(num1+num2)


# num1,num2=map(int,input().split(" "))
# print(add(num1,num2))

# lst=[]
# print(lst.append(1000))
# print(lst.pop())

def fibonacci(limit):
    lst=[]
    num1,num2=0,1
    for i in range(limit):
        lst.append(num1)
        num1,num2=num2,num1+num2

    for i in lst[::-1]:
        print(i,end=" ")
fibonacci(10)


        






