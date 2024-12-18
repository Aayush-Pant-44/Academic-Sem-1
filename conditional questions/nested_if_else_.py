#1
a=233
b=344
c=a
a=b
b=c
print(a,b)

# 2nd method by XOR method

a=10
b=20
a=a^b
b=a^b
a=a^b
print(a,b)

#2
print("welcome to teasure land")
msg=input("Choose a direction 'left' or 'right'")
if msg=="right":
  print("Game over")
elif msg=="left":
  msg2=input("do you want to 'swim' or 'wait'")
  if msg2=="swim":
    print("game over")
  elif msg2=="wait":
    msg3=input("select a color 'red' 'blue' 'yellow'= ")
    if msg3=="yellow":
      print("you win")
    elif msg3=="red" or msg3=="blue":
      print("Game over")
    else:
      print("invalid input")
  else:
    print("invalid input")
    
else:
  print("invalid input")

#4
x=int(input("enter a integer"))
if x>0:
  print("True")
elif x<0:
  print("False")
else:
  print("zero")

#5
num=int(input("enter the number"))
if num%2==0:
  print(f"{num} is even")
else:
  print(f"{num} is odd")

#6
sub_1=float(input("enter marks of first subject= "))
sub_2=float(input("enter marks of second subject= "))
sub_3=float(input("enter marks of third subject= "))
sub_4=float(input("enter marks of fourth subject= "))
total_marks=sub_1+sub_3+sub_2+sub_4
per=(total_marks/400)*100
print(f"totla marks= {total_marks}, percentage= {per}")
if per>=70:
  print("distiction")
elif per>=60:
  print("first")
elif per>=40:
  print("pass")
elif per<40:
  print("fail")
else:
  print("error")

#7
cost=int(input("enter the cost price of bike"))
if cost>100000:
  print("tax= 15%")
elif cost>50000:
  print("tax= 10%")
else:
  print("tax= 5% ")

#8
age_1=int(input("Enter the age of first person"))
age_2=int(input("Enter the age of second person"))
age_3=int(input("Enter the age of third person"))
age_4=int(input("Enter the age of fourth person"))
if age_1<age_2 and age_1<age_3 and age_1<age_4:
  print(f"{age_1} is the youngest one")
elif age_2<age_1 and age_2<age_3 and age_2<age_4:
  print(f"{age_2} is the youngest one")
elif age_3<age_1 and age_3<age_2 and age_3<age_4:
  print(f"{age_3} is the youngest one")
else:
  print(f"{age_4} is the youngest one")

#9
age_1=int(input("Enter the age of first person"))
age_2=int(input("Enter the age of second person"))
age_3=int(input("Enter the age of third person"))
age_4=int(input("Enter the age of fourth person"))
if age_1>age_2 and age_1>age_3 and age_1>age_4:
  print(f"{age_1} is the oldest one")
elif age_2>age_1 and age_2>age_3 and age_2>age_4:
  print(f"{age_2} is the oldest one")
elif age_3>age_1 and age_3>age_2 and age_3>age_4:
  print(f"{age_3} is the oldest one")
else:
  print(f"{age_4} is the oldest one")

#10
grade=int(input("enter your grades= "))
if grade<25:
  print("D")
elif grade<45:
  print("C")
elif grade<50:
  print("B")
elif grade<60:
  print("B+")
elif grade<80:
  print("A")
elif grade>=80:
  print("A+")
else:
  print("wrong input grade")

#11
exp=int(input("enter you experience year"))
if exp>10:
  print("10%")
elif exp>=6:
  print("8%")
else:
  print("5%")

#12
days=int(input("enter no of days= "))
if days>15:
  print("rs5/day")
elif days>=11:
  print("rs4/day")
elif days>=6:
  print("rs4/day")
else :
  print("rs2/day")

#13
salary=int(input("enter your salary"))
service=int(input("years of service"))

if service>=5:
  salary=salary+(5/100)*salary
  print(f"you salary with bonus is {salary}")
else:
  print("sorry no bonus for you")

#14
rad=float(input("enter the raidus"))

if rad>0:
  area=3.14*rad*rad
  print(area)
else:
  print("improper radius")

#15
import math
a = int(input("Enter the no of students in the first class: "))
b = int(input("Enter the no of students in the second class: "))
c = int(input("Enter the no of students in the third class: "))
total_students=a+b+c
total_desk=math.ceil(total_students/2)
print(total_desk)

#16
n=int(input("Enter the no of students: "))
k=int(input("Enter the no of total apples: "))
apple_for_each_student=k//n
print(apple_for_each_student)
remainning_apples=k-apple_for_each_student*n
print(remainning_apples)

#17
age=int(input("enter your age: "))
if age<18:
  print("no, vote for you little infant")
else:
  print("yes you can vote")

#18
city=input("enter a city name from Delhi, Agra, Jaipur: ").capitalize()
direc={
  "Delhi":"Red Fort",
  "Agra":"Taj Mahal",
  "Jaipur":"Jal Mahal"
  }

if city in direc:
  print(direc[city])
else:
  print("incorrect city name choose from 3 cities only")

#19
num=int(input("enter a int number: "))
if num%2==0 and num%3==0:
  print("Divisible")
else:
  print("not divisible")

#20
a=int(input("enter first number: "))
b=int(input("enter second number: "))
op=input("enter the operator: ")
dire={
  "+":a+b,
  "-":a-b,
  "*":a*b,
  "/":a/b,
  "//":a//b,
  "%":a%b,
  "^":a**b
}

if op in dire:
  print(dire[op])
else:
  print(f"{op} is not a valid operator")

#21
total_classes=int(input("total number of classes: "))
absent_classes=int(input("enter absent classes: "))

present_days=total_classes-absent_classes
present_percentage=round(((present_days/total_classes)*100),2)
print(f"present days= {present_percentage}%")

if present_percentage<75:
  print("you are not eligible enough to give exams")
else:
  print("you can give you exams")

#22
per=float(input("enter your percentage: "))
if per<40:
  print("failed")
elif per<55:
  print("Fair")
elif per>65:
  print("Good")
else :
  print("Excellent")

#23
age=int(input("enter your age: "))
gender=input("enter you gender M for male and F for female: ").capitalize()
if age<30 and age>=18:
  if gender=="M":
    print("wage= Rs.700/day")
  elif gender=="F":
    print("wage= Rs.750/day")
  else:
    print("wrong gender")
elif age>=30 and age<=40:
  if gender=="M":
    print("wage= Rs.800/day")
  elif gender=="F":
    print("wage= Rs.850/day")
  else:
    print("wrong gender")
else:
  print("criteria doesnt mathch for you age")

#24
a=True
b=True
c=True
d=True
print(c)
print(d)
print(not a)
print(not b)
print(not c)
print(not d)
print(a and b)
print(a or b)
print(a and b or c)
print(not a or b or c)
print(not a or not b or not c)
print(not(not a or not b or not c))

#25
n=int(input("enter a number"))
if n%3==0 and n%5==0 :
  print("Fizz Buzz")
elif n%5==0:
  print("buzz")
elif n%3==0:
  print("fizz")
else :
  print(n)

#26
name=input("enter username: ")
passcode=input("enter password: ")
credintials={
  "admin": "access granted", 
  "password123": "access granted"
}
if name in credintials and passcode in credintials:
  print("access granted")
else:
  print("access denied")

#27
a=int(input("enter first number: "))
b=int(input("enter second number: "))

if a>b:
  print(f"{a} is greater")
elif a==b:
  print("they are equal")
  if a<0:
    print("negative")
  elif a>0:
    print("positive")
  else:
    print("Zero")

else:
  print(f"{b} is greter")

#28
score=int(input("enter you subject score: "))
if score>=90:
  print("congratulations")
elif score>=50:
  print("you need improvement")
else:
  print("retake exam")

#29
age=int(input("enter your age: "))
exprience=int(input("enter you expreince in terms of years: "))

if age>=18:
  if exprience>3:
    print("highly eligible")
  elif exprience>1:
    print("eligible")
  else :
    print("under review")
  
else:
  print("not eligible")

#30
weight=float(input("eneter weight of luggage in kg: "))
urgency=input("If urgent type true and if not type false: ").capitalize()
cost=0

if urgency=="True":
  cost+=5
elif urgency=="False":
  cost=cost
else:
  print("wrong input")

if weight<=5:
  cost+=5
elif weight<=20:
  cost+=10
else:
  cost+=20

print(f"delevery cost= ${cost}")

#31
income=int(input("enter your income: "))

if income>50000:
  credit_score=int(input("enter your credit score: "))
  if credit_score>700:
    print("loan is approved")
  elif credit_score>=600:
    print("loan approved but with high intrest")
  else:
    print("your loan is rejected because of low credit score")
  
else:
  print("your loan is rejected because of low balance")

#32
weather=input("enter the weather 'sunny' or 'rainy': ")
if weather=="sunny":
  print("go for outdoor activities like hiking or picnic")
elif weather=="rainy":
  umb=input("write 'yes' if you have umberella and 'no' if you dont: ")
  if umb=="yes":
    print("go to a nearby mall or museum")
  elif umb=="no":
    print("stay at home watch movies")
  else:
    print("incorrect command")
else:
  print("weather not included")    

#33
print("welcome to the haunted house")
dicision_1=input("To go upstairs type 'up' and to go downstairs type 'down': ")

if dicision_1=="down":
  print("Game over")
elif dicision_1=="up":
  decision_2=input("if you want to enter room type 'in' and to stay outside type 'out': ")
  if decision_2=="in":
    print("game over")
  elif decision_2=="out":
    decision_3=input("choose between 'ghost', 'warewolf', 'vampire': ")
    if decision_3=="vampire" and decision_3=="ghost":
      print("game over")
    elif decision_3=="warewolf":
      print("you win")
    else:
      print("you entered the wrong option")
  else:
    print("you entered the wrong option")
else:
  print("you entered the wrong option")

#34
print("welcome to the Jungle Adventure")
decision_1=input("To go left type 'left' and to go right type 'right': ")

if decision_1=="right":
  print("Game over")
elif decision_1=="left":
  decision_2=input("if you want to climb a tree type 'climb' and to explore the cave type 'explore': ")
  if decision_2=="climb":
    print("game over")
  elif decision_2=="explore":
    decision_3=input("choose between 'bear', 'tiger', 'snake': ")
    if decision_3=="bear" and decision_3=="tiger":
      print("game over")
    elif decision_3=="snake":
      print("you win")
    else:
      print("you entered the wrong option")
  else:
    print("you entered the wrong option")
else:
  print("you entered the wrong option")

#35
print("welcome to the Magic Forest")
decision_1=input("To go north type 'n' and to go south type 's': ")

if decision_1=="s":
  print("Game over")
elif decision_1=="n":
  decision_2=input("if you want to cross a river type 'cross' and to follow the path type 'follow': ")
  if decision_2=="cross":
    print("game over")
  elif decision_2=="follow":
    decision_3=input("choose between 'fairy', 'ogre', 'elf': ")
    if decision_3=="fairy" and decision_3=="ogre":
      print("game over")
    elif decision_3=="elf":
      print("you win")
    else:
      print("you entered the wrong option")
  else:
    print("you entered the wrong option")
else:
  print("you entered the wrong option")

#36
print("Welcome to the Space Mission")
decision_1=input("To go to moon type 'moon' and to go Mars type 'mars': ")

if decision_1=="mars":
  print("Game over")
elif decision_1=="moon":
  decision_2=input("if you want to land on the surface type 'land' and to stay in the orbit type 'stay': ")
  if decision_2=="land":
    print("game over")
  elif decision_2=="stay":
    decision_3=input("choose between 'alien', 'asteroid', 'satellite': ")
    if decision_3=="alien" and decision_3=="asteroid":
      print("game over")
    elif decision_3=="satellite":
      print("you win")
    else:
      print("you entered the wrong option")
  else:
    print("you entered the wrong option")
else:
  print("you entered the wrong option")

#37
print("Welcome to the Pirate Island")
decision_1=input("To go left type 'left' and to go Right type 'right': ")

if decision_1=="right":
  print("Game over")
elif decision_1=="left":
  decision_2=input("if you want to dig for tresure type 'dig' and to sail the ship type 'sail': ")
  if decision_2=="dig":
    print("game over")
  elif decision_2=="sail":
    decision_3=input("choose between 'shark', 'pirate_ship', 'mermaid': ")
    if decision_3=="shark" and decision_3=="pirate_ship":
      print("game over")
    elif decision_3=="mermaid":
      print("you win")
    else:
      print("you entered the wrong option")
  else:
    print("you entered the wrong option")
else:
  print("you entered the wrong option")
