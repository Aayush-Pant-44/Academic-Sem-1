#1
a = [1, 2, 3, 4]
for i in range(len(a)-1, -1, -1):
    print(a[i], end=" ")

#2
a = "python"
for i in range(len(a)-1, -1, -1):
    print(a[i], end="")

#3
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(n, "x", i, "=", n*i)

#4
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

#5a
for i in range(2, 21, 2):
    print(i, end=" ")

#5b
for i in range(1, 20, 2):
    print(i, end=" ")

#6
for i in range(10, 301, 10):
    print(i, end=" ")

#7
for i in range(105, 6, -7):
    print(i, end=" ")

#8
n = int(input("Enter a number: "))
factorial = 1
for i in range(1, n+1):
    factorial *= i
print(factorial)

#9
n = input("Enter a number: ")
for i in range(len(n)-1, -1, -1):
    print(n[i], end="")

#10
myList = "Parameter"
count = 0
for char in myList:
    count += 1
print(count)

#11
sample_list = [8, 2, 3, -1, 7]
product = 1
for num in sample_list:
    product *= num
print(product)

#12
sample_list = [8, 2, 3, 0, 7]
total = 0
for num in sample_list:
    total += num
print(total)

#13
string = input("Enter a string: ")
for i in range(0, len(string), 2):
    print(string[i], end="")

#14
string = input("Enter a string: ")
for i in range(1, len(string), 2):
    print(string[i], end="")

#15
n = 10
total = 0
for i in range(1, n+1):
    total += i
print(total)

#16
sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in sample_list:
    if num % 2 == 0:
        print(num, end=" ")

#17
sample_list = [12, 13, 14, 15, 16, 17, 18, 19]
for num in sample_list:
    if num % 2 != 0:
        print(num, end=" ")

#18
for i in range(1, 101):
    if i % 5 == 0:
        print(i, end=" ")

#19
sample_list = [3, 7, 2, 8, 5]
largest = sample_list[0]
for num in sample_list:
    if num > largest:
        largest = num
print(largest)

#20
for i in range(1, 11):
    print(i**2, end=" ")

#21
for i in range(1, 6):
    print(i**3, end=" ")

#22
for char in "Python":
    print(char, end=" ")

#23
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print(i, end=" ")
