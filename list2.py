lst=[]
print(lst)
lst.append(10)
lst.append("sumit")
lst.append(999900)
lst.append("sumit@gmail.com")
print(lst)
lst.insert(2,100)
print(lst)
lst2=["street-10","moida","india"]
# for data in lst2:
#     lst.append(data)
lst.extend(lst2)
print(lst)    
lst[4]="sumitbond@007.com"
print(lst)
del(lst[3])
print(lst)
# removing element and storing the element we use pop
# cn=lst.pop()
# print(cn)
# print(lst)

cn=lst.pop(3)
print(cn)
print(lst)
lst.remove("street-10")
print(lst)

salary=[9000,5000,7000,3000,1000,0000]
# print(f"before sort {salary}")
# # salary.sort()
# # print(f"after sort {salary}")
# # salary.sort(reverse=True)
# newlist=sorted(salary)
# print(f"after sort {salary}")
# print(f"after sort {newlist}")

# salary.reverse()
# new=list(reversed(salary))
# print(new)

lst=["sumit","saransh","vinay","vansh","shola"]
# c=lst.count("sumit")
# print(f"count={c}")
# print(lst.index("sumit",4))

# lst.clear()
# print(lst)

lst[10,20]
lst2=lst
lst2.append(100)
print(lst)


