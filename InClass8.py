

num1 = int(input("Please enter the first number"))

num2 = int(input("Pleasee enter the second number"))

num3 = int(input("PLease enter the third number"))

num4 = int(input("please enter the fourth number"))

num5 = int(input("Please enter the fifth number"))


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




## for the lowest

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
