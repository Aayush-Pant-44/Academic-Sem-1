#1
while True:
  inp=int(input(" enter your age: "))
  if inp<18:
    print("you are a minor")
  elif inp<60:
    print("you are an adult")
  else:
    print("You are a senior citizen.")
  in2=input("enter stop to stop this loop: ")
  if in2=="stop":
    break
  else:
    pass

#2
#a
while True:
  inpu=input("enter the name of vechicle: ")
  if inpu=="bus":
    print("finally the wait is over")
    break
  else:
    print("wating")
    continue

#b
a=True
while a:
  inpu=input("enter the name of vechicle: ")
  if inpu=="bus":
    print("finally the wait is over")
    a=False
  else:
    print("wating")
    a=True

#3

while True:
  a=input("enter a fruit name: ")
  if a=="apple":
    print("You got it")
    break
  else:
    b=input("enter  try to try again: ")
    if b=="try":
      continue
    else:
      break


#4
password="open sesame"

while True:
  User_pass=input("guess the password: ")
  if User_pass==password:
    print("Access granted")
    break
  else:
    print("try again wrong password")

#5
day="sunday"
while True:
  user_inp=input("guess the day: ")
  if user_inp==day:
    print(" Enjoy your weekend")
    break
  else:
    print("It's not the weekend yet")
    continue


#6
import random
random_num=random.randint(1,10)
at=0
while True:
  
  input_user=int(input("guess a random number from 1 to 10 : "))
  
  if input_user==random_num:
    print(f"Right attempts={at}")
    break
  elif input_user>random_num:
    print("go lower")
  else:
    print("go higher")
  at+=1


#7

at=0
user_name="admin"
pass_word="1234"

while True:
  userName=input("enter your username: ")
  passWord=input("enter your passWord: ")
  if at==3:
    print("Too many failed attempts.")
    break
  elif user_name==userName and pass_word==passWord:
    print("login success: ")
    break
  else:
    print("invalid credintials try again")
    at+=1

#8
import random
while True:
  rand_num_1=random.randint(1,30)
  rand_num_2=random.randint(1,30)
  print(rand_num_1,rand_num_2)
  rand_mul=rand_num_1*rand_num_2
  user_guess=int(input("enter the multiplication of both numbers: "))

  if rand_num_1==user_guess:
    print("correct")
    continue
  else:
    print("incorrect try again: ")
    user_input=input("for terminale the loop type 'exit': or anything to continue")

    if user_input=="exit":
      break
    else:
      continue

#9
while True:
  num=int(input("enter a number: "))
  for i in range(2,num):
    if num%i==0:
      print("not a prime no ")
      break
    else:
      print("prime number")
      break
  he=input("ennter  exit to exit the code")

  if he=="exit":
    break
  else:
    continue

#10
pew_defin="python"

while True:
  it=input("enter the word")
  if it==pew_defin:
    in1=input("enter exit to exit the program")
    if in1=="exit":
      break
    else:
      continue
  else:
    print("incorrect try again")
    continue


#11
count=0
while True:
  in1=input("enter a phrase: ")
  if in1=="good luck":
    count+=1

    if count==3:
      print('you typed good luck 3 times')
      break
    else:
      print(f"you typed the same word {count} times")
  else:
    continue