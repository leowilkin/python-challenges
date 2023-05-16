# Challenge 52
#for i in range(0,3,1):
  #print("You Win!")
#print("Congratulations")

# Challenge 53
#for i in range(10, -1, -1):
 # print(i)

# Challenge 54
#ttChoice = int(input("What times table would you like displayed? Enter from 2 to 12 as an integer."))
#for i in range(1, 13, 1):
 # print(i*ttChoice)

# Challenge 55
#print("Please input two positive integers, a and b where b is #larger than a.")
#a = int(input("What is your a integer? "))
#b = int(input("What is your b integer? "))
#bEdit = b + 1
#if a > b:
#  print("Oops! a is bigger than b. Try again.")
#else:
 # if a // int(13):
 #   for i in range(a, bEdit, 13):
 #     print(i)
 # else:
 #   a + int(1)

# Challenge 55 #2
#print("Please input two positive integers, a and b where b is larger than a.")
#a = int(input("What is your a integer? "))
#b = int(input("What is your b integer? "))
#finalNumber = ""
#divider = int(input("Enter the number you'd like to check if there are any #numbers in your series that that number can be divided by. "))
#check = False
#if a > b:
#  print("Oops! a is bigger than b. Try again.")
#else:
#  while check == False:
#    if a > int(divider):
#      if a % int(divider) == 0:
#        finalNumber = finalNumber + str(a) + " "
#      else: a + int(1)  
#    if a > b:
#      check = True
# Challenge 56
# Program tested

# Challenge 57
#for i in range(0, 101, 5):
#  print(i, end = " ")

# Challenge 58
#monday = float(input("Enter your overtime for Monday: "))
#tuesday = float(input("Enter your overtime for Tuesday: "))
#wednesday = float(input("Enter your overtime for Wednesday: "))
#thursday = float(input("Enter your overtime for Thursday: "))
#friday = float(input("Enter your overtime for Friday: "))
#total_week = monday + tuesday + wednesday + thursday + friday
#print("Total Week:", total_week)

# Challenge 59
#number = 0
#print("Enter 5 numbers between 1.0 and 10.0")
#n1 = float(input("enter your first number"))
#n2 = float(input("enter your second number"))
##n3 = float(input("enter your third number"))
#n4 = float(input("enter your fourth number"))
#n5 = float(input("enter your fifth number"))
##if n1 == int:
 ## number += 1
#if n2 == int:
#  number += 1
#if n3 == int:
#  number += 1
#if n4 == int:
#  number += 1
#if n5 == int:
#  number += 1
#print(number)

# Challenge 59 #2
#print("Enter 5 numbers between 1.0 and 10.0")
#n1 = float(input("enter your first number"))
#n1int = int(n1)
#n2 = float(input("enter your second number"))
#n2int = int(n2)
#n3 = float(input("enter your third number"))
#n3int = int(n3)
#n4 = float(input("enter your fourth number"))
#n4int = int(n4)
#n5 = float(input("enter your fifth number"))
#n5int = int(n5)
#number = [n1, n2, n3, n4, n5]
#integer = [n1int, n2int, n3int, n4int, n5int]
#for n in range(0,5):
  #if number[n] == integer[n]:
    #  print(number[n])
  
# Challenge 60
#for i in range(1, 13, 1):
#  ans = i * 7
#  print("7 x", i, "=", ans)

# Challenge 61
#option = input("Choose your preferred unit of measurement: (cm/in) ")
#if option == "cm":
#  for i in range(10, 21, 5):
#    for q in range(10, 13, 2):
#      print(i * q)
#elif option == "in":
#  for i in range(4, 9, 2):
#    for q in range(4, 6, 1):
#      print(i * q)

# Challenge 62
#lengths = int(input("Number of lengths swam by Jane: "))
#if lengths > int(150) or lengths < int(10):
#  print("ERROR. Terminal meltdown")
#else:
#  print("Data accepted")

# Challenge 63
#day = 0
#totalLengths = 0
#lengths = int(input("Enter number of lengths: "))
#while lengths != -1:
  #day = day + 1
 #  totalLengths = totalLengths + lengths
 # lengths = int(input("Enter number of lengths, -1 to end: "))

#averageLengths = totalLengths / day
#round(averageLengths)
#print("Average daily number of lengths: ",averageLengths)

# Challenge 64
#day = 0
#totalLengths = 0
#moreData = True
#print("Enter -1 when no more data")
#while moreData:
#  lengths = int(input("Enter number of lengths on day "\
 #                     + str(day + 1) + ": "))
#  if lengths != -1:
#    day = day + 1
##    totalLengths = totalLengths + lengths
#  else:
#    moreData = False
#averageLengths = totalLengths / day
#print("Average daily lengths: ", round(averageLengths, 1))

# Challenge 65
#print("Enter runner name e.g. King, R; and then input runner time. When finished, input xxx for runner name")
#moreData = True
#time = 0
#averageTime = 0
#numberRunners = 0
#finalTime = 0
#while moreData:
#  name = input("Enter runner name: (King, R) ")
 # if name == 'xxx':
#    moreData = False
 #   finalTime = averageTime / numberRunners
 #   print("Over ", numberRunners, "runners, the average time in seconds was ", finalTime, ".")
#  else: 
 #   numberRunners = numberRunners + 1
  #  time = float(input("Enter time in seconds for "+ name + ": "))
  #  averageTime = averageTime + time

# Challenge 66 - 68
# All program files - N/A

# Challenge 69
##diverScore = 0
#benchmark = 1
#newData = True
#numberDivers = 0
#averageDivers = 0
#allDivers = 0
#print("Enter name of diver, and then score out of 10 e.g. 7.5")
#while newData:
#  diverName = input("Enter diver name: ")
#  if diverName != "xxx":
#    numberDivers = numberDivers + 1 
#    diverScore = float(input("Enter score out of 10 for "+diverName+": "))
#    allDivers = allDivers + diverScore
#    if diverScore > 10:
#      print("Error. Score too large")
#      diverScore = input("Enter score out of 10 for "+diverName+": ")
#    if diverScore > benchmark:
#      benchmark = diverScore
#      bestDiver = diverName
#  else:
#    newData = False

#print("Best diver: "+ str(bestDiver)+", with score of: "+str(benchmark))
#averageDivers = allDivers / numberDivers
#print("Average score:")
#print(averageDivers)

# Challenge 70
#Year = 0
#maxYear = 0
#minYear = 3000
##recentYear = 0
#print("Input the name and year of five Olympic Games.")

#for i in range(1, 6, 1):
#  Game = input("Enter location of game: ")
#  Year = input("Enter date of game: ")
#if int(Year) > int(maxYear):
#   maxYear = Year
##   recentYear = Year
 #  recentLocation  = Game
 #  if int(Year):
 #    print("Most recent games were in "+recentYear+" hosted at "+recentLocation)

# Fin
