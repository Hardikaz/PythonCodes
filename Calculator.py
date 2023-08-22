#Lets make a calculator

num1=input("Enter a Number ")
num2=input("Enter another Number ")

op=input("Enter the operation you want to perform ")

if op=="+":
    sm=int(num1)+int(num2)
    print(sm)

elif op=="-":
    dif=int(num1)-int(num2)
    print(dif)
   
elif op=="*":
    pro=int(num1)*int(num2)
    print(pro)

elif op=="/":
    div=int(num1)//int(num2)
    print(div)
