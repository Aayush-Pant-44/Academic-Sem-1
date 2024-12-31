#A
for row in range(6):
  for col in range(5):
    if (col==0 or col==4) and (row!=0):
      print("*",end=" ")
    elif (col==1 or col==2 or col==3) and (row==3 or row==0):
      print("*",end=" ")
    else:
      print(end="  ")
  print()

#A
for row in range(6):
  for col in range(5):
    if (col==0 or col==4) and (row!=0):
      print("*",end=" ")
    elif (col==1 or col==2 or col==3) and (row==3 or row==0):
      print("*",end=" ")
    else:
      print(end="  ")
  print()

#Y
for row in range(6):
  for col in range(5):
    if (col==0 or col==4) and row==0:
      print("*",end=" ")
    elif (col==1 or col==3) and row==1:
      print("*",end=" ")
    elif (col==2) and (row!=0 and row!=1):
      print("*",end=" ")
    else:
      print(end="  ")
  print()

#U
for row in range(5):
  for col in range(5):
    if (col==0 or col==4) and (row!=4):
      print("*",end=" ")
    elif (col!=0 and col!=4) and (row==4):
      print("*",end=" ")
    else:
      print(end="  ")
  print()


#S
for row in range(7):
  for col in range(4):
    if (col==0) and (row==1 or row==2):
      print("*",end=" ")
    elif (col==3) and (row==4 or row==5):
      print("*",end=" ")
    elif (col==1 or col==2) and (row==0 or row==3 or row==6):
      print("*",end=" ")
    else:
      print(end="  ")
  print()

#H
for row in range(7):
  for col in range(4):
    if (col==0 or col==3):
      print("*",end=" ")
    elif (col==1 or col==2) and (row==3):
      print("*",end=" ")
    else:
      print(end="  ")
  print()

































