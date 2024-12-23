#1
price=float(input("enter the price= "))
if price>1000:
  price=price-(10/100)*price
  print(price)
elif price>=500:
  price=price-(5/100)*price
  print(price)
else:
  print(f"you dont get any discounts your final price is= {price}")

#2
prefrence_1=input("enter you prefrence as for vegterian type 'veg' and for non-veg type 'non': ")
if prefrence_1=="veg":
  prefrence_2=input("Do you want 'salad' or 'pasta': ")
  print(prefrence_2)
elif prefrence_1=="non":
  prefrence_2=input("Do you want 'chicken' or 'fish': ")
  print(prefrence_2)
else:
  print("wrong input")

#3
salary=int(input("enter your salary"))
if salary>50000:
  print("high earner")
elif salary>20000:
  print("mid earner")
else:
  print("low earner")

#4
num=int(input("enter a number: "))
if num%2==0:
  if num%5==0:
    print("Divisible by 2 and 5")
  else:
    print("Divisible by 2 only")
else:
  print('Not divisible by both')


#5
marks=int(input("enter your marks"))
if marks>50:
  if marks>90:
    print("excellent")
  else:
    print("Good")
else:
  print("fail")

#6
a=int(input("enter first no: "))
b=int(input("enter second no: "))
c=int(input("enter third no: "))

if a>=b:
  if a>=c:
    print(f"{a} is greatest")
  else:
    print(f"{c} is greater")
else:
  if b>=c:
    print(f"{b} is greater")
  else:
    print(f"{c} is largest")

#7
print("welcome to the Forest Adventure")
decision_1=input("To go left type 'left' and to go right type 'right': ")
if decision_1=="right":
  print("Game over you fell in a trap")
elif decision_1=="left":
  decision_2=input("if you want to rest type 'rest' and to explore the cave type 'explore': ")
  if decision_2=="rest":
    print("game over you were attacked by wild animals")
  elif decision_2=="explore":
    print("you win")
  else:
    print("you entered the wrong option")
else:
  print("you entered the wrong option")

#8
print("Welcome to the Jungle Survival Challenge")
decision_1=input("To search for food type 'search' and to build a shelter 'build': ")
if decision_1=="build":
  print("Your shelter collapsed in the rain. Game Over.")
elif decision_1=="search":
  decision_2=input("if you want to hunt type 'hunt' and to gather type 'gather': ")
  if decision_2=="hunt":
    print("game over you were attacked by wild animals")
  elif decision_2=="gather":
    print("you win")
  else:
    print("you entered the wrong option")
else:
  print("you entered the wrong option")

#9
print("Welcome to the Space Adventure")
decision_1=input("To land on Mars type 'land' and to fly to Jupiter 'fly': ")
if decision_1=="fly":
  print("our spaceship crashed. Game Over.")
elif decision_1=="land":
  decision_2=input("if you want to explore type 'explore' and to build a base type 'build': ")
  if decision_2=="build":
    print("You ran out of resources. Game Over.")
  elif decision_2=="explore":
    print("you win")
  else:
    print("you entered the wrong option")
else:
  print("you entered the wrong option")

#10
print("Welcome to the Haunted Castle")
decision_1=input("To enter the castle type 'enter' and to run away 'run': ")
if decision_1=="run":
  print("you escaped safely.")
elif decision_1=="enter":
  decision_2=input("choose a door 'red','green','black' ")
  if decision_2=="red":
    print("You entered a room full of flames. Game Over.")
  elif decision_2=="green":
    print("You found the treasure. You Win!")
  elif decision_2=="black":
    print("you were captured by ghosts. Game Over.")
  else:
    print("you entered the wrong option")
else:
  print("you entered the wrong option")

#11
print("Welcome to the Underwater World")
decision_1=input("To dive deeper type 'dive' and to surface 'surface': ")
if decision_1=="surface":
  print("you returned safely.")
elif decision_1=="dive":
  decision_2=input("if you want to search for pearls type 'search' and to chase the fish type 'chase': ")
  if decision_2=="search":
    print("You found a rare pearl. You Win!")
  elif decision_2=="chase":
    print("You got lost underwater. Game Over.")
  else:
    print("you entered the wrong option")
else:
  print("you entered the wrong option")

#12
print("Welcome to the Pirate Ship Adventure.")
decision_1=input("To searches for treasure type 'search' and to battle enemy ships 'battle': ")
if decision_1=="search":
  decision_2=input("if you want to dig on the island type 'dig' and to explore the cave 'explore': ")
  if decision_2=="dig":
    print("You found a hidden treasure chest. You Win!")
  elif decision_2=="explore":
    print("You were trapped inside. Game Over.")
  else:
    print("you entered the wrong option")
elif decision_1=="battle":
  decision_2=input("if you want to attack type 'attack' and to defend type 'defend': ")
  if decision_2=="attack":
    print("You won the battle. You Win!")
  elif decision_2=="defend":
    print("You were outnumbered. Game Over.")
  else:
    print("you entered the wrong option")
else:
  print("you entered the wrong option")

#13
print("Welcome to the Wizarding World")
decision_1=input("To choose spells type 'spells' and to choose potions type 'potions': ")
if decision_1=="spells":
  decision_2=input("if you want to practice magic type 'practice' and to compete in duels type 'compete': ")
  if decision_2=="practice":
    print("You mastered a powerful spell. You Win")
  elif decision_2=="compete":
    print("You lost to a rival wizard. Game Over.")
  else:
    print("you entered the wrong option")
elif decision_1=="potions":
  decision_2=input("if you want to brew an elixir 'brew' and to crete poision type 'create': ")
  if decision_2=="brew":
    print("You healed a village. You Win!")
  elif decision_2=="create":
    print("Your potion backfired. Game Over")
  else:
    print("you entered the wrong option")
else:
  print("you entered the wrong option")

#14
print("Welcome to the Cybersecurity Mission")
decision_1=input("To choose trace the hacker type 'trace' and to secure the systems type 'secure': ")
if decision_1=="trace":
  decision_2=input("if you want to track their IP type 'track' and to decode their message type 'decode': ")
  if decision_2=="track":
    print("You caught the hacker. You Win!")
  elif decision_2=="decode":
    print("The message was a trap. GameOver.")
  else:
    print("you entered the wrong option")
elif decision_1=="secure":
  decision_2=input("if you want to shut down the server 'shut' and to upgrade the firewall type 'upgrade': ")
  if decision_2=="shut":
    print("The attack was stopped. You Win!")
  elif decision_2=="upgrade":
    print("The hacker bypassed it. Game Over.")
  else:
    print("you entered the wrong option")
else:
  print("you entered the wrong option")

#15
num=int(input("enter a number: "))
if num%2==0 and num%7==0:
  print("Double seven")
elif num%2==0:
  print("Even")
elif num%7==0:
  print("lucky seven")
else:
  print(f"the num was {num}")

#16
num=int(input("enter a number: "))
if num>100:
  print("big number")
elif num>50:
  print("medium number")
else:
  print("small number")

#17
color=input("enter a color from red, yellow green: ").capitalize()
if color=="Red":
  print("stop")
elif color=="Yellow":
  print("slow down")
elif color=="Green":
  print("Go")
else:
  print("invalid signal")

#18
tempr=float(input("enter temperature in celcius: "))
if tempr>=40:
  print("Hot")
elif tempr>=20:
  print("Warm")
else:
  print("Cold")

#19
bmi=float(input("enter you BMI: "))
if bmi<18.5:
  print("underweight")
elif bmi<24.9:
  print("normal weight")
elif bmi<29.9:
  print("overweight")
else:
  print("obesity")

#20
num_1=int(input("enter first no. : "))
num_2=int(input("enter second no. : "))

if num_1%2==0 and num_2%2==0:
  print(f"Both are eve , their sum ={num_1+num_2}")
elif num_1%2==0 or num_2%2==0:
  print(f"One is even and other is odd, their difference ={num_1-num_2}")
else:
  print(f"their product={num_1*num_2}")

#21
price=int(input("enter the price: "))
if price>1000:
  price-=(20/100)*price
  print(f"the new price after 20% discount= {price}")
elif price>=500:
  price-=(10/100)*price
  print(f"the new price after 10% discount= {price}")
else:
  print("no discount")

#22
age=int(input("enter your age: "))
gender=input("enter your gender M for male and F for female: ").capitalize()
income=int(input("enter your income: "))

if age>=18 and age<60:
  if gender=="M":
    if income>1000000:
      print("tax = 30%")
    elif income>500000:
      print("tax= 20%")
    else:
      print("tax = 10%")
  elif gender=="F":
    if income>1000000:
      print("tax = 25%")
    elif income>500000:
      print("tax= 15%")
    else:
      print("tax = 5%")
  else:
    print("wrong gender")
elif age>=60:
  if gender=="M" or gender=="F":
    if income>1000000:
      print("tax = 20%")
    else:
      print("tax= 10%")
  else:
    print("wrong gender")
else:
  print("No tax for you as you are a Minor")

#23

age=int(input("enter your age: "))
gender=input("enter your gender M for male and F for female: ").capitalize()
score=float(input("enter your acadimic score: "))

if age>=18 and age<=25:
  if gender=="M":
    if score>=85:
      print("Full Scholarship")
    elif score>=70:
      print("Partial Scholarship")
    else:
      print("No Scholarship")
  elif gender=="F":
    if score>=80:
      print("Full Scholarship")
    elif score>=65:
      print("Partial Scholarship")
    else:
      print("No Scholarship")
  else:
    print("wrong gender")
else:
  print("No grading for you as you are a Minor")

#24
age=int(input("enter your age: "))
gender=input("enter your gender M for male and F for female: ").capitalize()
experience=int(input("enter your experience years: "))

if age>=21 and age<=35:
  if gender=="M":
    if experience>=5:
      print("Senior Devloper")
    else:
      print("junior Developer")
  elif gender=="F":
    if experience>=5:
      print("Sinour anylyst")
    else:
      print("Junior Analyst")
  else:
    print("wrong gender")
elif age>35:
  if gender=="M" or gender=="F":
      print("Manager role")
  else:
    print("wrong gender")
else:
  print("You dont meet the age criteria for promotion") 

#25
age=int(input("enter your age: "))
gender=input("enter your gender M for male and F for female: ").capitalize()
show_time=int(input("enter your show time for matinee type '1' or evening type '0': "))
if age<12:
  if gender=="M" or gender=="F":
    if show_time==1:
      print("ticket Rs 500")
    elif show_time==0:
      print("ticket Rs 700")
    else:
      print("Wrong input")
 
  else:
    print("wrong gender")
elif age<60:
  if gender=="M":
    if show_time==1:
      print("ticket Rs 800")
    elif show_time==0:
      print("ticket Rs 100")
    else:
      print("Wrong input")
  elif gender=="F":
    if show_time==1:
      print("ticket Rs 700")
    elif show_time==0:
      print("ticket Rs 900")
    else:
      print("Wrong input")
  else:
    print("wrong gender")
else:
  if gender=="M" or gender=="F":
    print(" Ticket = Rs600")
  else:
    print("wrong gender")


#26

age=int(input("enter your age: "))
gender=input("enter your gender M for male and F for female: ").capitalize()
membership_Type=input("enter your membership type 'mn' for monthly and 'yr' for yearly : ").capitalize()

if age>=18 and age<30:
  if gender=="M":
    if membership_Type=="Mn":
      print("Rs 50")
    elif membership_Type=="Yr":
      print("Rs 500")
    else:
      print("Wrong input")
  elif gender=="F":
    if membership_Type=="Mn":
      print("Rs 45")
    elif membership_Type=="Yr":
      print("Rs 450")
    else:
      print("Wrong input")
  else:
    print("wrong gender")
elif age<=50 and age>=30:
  if gender=="M" or gender=="F":
    if membership_Type=="Mn":
      print("Rs 60")
    elif membership_Type=="Yr":
      print("Rs 600")
    else:
      print("Wrong input")
  else:
    print("wrong gender")
elif age>50:
  if gender=="M" or gender=="F":
    if membership_Type=="Mn":
      print("Rs 40")
    elif membership_Type=="Yr":
      print("Rs 400")
    else:
      print("Wrong input")
else:
  print("No membeship for you as you are a Minor")