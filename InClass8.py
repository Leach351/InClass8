

#github.com/Leach351/InClass8.git




num1Prob = True
num2Prob = True
num3Prob = True
num4Prob = True
num5Prob = True
num6Prob = True
num7Prob = True
num8Prob = True
num9Prob = True
num10Prob = True

while num1Prob == True:

    num1 = int(input("Please enter the first number :"))

    if num1 >= 0 and num1 <= 1000:
        num1Prob =False
    else:
        print ("Error num not in Range")

while num2Prob == True:
    num2 = int(input("Pleasee enter the second number :"))

    if num2 >= 0 and num2 <=1000:
        num2Prob = False
    else:
        print ("Error num not in Range")


while num3Prob == True: 
    num3 = int(input("PLease enter the third number :"))

    if num3 >= 0 and num2 <= 1000:
        num3Prob = False
    else:
        print ("Error num not in Range") 
        
    
while num4Prob == True:
    num4 = int(input("please enter the fourth number :"))
        
    if num4 >= 0 and num4 <= 1000:
        num4Prob = False
    else:
        print ("Error num not in Range")    


while num5Prob == True:
    num5 = int(input("Please enter the fifth number :"))

    if num5 >= 0 and num5 <= 1000:
        num5Prob = False
    else:
        print ("Error num not in Range")

while num6Prob == True:

    num6 = int(input("Please enter the sixth number :"))

    if num6 >= 0 and num6 <= 1000:
        num6Prob =False
    else:
        print ("Error num not in Range")

while num7Prob == True:
    num7 = int(input("Pleasee enter the seventh number :"))

    if num7 >= 0 and num7 <=1000:
        num7Prob = False
    else:
        print ("Error num not in Range")


while num8Prob == True: 
    num8 = int(input("PLease enter the eighth number :"))

    if num8 >= 0 and num8 <= 1000:
        num8Prob = False
    else:
        print ("Error num not in Range") 
        
    
while num9Prob == True:
    num9 = int(input("please enter the ninth number :"))
        
    if num9 >= 0 and num9 <= 1000:
        num9Prob = False
    else:
        print ("Error num not in Range")    


while num10Prob == True:
    num10 = int(input("Please enter the tenth number :"))

    if num10 >= 0 and num10 <= 1000:
        num10Prob = False
    else:
        print ("Error num not in Range")    


## for lowest

largest = 0
smallest = 0



if num1 < num2 and num1 < num3 and num1 < num4 and num1 < num5 and num1 < num6 and num1 < num7 and num1 < num8 and num1 < num9 and num1 < num10:

    smallest = num1

elif num2 < num1 and num2 < num3 and num2 < num4 and num2 < num5 and num2 < num6 and num2 < num7 and num2 < num8 and num2 < num9 and num2 < num10:

    smallest = num2

elif num3 < num1 and num3 < num2 and num3 < num4 and num3 < num5 and num3 < num6 and num3 < num7 and num3 < num8 and num3 < num9 and num3 < num10:

    smallest = num3

elif num4 < num1 and num4 < num2 and num4 < num3 and num4 < num5 and num4 < num6 and num4 < num7 and num4 < num8 and num4 < num9 and num4 < num10:

    smallest = num4

elif num5 < num1 and num5 < num2 and num5 < num3 and num5 < num4 and num5 < num6 and num5 < num7 and num5 < num8 and num5 < num9 and num5 < num10:
   smallest = num5

elif num6 < num1 and num6 < num2 and num6 < num3 and num6 < num4 and num6 < num5 and num6 < num7 and num6 < num8 and num6 < num9 and num6 < num10:
   smallest = num6

elif num7 < num1 and num7 < num2 and num7 < num3 and num7 < num4 and num7 < num5 and num7 < num6 and num7 < num8 and num7 < num9 and num7 < num10:
    smallest = num7

elif num8 < num1 and num8 < num2 and num8 < num3 and num8 < num4 and num8 < num5 and num8 < num6 and num8 < num7 and num8 < num9 and num8 < num10:
    smallest = num8

elif num9 < num1 and num9 < num2 and num9 < num3 and num9 < num4 and num9 < num5 and num9 < num6 and num9 < num7 and num9 < num8 and num9 < num10:
    smallest = num9

else:
    smallest = num10







## for the largest

if num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5 and num1 > num6 and num1 > num7 and num1 > num8 and num1 > num9 and num1 > num10:

    largest= num1

elif num2 > num1 and num2 > num3 and num2 > num4 and num2 > num5 and num2 > num6 and num2 > num7 and num2 > num8 and num2 > num9 and num2 > num10:

    largest = num2

elif num3 > num1 and num3 > num2 and num3 > num4 and num3 > num5 and num3 > num6 and num3 > num7 and num3 > num8 and num3 > num9 and num3 > num10:

    largest = num3

elif num4 > num1 and num4 > num2 and num4 > num3 and num4 > num5 and num4 > num6 and num4 > num7 and num4 > num8 and num4 > num9 and num4 > num10:

    largest = num4

elif num5 > num1 and num5 > num2 and num5 > num3 and num5 > num4 and num5 > num6 and num5 > num7 and num5 > num8 and num5 > num9 and num5 > num10:
    largest = num5

elif num6 > num1 and num6 > num2 and num6 > num3 and num6 > num4 and num6 > num5 and num6 > num7 and num6 > num8 and num6 > num9 and num6 > num10:
    largest = num6

elif num7 > num1 and num7 > num2 and num7 > num3 and num7 > num4 and num7 > num5 and num7 > num6 and num7 > num8 and num7 > num9 and num7 > num10:
    largest = num7

elif num8 > num1 and num8 > num2 and num8 > num3 and num8 > num4 and num8 > num5 and num8 > num6 and num8 > num7 and num8 > num9 and num8 > num10:
    largest = num8

elif num9 > num1 and num9 > num2 and num9 > num3 and num9 > num4 and num9 > num5 and num9 > num6 and num9 > num7 and num9 > num8 and num9 > num10:
    largest = num9

else:

    largest = num10


print("The smallest number is: ", smallest, "The largest number is: ", largest)






