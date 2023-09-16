a = int(input("Enter Your First Number : "))
b = int(input("Enter Your Second Number : "))

ope = input("Choose a operation to execute (+,-,/,*,%) : ")

if ope =="+":
    print("Your Answer Is : ",a+b)

elif ope == "-":
    print("Your Answer Is : ", a-b)

elif ope == "/":
    print("Your Answer Is : ", a/b)

elif ope == "*":
    print("Your Answer Is : ", a*b)

elif ope == "%":
    print("Your Answer Is : ", a%b)

else:
    print("INVALID INPUT !!!")