class Address:
    def __init__(self,hno,street,city,state,pin):
        self.hno=hno
        self.street=street
        self.city=city
        self.state=state
        self.pin=pin

    def printAddress(self):
        print(f"Address:{self.hno} {self.street} {self.city} {self.state} {self.pin}")


class Student:
    def __init__(self,sid,name,address):
        self.sid=sid
        self.name=name
        self.address=address
      
    def printStu(self):
        print(f"Sid:{self.sid} Name:{self.name}")
        self.address.printAddress()


class Employee:
    def __init__(self,eid,name,address):
        self.eid=eid
        self.name=name
        self.address=address

    def printEmp(self):
        print(f"Eid:{self.eid} Name:{self.name}")
        self.address.printAddress()
      
add=Address("123","Sector-19","Noida","UP","6767462")
st=Student(101,"Sumit",add)
emp=Employee(1002,"King",add)

st.printStu()
emp.printEmp()
