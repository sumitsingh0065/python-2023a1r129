'''
Inheritance is the mechanism of acquiring some attributres of any existing class type into a new class type.
One of the key concepts of OOP's.
Established a hierarchical relationship among classes.
Established a superclass/subclass relationship.
Established "is a " relationship.

Bemefits:
1. Reusability of code.
2. put code in one class, use it in all the subclasses.
3. Write general purpose code designed for a supertype that works for all subtypes.
4. A superclass defines a general set of functionality, whereas subclasses define functionalities specific to them.

Syntax:
class derivedclassname(baseclassname):
     <statement-1>
     <statement-N>
'''

class Employee:
    def __init__(self, eid, name, contact):
        self.eid = eid
        self.name = name
        self.contact = contact
    def printEmp(self):
        print(f"""
Eid : {self.eid}
Name : {self.name}
Contact : {self.contact}""")
        # ob = Employee(101, 'Sumit', 9876543210)
# ob.printEmp()
        
class RegularEmp(Employee):
    def __init__(self,eid,name,contact,basic,hra,da):
        # super function
        super().__init__(eid,name,contact)
        self.basic=basic
        self.hra=hra
        self.da=da
        self.salary=self.basic+self.hra+self.da*30

    def printRegEmp(self):
        super().printEmp()
        print(f"""
Basic:{self.basic}
HRA:{self.hra}
DA:{self.da}
salary:{self.salary}
""")

ob=RegularEmp(101,"james","21324354354",77000,54000,24000)
ob.printRegEmp()
