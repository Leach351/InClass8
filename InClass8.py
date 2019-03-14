
num1Prob = True
num2Prob = True
num3Prob = True
num4Prob = True
num5Prob = True

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


## for lowest
if num1 < num2 and num1 < num3 and num1 < num4 and num1 < num5:

    print ("The smallest number is ", num1)

elif num2 < num1 and num2 < num3 and num2 < num4 and num2 < num5:

    print ("The smallest number is ", num2)

elif num3 < num1 and num3 < num2 and num3 < num4 and num3 < num5:

    print ("the smallest number is ", num3)

elif num4 < num1 and num4 < num2 and num4 < num3 and num4 < num5:

    print ("the smallest number is", num4)

else:
    print ("the smallest number is", num5)




## for the largest

if num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5:

    print ("The largest number is ", num1)

elif num2 > num1 and num2 > num3 and num2 > num4 and num2 > num5:

    print ("The largest number is ", num2)

elif num3 > num1 and num3 > num2 and num3 > num4 and num3 > num5:

    print ("the largest number is ", num3)

elif num4 > num1 and num4 > num2 and num4 > num3 and num4 > num5:

    print ("the largest number is", num4)

else:
    print ("the largest number is", num5)




