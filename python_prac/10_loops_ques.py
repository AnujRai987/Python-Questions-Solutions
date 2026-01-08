#Question 1: Given a list of numbers, count how many are positive.
'''
numbers=[1,-2,3,-4,5,6,-7,-8,9,10]
count=0
for value in numbers:
    if value>=0:
        count+=1

print("Final count of positive number is: ",count)
'''

#Question 2: Calculate the sum of even numbers up to a given number n.
'''
n=8
sum=0
i=1
while(i<=8):
    if(i%2==0):
        sum+=i
    i+=1

print("The sum of given n even numbers : {}".format(sum))
'''

#Question 3: Print the multiplication table for a given number up to 10, but skip the fifth iteration.
'''
n=6
for i in range(1,11):
    if(i==5):
        continue
    print(f"{n} X {i} = {n*i}")
'''

#Question 4:Reverse a string using a loop.

'''
input_str="Python"
reversed_str=""

for char in input_str:
    reversed_str=char+reversed_str
    print(reversed_str)    # for understanding how it works

print(reversed_str)
'''

#Question 5:Given a string, find the first non-repeated character.
'''
input_str="teeter"

for char in input_str:
    if(input_str.count(char)==1):
        print(char)
        break
'''

#Question 6:Compute the factorial of a nubmer using a while loop.
'''
num=5
fact=1
if(num==0 or num==1):
    pass
else:
    i=1
    while(i<num+1):
        fact*=i
        i+=1
print(f"factorial of {num} is :{fact}")
'''

#Question 7:Keep asking the user for input until they enter a number between 1 and 10.
'''
while True:
    number=int(input("Enter value b/w 1 and 10 :"))
    if(0<number<11):
        print("Thanks")
        break

    else:
        print("Invalid input try again....")
'''

#Question 8: Check if a number is prime.
'''
num=17
isPrime=True

if(num>1):
    for i in range(2,num):
        if(num%i==0):
            isPrime=False
            break

print("Number {} is {}".format(num,"Prime" if isPrime==True else "Not Prime"))
'''

#Question 9: Check if all elements in a lsit are unique. If a duplicate is found,exit the loop and print the duplicate.
'''
items=["apple","banana","orange","apple","mango"]
count=0

for item in items:
    if(items.count(item)>1):
        print(item)
        break
'''
#Question 10:Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second,but stops after retries.
'''
import time

Max_attempts=5
no_attempts=0
wait_time=1

while no_attempts<Max_attempts:
    print(f"Attempt :{no_attempts+1} , Wait Time : {wait_time} seconds")
    time.sleep(wait_time)
    no_attempts+=1
    wait_time*=2
'''
