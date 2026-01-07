#Question 1: Write a function to calculate and return the square of a number.
'''
def square(x):
    return x**2
print(square(2))
'''

#Question 2: Create a fucntion that takes two numbers as parameters and returns their sum.
'''
def sum(x,y):
    return x+y
print(sum(2,4))
'''

#Question 3: Write a function multipy that multiplies two numbers,but can also accept and multipy strings.
'''
def multipy(p1,p2): 
    return p1*p2
print(multipy(4,5))
print(multipy('h',5))
'''

#Question 4: Create a function that returns both the area and circumference of a cirlce given its radius.
'''
import math

def circle_stats(r):
    area=math.pi*(r**2)
    circumference=2*math.pi*r
    return area,circumference

a,c=circle_stats(4)
print("Area:{}\n".format(round(a,2)),"Circumference:{}".format(round(c,2)))
'''

#Question 5: write a function that greets a user.If no name is provided,it should greet with a default name.
'''
def greet(name="Guest"):
    return ("Hello, "+ name + "!")

print(greet())
print(greet("Anuj"))
'''

#Question 6:Create a lambda function to compute the cube of a number.
'''
cube_number=lambda num : num **3
print(cube_number(3))
'''
#Question 7: Write a function that takes variable number of arguments and return their sum.
'''
def sum_all(*args):
    add=0
    for i in args:
        add+=i
    return add
    # return sum(args)
print(sum_all(1,3,4))
'''

#Question 8: Create a function that accepts any number of keyword arguments and prints them in the format key: value.
'''
def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")

print_kwargs(name="Anuj",age=24)
'''

#Question 9: Write a generator function that yields even numbers up to a specified limit.
'''
def even_numbers(limit):
    for i in range(2,limit+1,2):
        yield i
        

for num in even_numbers(10):
    print(num)
'''

#Question 10: Create a recursive function to calculate the factorial of a number.
'''
def factorial(num):
    if(num==0):
        return 1
    
    return factorial(num-1)*num

print(factorial(5))
'''