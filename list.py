# # question-1

# # Aap apne friends ki ek list banaye

# namelist=["Neha","Devyani","Suchitra","Gayatri"]
# print(namelist)
# print(type(namelist))

# # question-2

# # Write a program that tells how many elements are there in a given list. It is similar to len() function, so in order to implement this program we will not use len() function but we will try to understand that how did any programmer implemented this len() function.

# numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
# count=0
# for i in (numbers):
#      count+=1
# print(count)
    

# # question-3

# # Write a code, that counts the numbers between 20 and 40 and then print its count.

# numbers=[50, 40, 23, 70, 56, 12, 5,10, 7]
# i=0
# while i<len(numbers):
#     if numbers[i]>20 and numbers[i]<=40:
#         print(numbers[i],"its count")
#     i+=1

# numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
# i=0
# a=[]
# count=0
# while i<len(numbers):
#     if numbers[i]>=20 and numbers[i]<=40:
#         a.append(numbers[i])
#         count+=1
#     i+=1
# print(count)
# print(a)        



# # question-6

# Write a code that the reverses the order of the items means in opposite order.

# places=["delhi", "gujrat", "rajasthan", "punjab", "kerala"]

# i=0
# while i<len(places):
#     print(places[-i-1])
#     i+=1

# question-7

# Iterate over both the values in a list and their indices

# grocery_list = ['flour','cheese','carrots']

# i=0
# while i<len(grocery_list):
#     print(i,grocery_list[i])
#     i+=1

# question-8

# Convert Character Matrix to single String;
# 	The original list is: [ ['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't'] ]
# The String after join: gfgisbest


# a=[ ['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't'] ]
# print("The original list is : " + str(a))
# res = ''.join(ele for sub in a for ele in sub)
# print("The String after join : " + res)


# question-9

# list=[1,2,3,4]
# i=0
# sum=0
# while i<len(list):
#     sum=sum+list[i]
#     i+=1
# print(sum)    

# question-10

# list=[1,2,3,4,5,6,7,8,9,10]
# list_even=[]
# list_odd=[]
# # while i<len(list):
# for i in range (len(list)):
#     if list[i] % 2==0:
#         list_even.append(list[i])
#     else:
#         list_odd.append(list[i])
# print(list_even)
# print(list_odd)



# name="neha"
# age=12
# print(name+age)


# name=""
# age="12"
# print(name+age)

# Convert Character Matrix to single String;
# 	The original list is: [ ['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't'] ]
# The String after join: gfgisbest


# list=[ ['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't'] ]
# name=[""]
# i=0
# while i<len(list):
#     j=0
#     while j<len(list[i]):
#         print(list[i][j],end="")
#         j+=1
#     i+=1
        
# question-11

# Write a code that checks whether a list is a palindrome or not.
# And print “Haan! palindrome hai” if its a pallindrome and “nahi! palindrome nahi hai” if its not a palindrome.

# For the time being you can use the list given below for writing the code.


# name=input("enter the name: ")
# # name=["natan"]
# i=0
# length=len(name)
# a=[]
# while i<(length):
#     length=length-1
#     a.append(name[i])
# print(name)
# if a==name:
#     print(" it is a pallindrome name")
# else:
#     print("it is a not pallidrome name")    
    


# a="Neha"
# a+="\nshubham"
# print(a)

# # list iteration
# list=['a','b','c',1,2,3]
# for x in list:
#     print(x)


# # list concantration

# list1=['a','b','c']
# list2=['x','y','z']
# list3=list1+list2
# print(list3)

# # list append

# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)

# # list slicing method
# list=['foo','bar','baz','quz','quux','corge']
# print(list[2])
# print(list[3:5])
# print(list[-4:-1])
# print(list[1:5:2])
# print(list[-1: :-1]) #reverse list



# a=["ram",10,"shyam",121.5]
# print(a)
# a[1]=20
# print(a)
# a[2]="amit"
# print(a)
# a=["ram",10,"shyam",121.5]
# del(a[2])
# print(a)
# a=["ram",10,121.5]
# del(a[0])
# print(a)

# # changable list
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)

# # insert list
# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "watermelon")
# print(thislist) 

# list slicing

# list=['foo','bar','baz','quz','quux','corge']
# print(list[4:6])
# print(list[-4:-1])
# print(list[1:5:2])
# print(list[-1: :-1]) #reverse list


# # list count

# list=[1,2,3,'a','b','c',1,2,3]
# print(list.count(1))
# print(list.count('b'))
# print(list.count(4))
# print(len(list))
 

# numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
# i=0
# while i<=len(numbers):
#     if numbers[i]>=20 and numbers[i]<=40:
#         print(numbers[i],"count")
#     i+=1    


# # extend list 

# a=[1,2,3]
# a.extend([4])
# a.extend('apukuubso')
# a.extend(['a','b','c'])
# print(a)


# # create a list
# prime_numbers = [2, 3, 5]

# # create another list
# numbers = [1, 4]

# # add all elements of prime_numbers to numbers
# numbers.extend(prime_numbers)


# print('List after extend():', numbers)

# Output: List after extend(): [1, 4, 2, 3, 5] 

# list=[50,10,70,60]
# i=0
# while i<len(list):
#     print(i)
#     i+=1


# list=[50,10,70,60]
# i=0
# sum=0
# while i<len(list):
#     sum=sum+list[i]
#     i+=1
# print(sum)


# list=[50,10,70,60]
# print(list[-1::-1])


# a=[2,3,4,4,5,6,7,7,8,9,9,12]
# b=[]
# for i in range(len(a)):
#     k=a[i]
#     if k not in b:
#         b.append(i)
# print(b)

# a=[2,3,4,4,5,6,7,7,8,9,9,12]
# dup_items=set()
# uniq_items=[]
# for x in a:
#     if x not in dup_items:
#         uniq_items.append(x)
#         dup_items.add(x)

# print(dup_items)


# a=[1,2,3,4,5,6,7]
# b=[9,8,7,6,5,3,4]
# i=0
# while i<=len(a): 
#     print(len(a))
#     # sum=a[i]+b[i]
#     # b.append(sum)
#     i+=1
# # print(b)



# magic_square = [[8, 3, 4],[1, 5, 9],[6, 7,[5],2]]

# # print (magic_square)
# print (magic_square[2,0])
# # print type(magic_square[1])

# # print sum(magic_square[0])
# # print sum(magic_square[1])
# # print sum(magic_square[2])

# # QUESTION:
# List product excluding duplicates.
# 	List = [6,1,3,5,6,3,1]
# 	Output: 60

# QUESTION:

# b=[[1,2,0],[3,2,5],[5,2,9]]
# max=0
# for i in range(len(b)):
#     if b[i] >max:
#         max=b[i]
   
# print(max)

# QUESTION:

# d=['red','yellow','pink']
# i=0
# a=[]
# while i<len(d):
#     b=(list(d[i]))
#     a.append(b)
#     i+=1
# print(a) 

# QUESTION:

# c=["laduu",23,24,"yes",53.4]
# i=0
# a=[]
# while i<len(c):
#     if type(c[i])==int or type(c[i])==float:
#         a.append(c[i])
#     i+=1
# print(a)


# a=["NEHA"]
# i=0
# while i<len(a[0]):
#     n=a[0]
#     j=0
#     while j<1:
#         print(n[i])
#         j=j+1
#     i=i+1
  

# a=['NEHA']
# i=0
# b=[]
# while i<len(a):
#     c=(list(a[i]))
#     b.append(c)
#     i+=1
# print(b)  


# a=[[1,2,0],[3,2,5],[5,2,9]]
# sum=0
# for i in range(len(a)):
#     n=a[i]
#     if type (n)==list:
#         for j in range (len(n)):
#             m=n[j]
#             if type(m)==list:
#                 for k in range(len(m)):
#                     o=m[k]
#                     sum=sum+0
#             else:
#                 sum=sum+m
#     else:
#         sum=sum+0
# print(sum)


# a=[[1,2,0],[3,2,5],[5,2,9]]
# sum=0
# for i in range(len(a)):
#     n=a[i]
#     if type (n)==list:
#         for j in range (len(n)):
#             m=n[j]
#             if type(m)==list:
#                 for k in range(len(m)):
#                     o=m[k]
#                     sum=sum+0
#             else:
#                 sum=sum+m
#     else:
#         sum=sum+0
# print(sum)



# # QUESTION (magic square):

# # magic_square = [[8, 3, 4],[1, 5, 9],[6, 7, 2]]
# magic=[
#     [8,3,4],
#     [1,5,9],
#     [6,7,2]
# ]
# i=0
# sum=0
# sum1=0
# sum2=0
# while i<len(magic):                       
#     colum=0
#     while colum<len(magic[i]):
#         if sum!=15:
#             sum=sum+magic[i][colum]
#         elif sum1!=15:
#             sum1=sum1+magic[i][colum]
#         else:
#             sum2=sum+magic[i][colum]
#         colum+=1
#     i=i+1
# print(sum,sum1,sum2)
# if sum==sum1==sum2:
#     print("its a magic square")
# else:
#     ("it's not magic square")


# # # QUESTION:

# a=[1,2,3,4,5,6,7,8,9,10,11,12]
# b=[]
# for i in range (len(a)):
#     if a[i]%2==0:
#         b.append(0)
#     else:
#         b.append(a[i])
# print(b)


# # QUESTION:

# a=[1,2,3,[1,2,3,4],28,[1,2]]
# sum=0
# sum=0
# for i in range(len(a)):
#     n=a[i]
#     if type (n)==list:
#         for j in range (len(n)):
#             m=n[j]
#             if type(m)==list:
#                 for k in range(len(m)):
#                     o=m[k]
#                     sum=sum+0
#             else:
#                 sum=sum+m
#     else: qwer    
#         sum=sum+0
# print(sum)

# # QUESTION:

# a=["NEHA","DEVYANI","DURGESH","NISHANT","DIMPAL","SANKET","KAMINI"]
# var=input("enter the number:")
# i=0
# while i<(len(a)):
#     i+=1
# print(len(var))



# # QUESTION:

# a=[1,2,3,4,5,6,7,8,9,10,11,12]
# list_even=[]
# list_odd=[]
# for i in range (len(a)):
#     if a[i] % 2==0:
#         list_even.append(a[i])
#     else:
#         list_odd.append(a[i])
# print(list_even)
# print(list_odd)


# a=['NEHA']
# i=0
# b=[]
# while i<(len(a)):
#     print(a.upper()[i]+a.lower()[i]*(i),end=" ")
#     if i!=len(a)+1:
#         b.append(a[i])
#     i+=1    
# # print("_",end=" ")    
# print(b)    

# a=input("enter the name: ")
# i=0
# while i<(len(a)):
#     print(a.upper()[i]+a.lower()[i]*(i),end=" ")
#     if i!=len(a)+1:
#         print("_",end=" ")
#     i+=1
        

# name=["m","o","m"]

# # name=input("enter the name: ")
# # # # name=["natan"]
# i=0
# length=len(name)
# a=[]
# while i<length:
#     if a==name:
#         length=length-1
#         a.append(name[i])
#     i+=1

# count=0
# j=0
# while j<len(name):
#     if name[j]==a:
#         count+=1
#     j+=1
# print(count)

# if a==name:
#     print(" it is a pallindrome number")
# else:
#     print("it is a not pallidrome number")
# i+=1  


# a='MONIKA'
# print(a[::-1])





   

# a=['neha']
# b=[]
# for i in range (len(a)):
#         b.append(a[i][::-1])
# print(b)
# # print(a[0][::-1])





# question=[
#     "Which is the capital of India?"
#     "Which is the longest dam in India?"
#     "Which is the national tree of India?"
#     "Which is the national bird of India?"
#     "What is another name for Sahyadris?"
# ]

# options=[
#     ["delhi","mumbai","pune","rajasthan"]


# ]





 
# list=[12,13,15,18]
# i=0
# sum=0
# while i<len(list):
#     j=0
#     sum=0
#     while j<(list[i]):
#         sum=sum+list[i]
#         j+=1
#     i+=1
# print(sum)


# list=[12,13,15,18]
# i=0
# sum=0
# a=[]
# while i<len(list):
#     b=str(list[i])
#     # a.append(b)
#     j=0
#     while j<(list[i]):
#        sum=sum+list[j]
#        a.append(sum)
#     j+=1
#     i+=1
# print(a)        





# a=[12,"Gayatri",12.32,"Devyani",12+0j,12]
# c=[]
# b=a[1],a[3]
# c.append(b)
# print(c)




# a=[12,"Gayatri",12.32,"Devyani",12+0j,12]
# i=0
# c=[]
# while i< len(a):
#     if type(a[i])==str:
#         c.append(a[i])
#     i+=1
# print(c)  


# a='NEHA'
# print(len(a))



# a=[12,"Gayatri",12.32,"Devyani",12+0j,12]
# count=0
# for i in (a):
#     count+=1
# print(count)
    
# b=[]
# a=int(input("enter the number: "))
# for i in range (0,a):
#     n=int(input("enter the munber:"))
#     b.append(n)
# print(b)    





# a=input("enter the input:")
# b=[]
# for i in range (0,a):
#     b.append(a)
# print(b) 

# b=[]
# a=input("enter the input:")
# for i in range (0,a):
#     b.append(a)
# print(b)






# a=['NehaRandhavan']
# print(a)





 
# a=['dad','mom','sis','tanu','neha']
# i=0
# count=0
# length=len(a)
# b=[]
# while i<(length):
#     length=length-1
#     b.append(a[i])
#     if b==a:
#         print(b)
#     i+=1
#     count+=1
# print(count,"=",b)        
 


# a=[1,-2,-3,-4,5,-6,7]
# b=[]
# for i in range (len(a)):
#     if a[i]<0:
#         b.append(0)
#     else:
#         b.append(a[i])
# print(b)


# a=input("enter the number:")
# b=[]
# a=a.title()
# b.append(a)
# print(b)        




# a=[[1,2],[3,4],[5,6],[7,8,9]]

# i=0
# b=[]
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         b.append(a[i][j])
#         j+=1
#     i+=1
# print(b)        




# a=[1,2,3,4,5,6,7,8,9]
# i=1
# count=0
# while i<len(a):
#     if i%2!=0:
#         # print(i,a[i])
#            count+=1
#     i+=1
# print(i)        

# a=[1,2,3,14,5,6,7,8,9]
# i=0
# while i<len(a):
#     if i%2!=0:
#         print(i,a[i])
#     i=i+1        


