# QUESTION-1

# num1=input("enter the number:")
# num2=input("enter the number:")
# print(num1)
# print(num2)

# QUESTION-2

# num1=int(input("enter the number:"))
# num2=int(input("enter the number:"))
# num3=int(input("enter the number:"))
# if num1>num2 and num1>3:
#     print("maximum number",num1)
# elif num2>num1 and num2>num3:
#     print("maximum number",num2)
# elif num3>num1 and num3>num2:
#     print("maximum number",num3)
# else:
#     print("minimum number")           


# QUESTION-3

# num1=int(input("enter the number:"))
# num2=int(input("enter the number:"))
# if num1>num2:
#     print("maximum",num1)
# else:                              
#     print("maximum",num2)    


# QUESTION-4

# num1=int(input("enter the number:"))
# num2=int(input("enter the number:"))
# num3=int(input("enter the number:"))
# if num1>num2 and num1<num3 or num1<num2 and num1>num3:
#     print("middle number",num1)
# elif num2>num1 and num2<num3 or num2<num3 and num2>num3:
#     print("middle number",num2)
# else:
#     print("middle number",num3)
    

# QUESTION-5

# marks =int(input("enter the number:"))
# if marks>=80:
#     print("grade A")
# elif marks>=60 and marks<=80:
#     print("grade C")
# elif marks>=40 and marks<=60:
#     print("grade D")
# elif marks>=25 and marks<=40:
#     print("grade E")    
# else:
    # print("grade F")

# QUESTION-6

# num=int(input("Enter The Year:"))
# if num%4==0 and num%100==0:
#     print(num,"Leap Year")
# else:
#     print(num,"Not Leap Year")   


# QUESTION-7

# num=int(input("enter the number:"))
# if num<0:
#     print("negative number")
# elif num>0:
#     print("postive number")
# else:
#     print("zero")


# QUESTION-8

# num1=int(input("enter the number:"))
# num2=int(input("enter the number:"))
# num=num1*num2
# if num%5==0:
#     print("YES")
# else:
#     print("NO")


# QUESTION-9

# num1=int(input("enter the number:"))
# num2=int(input("enter the number:"))
# num3=int(input("enter the number:"))
# num4=int(input("enter the number:"))
# num5=int(input("enter the number:"))
# if num1>num2 and num1>num3 and num1>num4 and num1>num5:
#     print("maximum number",num1)
# elif num2>num1 and num2>num3 and num2>num4 and num2>num5:
#     print("maximum number",num2)
# elif num3>num1 and num3>num2 and num3>num4 and num3>num5:
#     print("maximum number",num3)
# elif num4>num1 and num4>num2 and num4>num3 and num4>num5:
#     print("maximum number",num4)    
# elif num5>num1 and num5>num2 and num5>num4 and num5>num4:
#     print("maximum number",num5)
# else:
#     print("minimum number")


# QUESTION-10

# num=int(input("enter the number:"))
# if num<12:
#     print(12-num,"girls ")
# elif num<12:
#     print("extra girls")
# # else:
# #     print("all girls")    

# QUESTION-11

# num=int(input("enter the number of girls:"))
# num1=12-num
# if num<12:
#     print(num1,"girls are less")
# elif num==12:
#     print("equal girls")    
# else:
#     print(num-num1-num," girls")

# QUESTION-12

# num1=int(input("enter the birth year:"))
# num2=int(input("enter the recent year:"))
# # a= num2-num1
# if num2-num1:
#     print(num2-num1,"AGE")
# else:
#     print("number")


# QUESTION-13

# name=(input("Enter the name:"))
# a=len(name)
# if a%2==0:
#     print(a,"even numbers")
# elif a%2!=0:
#     print(a,"odd numbers")
# else:
#     print(name)


# QUESTION-14

# Write a python program to check whether a number is divisible by 5 and 11 or not.

# num=int(input("enter the number:"))
# if num%5==0:
#     print("divisible by 5")
# elif num%11==0:
#     print("divisible by 11")
# else:
#     print("not divisible")


# QUESTIION-15

# Write a python program to check whether a character is uppercase or lowercase alphabet.


# name=input("enter the word:")
# if name>="a" and name<="z":
#     print("lowercase")
# elif name>="A" and name<="Z":
#     print("uppercase")
# else:
#     print("error")

# name=input("enter the word:")
# if name>="a" and name<="z":
#     print("lowercase")
# elif name>="A" and name<="Z":
#     print("uppercase")
# else:
#     print("error")


# QUESTION-16

# Write a python program to input week number and print week day.

# num=int(input("enter theii week number (1-7):"))
# if num==1:
#     print("Monday")
# elif  num== 2 :
#     print("Tuesday")

# elif num== 3 :
#     print("Wednesday")

# elif num==4 :
#     print("Thursday")

# elif num== 5 :
#     print("Friday")

# elif num== 6 :
#     print("Saturday")

# elif num== 7 :
#     print("Sunday")

# else :
#     print("Please enter weekday number between 1-7.") 


# QUESTION-17

# Write a python program to input the month number and print the number of days in that month

# num =int(input("enter the month number between 1 to 12:"))
# if num<13:
#     if num==2:
#         print("28 days""29 days if leap year")
#     elif num % 2==0:
#         print("30 days")
#     else:
#         print("31 days")

# QUESTION-18

# Write a python program to count the total number of notes in a given amount

# amt=int(input("enter the amount: "))
# note500=amt//500 
# note100=(amt-(note500*500))//100
# note50=(amt-(note500*500+note100*100))//50
# note10=(amt-(note500*500+note100*100+note50*50))//10
# note5=(amt-(note500*500+note100*100+note50*50+note10*10))//5
# note1=(amt-(note500*500+note100*100+note50*50+note10*10+note5*5))//1
# if(amt>=500): 
#     (note500==amt//500) 
#     (amt==amt-note500*500)
# if(amt>=100):
#     (note100==amt//100)
#     (amt==amt-note100*100)
# if(amt>=50):
#     (note50==amt//50)
#     (amt==amt-note50*50)
# if(amt>10):
#     (note10==amt//10)
#     (amt==amt-note10*10)
# if(amt>5):
#     (note5==amt//5)
#     (amt==amt-note5*5)
# if(amt>1):
#     (note1==amt//1)
#     (amt==amt-note1*1)
#     print("500" , note500)
#     print("100" ,note100 )
#     print("50" , note50)
#     print("10" ,note10)
#     print("5", note5)
#     print("1" , note1)


# QUESTION-19

# Write a python program to input all sides of a triangle and check whether the triangle is valid or not.

# a=float(input("enter the side a: "))
# b=float(input("enter the side b: "))
# c=float(input("enter the side c: "))
# if a+b>c and b+c>a and c+a>b:
#     print("triangle can be formed")
# else:
#     print("triangle is not formed")


# QUESTION-20

# A shop will give a discount of 10% if the cost of the purchased quantity is more than 1000. Ask the user for quantity, Suppose, one unit will cost 100. Judge and print total cost for user.


# user=int(input("enter the quantity:"))
# amt=user*100
# discount=amt*10/100
# if amt>=1000:
#     print(discount,"discount amount")
#     print(amt-discount)
# else:
#     print(amt,"no discount")

# QUESTION-21

#  Take the age of 3 people by user and determine oldest and youngest among them.

# num1=int(input("enter the age: "))
# num2=int(input("enter the age: "))
# num3=int(input("enter the age: "))
# if  num1>num2 and num1>num3:
#     print("oldest",num1)
# if  num2<num1 and num2>num3:
#     print("younger",num2)
# else:
#     print("child",num3)     

# num=int(input("enter the number"))
# number=num%10
# if(number/3==1)or (number/3==2) or (number/3==3):
#     print("yes")
# else:
#     print("no")

# num=input("enter your number: ")
# b=len(num)-2
# c=int(num)//10**b
# d=c%10
# if d==4:
#     print("yes")
# else:
#     print("no")


# num=input("enter your number: ")
# b=len(num)
# c=int(num)//10**b
# d=c%10
# if d==3:
#     print("yes")
# else:
#     print("no")

# num=str(input("enter the number and alphabet: "))
# if num<="10" and num>="0":
#     print("numbers")
# elif num >="a" and num<="z" or num >="A" and num<="Z":
#     print("alphabet")
# else:
#     print("nothing")


# birth_year=int(input("enter the birth year: "))
# current_year=int(input("enter the current year: "))
# if current_year-birth_year:
#     print(current_year-birth_year,"age")
# else:
#     print("nothing")

    
# day=int(input("enter the day number:"))
# if day==1:
#     print("sunday")
# elif day==2:
#     print("monday")
# elif day==3:
#     print("tuesday")
# elif day==4:
#     print("wensday")
# elif day==5:
#     print("thrsday")
# elif day==6:
#     print("friday")
# elif day==7:
#     print("saturday")
# else:
    # print("not")




# # prime number:

# a=int(input("enter the number: "))

# if a%2!=0 and a%3!=0 and a%5!=0 and a%7!=-0:
#     print("prime number")
# elif a==2 or a==3 or a==5 or a==7:
#     print("prime")
# else:
#     print("not prime")



# # negative number:

# n=int(input("enter the number:"))

# if n==n:
#     print(-n)
# else:
#     print(n)


