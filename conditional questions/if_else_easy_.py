#1
a=int(input("enter first number"))
b=int(input("enter second number"))

if a==b:
    print("1")
elif a>b:
    print("2")
else :
    print("3")

################----------------------#####################

#2 
n=int(input("enter first number"))
if n%2==0:
  print("even")
else :
  print("odd")


################----------------------#####################

#3
n=int(input("enter a no between 1 to 12 number"))
#you can also use ditionary for this
if n==1:
  print("january")
elif n==2:
  print("february")
elif n==3:
  print("mar")
elif n==4:
  print("apr")
elif n==5:
  print("may")
elif n==6:
  print("june")
elif n==7:
  print("july")
elif n==8:
  print("aug")
elif n==9:
  print("sep")
elif n==10:
  print("oct")
elif n==11:
  print("nov")
elif n==12:
  print("dec")
else :
  print("out of range number")



################----------------------#####################

#2nd method
n=input("enter a no between 1 to 12 number")
dic = {
    "1": "Jan",
    "2": "Feb",
    "3": "Mar",
    "4": "Apr",
    "5": "May",
    "6": "Jun",
    "7": "Jul",
    "8": "Aug",
    "9": "Sep",
    "10": "Oct",
    "11": "Nov",
    "12": "Dec"
}

if n in dic:
  print(dic[n])


################----------------------#####################



#4
n=float(input("enter your marks"))
if n<25:
  print("f")
elif n<45:
  print("e")
elif n<50:
  print("d")
elif n<60:
  print("c")
elif n<80:
  print("b")
else: 
  print("a")


################----------------------#####################

#5
n=int(input("enter one no"))
if n%7:
  print("yes divisible by 7")
else:
  print("not divisible by 7")


################----------------------#####################

#6
a=int(input("enter first no"))
b=int(input("enter second no"))
op=input("enter operator")

dir={
  "+":a+b,
  "-":a-b,
  "*":a*b,
  "/":a/b,
  "%":a%b,
  "//":a//b
  }

if dir[op]:
  print(dir[op])
else:
  print(" input error")


################----------------------#####################

#7
n=int(input("enter a number"))
if n%5==0:
  print("hello")
else :
  print("bye")


################----------------------#####################

#8
n=int(input("enter a number"))
if n%3==0 and n%5==0 :
  print("fizzbuzz")
elif n%5==0:
  print("buzz")
elif n%3==0:
  print("fizz")
else :
  print(n)



################----------------------#####################

#9
a=input("enter a char")
vow=["a","e","i","o","u"]
if a in vow:
  print("vowel")
else:
  print("consonent")


################----------------------#####################

#10
n=float(input("enter your marks till 100"))
if n>=90 and n<=100:
  print("A")
elif n>=80:
  print("b")
elif n>=70:
  print("c")
else:
  print("fail")


################----------------------#####################

#11
age=int(input("enter your age= "))
if age<13:
  print("child")
elif age>=13 and age<=19:
  print("teenager")
else:
  print("adult")


################----------------------#####################

#12
a=input("enter a char")
upp=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
low=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
dig=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

if a in upp:
  print("upper")
elif a in low:
  print("lower")
elif a in dig:
  print("digit")
else:
  print("symbol")


################----------------------#####################

#13
color=input("give a traffic colour").capitalize()

traffic={
  "Red":"Stop",
  "Yellow":"Get Ready",
  "Green":"Go"
}
if color in traffic:
  print(traffic[color])
else:
  print("wrong input")


################----------------------#####################

#14
age=int(input("enter your age= "))
experience=int(input("enter your worked years= "))
if age>18 and experience>=2:
  print("eligible")
else:
  print("not eligible")


################----------------------#####################

#15
temp=float(input("enter temperature= "))

if temp>30:
  print("It's hot, stay hydrated!")
elif temp<15:
  print("It's cold, wear warm clothes")
else:
  print("enjoy the weather")


################----------------------#####################

#16
item=input("enter item to eat").capitalize()
menu={
  "Pizza":"$10",
  "Burger":"7",
  "Pasta":"$8"
}
if item in menu:
  print(menu[item])
else:
  print("not in menu")


################----------------------#####################

#17
height=float(input("enter your height in feet"))
if height>=6:
  print("selected")
else:
  print("not selected")


################----------------------#####################

#18
age=int(input("enter your age"))
if age>=18:
  print("allowed")
else:
  print("not allowed")


################----------------------#####################

#19
name=input("enter username")
passcode=input("enter passpord")
credintials={
  "Username": "admin", 
  "Password": "password123"
}

if name == credintials["Username"] and passcode==credintials["Password"]:
  print("access granted")
else:
  print("access denied")


################----------------------#####################

#20
n=int(input("enter a number  between 1-12= "))
if n in (12,1,2):
  print("winter")
elif n in (3,4,5):
  print("spring")
elif n in (6,7,8):
  print("summer")
elif n in (9,10,11):
  print("autumn")
else:
  print(f"wrong number {n}")


################----------------------#####################

#21
Salary=float(input("enter your salary= "))
credit_score=float(input("enter your credit score= "))
if Salary>=50000 and credit_score>=700:
  print("eligible")
else:
  print("not eligible")



################----------------------#####################


#22
num=float(input("enter a number"))
if num>1 and num<100:
  print("lies between 1 and 100")
else:
  print(f"doesnt lies between 1 and 100, number is {num}")
  

################----------------------#####################
