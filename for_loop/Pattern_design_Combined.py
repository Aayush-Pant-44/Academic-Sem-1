for row in range(7):
  #A
  for col in range(6):
    if (col==0 or col==4) and (row!=0):
      print("*",end=" ")
    elif (col==1 or col==2 or col==3) and (row==3 or row==0):
      print("*",end=" ")
    else:
      print(end="  ")
#A
  for col in range(6):
    if (col==0 or col==4) and (row!=0):
      print("*",end=" ")
    elif (col==1 or col==2 or col==3) and (row==3 or row==0):
      print("*",end=" ")
    else:
      print(end="  ")   
#Y
  for col in range(6):
    if (col==0 or col==4) and row==0:
      print("*",end=" ")
    elif (col==1 or col==3) and row==1:
      print("*",end=" ")
    elif (col==2) and (row!=0 and row!=1):
      print("*",end=" ")
    else:
      print(end="  ")
#U
  for col in range(6):
    if (col==0 or col==4) and (row!=6):
      print("*",end=" ")
    elif (col==1 or col==2 or col==3) and (row==6):
      print("*",end=" ")
    else:
      print(end="  ")
#S
  for col in range(5):
    if (col==0) and (row==1 or row==2):
      print("*",end=" ")
    elif (col==3) and (row==4 or row==5):
      print("*",end=" ")
    elif (col==1 or col==2) and (row==0 or row==3 or row==6):
      print("*",end=" ")
    else:
      print(end="  ")
#H
  for col in range(5):
    if (col==0 or col==3):
      print("*",end=" ")
    elif (col==1 or col==2) and (row==3):
      print("*",end=" ")
    else:
      print(end="  ")
  print()