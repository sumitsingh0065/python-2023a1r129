'''Q.6 -  write a program to create a list of student's records 
and search a student record using a dictionary.'''
stulist=[]
num=int(input("Enter number of students: "))
for i in range(num):
    name=input("Enter name: ")
    age=int(input("Enter age: "))
    marks=float(input("Enter marks: "))
    stu={"Name":name,"Age":age,"Marks":marks}
    stulist.append(stu)
print(stulist)
search=input("Enter name to search: ")
found=False
for student in stulist:
    if student["Name"]==search:
        print("Student found:",student)
        found=True
        break
if not found:
    print("Student not found")
    
