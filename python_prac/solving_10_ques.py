# Problem 1: Age Categorization
'''
age=int(input("Enter your age: "))
if(age<13):
    print("child")
elif(age <20):
    print("Teenager")
elif(age <60):
    print("Adult")
else:
    print("Senior")
'''

#Problem 2: Movie tickets are priced based on age:$12 for adults(18 and over),$8 for children. Everyone gets a $2 discount on wednesday.

'''
age = int(input("Enter your age: "))
wednesday=1
price =8 if age<18 else 12

if wednesday==1:
    price-=2

print("Ticket price for you is : ${}".format(price))
'''

#Problem 3: Assign a letter grade based on a student's score: A(90-100),B(80-90),C(70-79),D(60-69),F(below 60).
'''
marks=int(input("Enter your marks: "))
if(marks<=100 and marks>=0):
    grade= 'F' if marks<60 else ('D' if marks<=69 else ('C' if marks<=79 else ('B' if marks<=90 else 'A')))
else : 
    grade="invalid marks"
print(f"Your Grade is : {grade}")

'''

#Problem 4: Determine if a fruit is ripe,overripe or unripe based on its color.(e.g., Banana:Green-Unripe,Yellow-Ripe,Brown-Overripe)
'''
fruit="Banana"
color=int(input("Press...\ncolor of fruit:\n1.Green\n2.yellow\n3.Brown\nEnter: "))

condition="Unripe" if color==1 else("Ripe" if color==2 else "Overripe")

print(f"{fruit} is {condition}.")
''' 

#Problem 5: Suggest an activity based on the weather(e.g.,Sunny-Go for a walk,Rainy-Read a book, Snowy - Build a snowman).
'''
weather="Rainy"
w=weather.lower()
if(w=="sunny"):
    activity="Go for a walk"

elif(w=="rainy"):
    activity="Read a book"

elif(w=="snowy"):
    activity="Build a snowman"
else:
    activity="Not Known"

print(activity)
'''

#Problem 6: Choose a mode of transportation based on the distance(e.g.,<3Km: Walk, 3-15Km: Bike ,>15Km : Car)
'''
distance=90
mode_transport="Walk" if distance<3 else("Bike" if distance<=15 else "Car")
print(f"Distance to travel is {distance} Km , so choose : {mode_transport}")
'''


#Problem 7: Customize a coffee order:"Small","Medium",or"Large" with an option for "Extra shot" of espresso.
'''
order_size=int(input("what size do you want :\n1.Small\n2.Medium\n3.Large\n\nChoose:"))
coffee_size={1:"Small",2:"Medium",3:"Large"}
option=input("Do you want Extra shot of espresso (yes/no):")
if(option.lower()=="yes"):
    print(f"Here is your {coffee_size[order_size]} coffee with extra shot of espresso.")
else:
    print(f"Here is your {coffee_size[order_size]} coffee.")

'''

#Problem 8: Password Strength Checker weak ,medium or strong .if chars()<6) :weak, char (6-10) :Medium ,char(>10):Strong
'''
password="Hel"
chars=len(password)

strength="Weak" if chars<6 else ("Medium" if chars<=10 else "Strong")
print("Your password is "+strength)
'''

#Problem 9: Determine if it is a leap year or not
'''
year=1600

check="Yes" if((year%400==0) or (year%4==0 and year%100!=0)) else "Not"
print(check+ " "+str(year)+" a Leap year.")
'''


#Problem 10: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2years- Puppy food , Cat: >5years- Senior cat food)

'''
pet="Cat"
pet_Age=10
food="Puppy food" if (pet.lower()=="dog" and pet_Age<2) else ("Senior cat food" if (pet.lower()=="cat" and pet_Age>5) else "No informatio realated to this.")
print(f"Recommended food for this {pet} : {food}")
'''