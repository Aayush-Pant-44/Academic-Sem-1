#1
lst=[1,2,3,4]
reverse_list=[]
for i in range(-1,-len(lst)-1,-1):
  reverse_list.append(lst[i])
print(reverse_list)

#2
a="python" 
b=""
for i in range(len(a)-1,-1,-1):
  b+=a[i]
print(b)

#3
n=int(input("enter any number: "))
for i in range(1,11,1):
  print(f"{n}*{i}={n*i}")

#4
lst=["apple", "banana", "cherry"]
for i in lst:
  print(i)

#5
#a
for i in range(0,20,2):
  print(i)

#b
for i in range(1,20,2):
  print(i)

#6
for i in range(10,301,10):
  print(i)

#7
for i in range(105,6,-7):
  print(i)

#8
num=int(input("enter a num : "))
fact=1
for i in range (1,num+1):
  fact*=i
print(f"factoral of {num}= {fact}")

#9
num=int(input("enter a no: "))
str_1=str(num)
str_2=""
for i in range(-1,-len(str_1)-1,-1):
  str_2+=str_1[i]
num_2=int(str_2)
print(num_2)

#10
myList = "Parameter"
len=0
for i in myList:
  len+=1
print(len)


#11
Sample_list = [8,2,3,-1,7]
mul=1
for i in Sample_list:
  mul*=i
print(mul)

#12
Sample_list = [8, 2, 3, 0, 7]
sum=0
for i in Sample_list:
  sum+=i
print(sum)

#13
str=input("enter a string: ")
index=0
for i in str:
  if index%2==0:
    print(i)
  index+=1

#14
str=input("enter a string: ")
index=0
for i in str:
  if index%2!=0:
    print(i)
  index+=1

#15
sum=0
for i in range(1,11):
  sum+=i
print(sum)

#16
lst=[1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in lst:
  if i%2==0:
    print(i)


#17
lst=[1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in lst:
  if i%2!=0:
    print(i)

#18
for i in range(1,101):
  if i%5==0:
    print(i)

#19
lst=[3, 7, 9, 9, 5]
a=lst[0]
for i in range(1,len(lst)):
  if a>lst[i]:
    a=a
  elif lst[i]>a:
    a=lst[i]
  else:
    a=a
print(a)
    
#20
for i in range(1,11):
  print(i**2)

#21
for i in range(1,6):
  print(i**3)

#22
str="Python"
for i in str:
  print(i)

#23
for i in range(1,50):
  if i%3==0 and i%5==0:
    print(i)
