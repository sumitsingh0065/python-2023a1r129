'''BEGINNER LEVEL'''

'''Q. A lambda can take an argument and add 10 to it.'''

add_10 = lambda x: x + 10
print(add_10(5))

'''Q. Multiply two numbers'''

multiply = lambda x,y: x*y
print(multiply(4,5))

'''Q. Square a number'''

square = lambda x: x ** 2
print(square(6))  

'''Q. Return the last character of a string'''

last_char = lambda s: s[-1]
print(last_char("Sumit"))

'''Q. Convert a string to uppercase'''

to_upper = lambda j: j.upper()
print(to_upper("sumit"))

'''Q. Check if a string contains the letter (a) '''

contains_a = lambda s: 'a' in s
print(contains_a("apple"))

'''Q. Find the maximum of two numbers'''

maximum = lambda x,y: x if x>y else y
print(maximum(10,20))

'''Q. Return the length of a list'''

length = lambda lst: len(lst)
print(length([1,2,3,4,5]))

'''Q. Check if a number is divisible by 5'''

divide_by_5 = lambda n: n % 5 == 0
print(divide_by_5(25))

'''Q. Concatenate two strings'''

concatenate = lambda s1,s2: s1 + s2
print(concatenate("Hello, ","World!"))

'''Q. Find the cube of a number'''

cube = lambda x: x ** 3
print(cube(3))

'''INTERMEDIATE LEVEL'''

'''Q. Square all numbers in a list'''

numbers = [1,2,3,4,5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)

'''Q. Find even numbers in a list'''

nums = [1,2,3,4,5,6]
evens = list(filter(lambda x: x%2 == 0, nums))
print(evens)

'''Q. Extract words longer than 4 letters'''

words = ["sumit", "is", "a", "developer", "from", "india"]
longwords = list(filter(lambda w: len(w)>4,words))
