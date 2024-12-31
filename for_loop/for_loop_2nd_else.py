#1
for i in range(1,11):
  print("softwarica")

#2
lst=[1,2,3,4,5]
sum=0
for i in lst:
  sum+=i
print(sum)  

#3
lst=[1,2,3,4,5]
for i in range(0,len(lst)):
  print(lst[i])

#4
lst=[1,"a","c",2,3,4]
for i in lst:
  if type(i)==int:
    print(i)

#5
list=[4,5,3,2]
mul=1
for i in list:
  mul*=i
print(mul)

#6
n=int(input("enter a num: "))
for i in range(1,11):
  print(f"{n}*{i}= {n*i}") 

#7
list=[4,5,3,2]
reverse_list=[]
for i in range(-1,-len(list)-1,-1):
  reverse_list.append(list[i])
print(reverse_list)  

#8
list=[1,2,3,4]
new_list=[]
for i in list:
  new_list.append(i+1)
print(new_list)

#9
lst=[1,2,3,4] 
for i in lst:
  if i==1 or i==4:
    print(i)

#10
lst=[1,2,3,4] 
for i in lst:
  if i==1 or i==4 or i==2:
    print(i)

#11
lst = [1, 2, 3, 4]
ind=0
for i in lst:
  if i==2:
    lst[ind]="a"
  elif i==3:
    lst[ind]=2
  else:
    pass
  ind+=1

print(lst)

#12
lst=[1,2,3,4,5]
even=[]
odd=[]
for i in lst:
  if i%2==0:
    even.append(i)
  else:
    odd.append(i)

print(f"even={even}\n odd={odd}")

#13
list=[1,2,3,"d",4,5,"a"]
in_t=[]
st_r=[]
for i in list:
  if isinstance(i, int):
    in_t.append(i)
  else:
    st_r.append(i)
   
print(f"in_t={in_t}\n st_r={st_r}")

#14
list=[1,2,3,4,"a","b"]
in_t=[]
st_r=[]
for i in list:
  if isinstance(i, int):
    in_t.append(i)
  else:
    st_r.append(i)
   
print(f"in_t={in_t}\n st_r={st_r}")

#15
string=input("enter a string: ")
digit=0
letters=0
space=0
for i in string:
  if i.isdigit():
    digit+=1
  elif i.isalpha():
    letters+=1
  elif i==" ":
    space+=1
  else:
    pass

print(f"digit={digit}\nletters={letters}\nspace={space}")

#16
list=["aayush","12345678"]
user_name=input("enter your username: ")
password=input("enter your password: ")
a=False
b=False
for i in list:
  if user_name==i:
    a=True
  elif password==i:
    b=True
  else:
    pass
print("valid") if a and b else print("not valid")

#17
num=int(input("enter a num: "))
if num%2==0:
  print("even")
else:
  print("odd")

#18
num=4
fact=1
for i in range(1,num+1):
  fact*=i
print(fact)

#19
for i in range(1,9):
  for j in range(1,11):
    print(f"{i}*{j}= {i*j}")

#20
lst=[1,2,3,4] 
for i in lst:
  if i!=1 and i!=2:
    continue
  print(i)

#21
sum=0
for i in range(1,11):
  if i%2!=0:
    sum+=i
print(sum)

#22
sum=0
for i in range(1,11):
  if i%2==0:
    sum+=i
print(sum)

#23
space=0
string=input("enter a string : ")
for i in string:
  if i.isspace():
    space+=1
print(space)


#24
lst=[1,2,3,4]
for i in range(0,len(lst)):
  lst[i]=(lst[i])**3
print(lst)

#25
a="programming"
b=""
for i in range(-1,-len(a)-1,-1):
  b+=a[i]
print(b)

#26
for i in range(50):
  if i>7:
    break
  print(i)
    
#27
str="sdfgdfhg"
for i in str:
  print(i)

#28
a=["ram","shyam",1,2] 
for i in a:
  print(f'"hello!,{i}"')

#29
a=["ram","shyam"] 
lst=[]
for i in a:
  lst.append(f"Dr.{i}")
print(lst)

#30
lst=[1,2,3,4,5]
new_list=[]
for i in lst:
  new_list.append(i**2)
print(new_list)

#31
lst1=[111, 32, -9, -45, -17, 9, 85, -10]
newlst=[]
for i in lst1:
  if i>0:
    newlst.append(i)
  else:
    continue
print(newlst)

#32
list=[0,1,2,3,4,5,6]
for i in list:
  if i==3 or i==6:
    continue
  else:
    print(i)

#33
list1=[1,"sdf",True,{},1.23]
list2=[]

for i in list1:
  typ=type(i)
  list2.append(typ)

print(list2)

#34
for i in range(4):
  pass
else:
  print("excecuted sucessfully")

#35
for i in range(105,6,-7):
  print(i)

#36
bad_chars = [';', ':', '!', "*"," "]
string = "py;th* o:n ! ;py * t*h:o !n"
newstr=""
for i in string:
  if i in bad_chars:
    continue
  else:
    newstr+=i
print(newstr)

#37
even=0
odd=0
for i in range(80):
  if i%2==0:
    even+=1
  else:
    odd+=1
print("even= ",even)
print("odd= ",odd)

#38
sum=0
for i in range(3,99):
  if i%3==0 or i%5==0:
    sum+=1
  else:
    continue
print(sum)

#39
even=0
odd=0
for i in range(1,101):
  if i%2==0:
    even+=i
  else:
    odd+=i
print("even= ",even)
print("odd= ",odd)

#40
num=1221
strnum=str(num)
reverse_str=""
for i in range(-1,-len(strnum)-1,-1):
  reverse_str+=strnum[i]
if strnum==reverse_str:
  print("is a palindrome")
else:
  print("not a palindrome")

#41
num=153
str_n=str(num)
sum=0
for i in str_n:
  n=int(i)
  sum+=n**len(str_n)

if num==sum:
  print("is an amstrong")
else:
  print("not an amstrong")

#42
tup=("a","e","i","o","u")
str_1="aeiou223sr"
str_2=""
for i in str_1:
  if i in tup:
    continue
  else:
    str_2+=i
print(str_2)


#43
num=6
sum=0
for i in range(1,num):
  if num%i==0:
    sum+=i
  else:
    continue
if sum==num:
  print("perfect num")
else:
  print("not perfect num")


#44
a=[1,2,3,4,5] 
b=[3,4,5,6,7]
c=[]
for i in a:
  if i in b:
    c.append(i)
  else:
    continue
print(c)

#45
num=13
for i in range(2,num):
  if num%i==0:
    print("not a prime no its multiple is=",i)
    break
  else:
    continue
else:
  print("a prime number")




