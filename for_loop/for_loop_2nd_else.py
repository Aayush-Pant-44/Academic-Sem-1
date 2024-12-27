#1
for i in range(10):
    print("softwarica")

#2
lst = [1, 2, 3, 4]
sum = 0
for num in lst:
    sum += num
print(sum)

#3
string = "softwarica"
for i in range(len(string)):
    print(string[i])

#4
lst = [1, "a", "c", 2, 3, 4]
for item in lst:
    if isinstance(item, int):
        print(item)

#5
lst = [4, 5, 3, 2]
mul = 1
for num in lst:
    mul *= num
print(mul)

#6
num = 5
for i in range(1, 11):
    print(num * i)

#7
lst = [1, 2, 3, 4]
lst.reverse()
print(lst)

#8
lst = [1, 2, 3, 4]
new_lst = []
for num in lst:
    new_lst.append(num + 1)
print(new_lst)

#9
lst = [1, 2, 3, 4]
print(lst[0])
print(lst[-1])

#10
lst = [1, 2, 3, 4]
for i in range(len(lst)):
    if i == 2:
        continue
    print(lst[i])

#11
lst = [1, 2, 3, 4]
lst[1] = "a"
print(lst)

#12
lst = [1, 2, 3, 4, 5]
odds = []
evens = []
for num in lst:
    if num % 2 == 0:
        evens.append(num)
    else:
        odds.append(num)
print(odds)
print(evens)

#13
lst = [1, 2, 3, "d", 4, 5, "a"]
integers = []
strings = []
for item in lst:
    if isinstance(item, int):
        integers.append(item)
    else:
        strings.append(item)
print(integers)
print(strings)

#14
lst = [1, 2, 3, 4, "a", "b"]
int_types = []
str_types = []
for item in lst:
    if isinstance(item, int):
        int_types.append(type(item))
    else:
        str_types.append(type(item))
print(int_types)
print(str_types)

#15
string = "Hello World 123"
letters = 0
digits = 0
spaces = 0
for char in string:
    if char.isdigit():
        digits += 1
    elif char.isalpha():
        letters += 1
    elif char.isspace():
        spaces += 1
print(letters)
print(digits)
print(spaces)

#16
username = "user"
password = "pass123"
if len(username) >= 3 and len(password) >= 6:
    print("Valid")
else:
    print("Invalid")

#17
num = 4
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

#18
num = 5
fact = 1
for i in range(1, num + 1):
    fact *= i
print(fact)

#19
for num in range(1, 9):
    for i in range(1, 11):
        print(num * i)

#20
lst = [1, 2, 3, 4]
print(lst[0])
print(lst[1])

#21
start = 1
end = 10
sum = 0
for num in range(start, end + 1):
    if num % 2 != 0:
        sum += num
print(sum)

#22
start = 1
end = 10
sum = 0
for num in range(start, end + 1):
    if num % 2 == 0:
        sum += num
print(sum)

#23
string = "Count spaces in this sentence."
spaces = 0
for char in string:
    if char == " ":
        spaces += 1
print(spaces)

#24
lst = [1, 2, 3, 4]
new_lst = []
for num in lst:
    new_lst.append(num ** 3)
print(new_lst)

#25
a = "programming"
print(a[::-1])

#26
for i in range(50):
    if i == 8:
        break
    print(i)

#27
string = "hello"
for char in string:
    print(char)

#28
a = ["ram", "shyam", 1, 2]
for name in a:
    if isinstance(name, str):
        print("Hello!", name)

#29
a = ["ram", "shyam"]
dr_list = []
for name in a:
    dr_list.append("Dr." + name)
print(dr_list)

#30
lst = [1, 2, 3, 4]
squares = []
for num in lst:
    squares.append(num ** 2)
print(squares)

#31
lst1 = [111, 32, -9, -45, -17, 9, 85, -10]
positive_nums = []
for num in lst1:
    if num > 0:
        positive_nums.append(num)
print(positive_nums)

#32
lst = [0, 1, 2, 3, 4, 5, 6]
for num in lst:
    if num == 3 or num == 6:
        continue
    print(num)

#33
lst = [1, "a", 2.0, True]
types = []
for item in lst:
    types.append(type(item))
print(types)

#34
for i in range(5):
    print(i)
else:
    print("Done")

#35
start = 105
step = -7
for i in range(start, 97, step):
    print(i)

#36
bad_chars = [';', ':', '!', "*"]
string = "py;th* o:n ! ;py * t*h:o !n"
new_string = ""
for char in string:
    if char not in bad_chars:
        new_string += char
print(new_string)

#37
nums = [1, 2, 3, 4, 5, 6, 7, 8]
odds = 0
evens = 0
for num in nums:
    if num % 2 == 0:
        evens += 1
    else:
        odds += 1
print(evens)
print(odds)

#38
sum = 0
for num in range(3, 100):
    if num % 3 == 0 or num % 5 == 0:
        sum += num
print(sum)

#39
sum_odd = 0
sum_even = 0
for num in range(1, 101):
    if num % 2 == 0:
        sum_even += num
    else:
        sum_odd += num
print(sum_odd)
print(sum_even)

#40
num = 121
reverse_num = str(num)[::-1]
if str(num) == reverse_num:
    print("Palindrome")
else:
    print("Not Palindrome")

#41
num = 153
sum = 0
power = len(str(num))
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** power
    temp //= 10
if sum == num:
    print("Armstrong")
else:
    print("Not Armstrong")

#42
string = "programming"
vowels = "aeiou"
new_string = ""
for char in string:
    if char not in vowels:
        new_string += char
print(new_string)

#43
num = 28
sum = 0
for i in range(1, num):
    if num % i == 0:
        sum += i
if sum == num:
    print("Perfect")
else:
    print("Not Perfect")

#44
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common = []
for num in list1:
    if num in list2:
        common.append(num)
print(common)

#45
num = 29
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")
