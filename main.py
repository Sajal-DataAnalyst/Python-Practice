#print("hello youtube lets start learning python")

#a=25
#print(type(a))

#a='Aditya 123'
#print(a[7],a[-1])

#a='Sajal Jaiswal'
#print(a[6::1])

#a= ""
#print(bool(a))

# age=int(input('What is your age?'))
# print(age)

# print(True and bool(0))

# a = 13

# if a>6:
#     print("I will do the task A")

# else:
#     print("I will do task B")    

# money = int(input("Please provide me the money "))

# if money==10:
#     print("I will have a choco bar ice cream")
# elif money==20:
#     print(" I will have a mango dolly")    

# else:
#     print("I will have a CONE")    

# number1 = int(input(" Enter the first number "))
# number2 = int(input("Enter the second number "))

# if number1>number2:
#     print(f"{number1} is greater than {number2}")
# elif number2>number1:
#     print(f"{number2} is greater than {number1}") 
# else:
#     print("Both numbers are same")    
     
# gen=input("Enter your Gender as Character (M) or (F) :- ")

# if gen=="M" or gen=='m':
#     print("Good morning Sir")
# elif gen=="F" or gen=='f':
#     print("Good morning Mam")
# else:
#     print("Wrong gender Please write in proper format M or F")         

# num=int(input('Enter the number :- '))

# if num%2==0:
#     print("Even Number")
# elif num%2!=0:
#     print('ODD Number')    
# else:
#     print(' Wrong Number entered')    

# name=input(' Enter your Name :- ')
# age=int(input(' Enter your age :- '))

# if age>=18:
#     print(f'Hello {name} you are a Valid Voter ')
# elif age<18:
#     print(f'Hello {name} you are not ELIGIBLE to Vote')

# year = int(input(' Tell your year :- '))

# if year%100==0 and year%400==0:
#     print('Its a leap year')

# elif year%4 ==0:
#     print('Its a leap year')
# elif print('Its a normal year')        

# t = int(input('Please tell your temperature :- '))

# if t<0:
#     print('Freezing cold ')
# elif t>=0 and t<10:
#     print('very cold')    
# elif t>=10 and t<20:
#     print('cold') 
# elif t>=20 and t<30:
#     print('pleasant') 
# elif t>=30 and t<40:
#     print('hot')
# else:
#     print('very hot')         

# a = range(1,20,1)

# for i in a:
#     print(i)

# for i in range(-3,-16,-1):
#     print(i)

# table of any number

# n=int(input('TEll me table number you want to print'))
# for i in range(n,n*10+1,n):
#     print(i)

# print string using for loop

# a='SAJAL IS HANDSOME'

# for i in range(len(a)):
#     print(a[i])

# b='SAJAL IS HOT' 

# for i in b:
#     print(i)

# for i in range(1,21):
#     if i==6:
#         continue
#     print(i)

# n = int(input('Enterthe reverse number '))

# for i in range(n,0,-1):
#     print(i)

# n = int(input('Enter the table  number '))

# for i in range(1,11):
#     print(f'{n} * {i} = {n*i}')


# n = int(input('Tell your NUMBER '))
# sum=0

# for i in range(1,n+1):
#     sum=sum+i

# print(f' Your sum is {sum}')

# n = int(input('Tell your NUMBER '))
# fact=1

# for i in range(1,n+1):
#     fact=fact*i

# print(f' FACTORIAL OF YOUR NUM is {fact}')

# n = int(input("Tell your number  "))
# even=0
# odd=0
# for i in range(1,n+1):
#     if i%2 ==0:
#         even=even+i
#     else:
#         odd=odd+i    
# print(f'Your even and odd sum are {even}, {odd}')

# n= int(input("Please tell your number for factorial   "))

# for i in range(1,n+1):
#     if n%i==0:
#         print(i)

# n= int(input(" ENTER PERFECT NUMBER TILL WHICH YOU WANT   "))
# sum=0
# for i in range(1,n):
#     if n%i == 0:
#         sum=sum+i

# if sum == n:
#     print("Your number is perfect")
# else:
#     print('not a perfect number')        

# n= int(input(" ENTER number to check prime   "))
# count=0
# for i in range(1,n+1):
#     if n%i ==0:
#         count=count+1

# if count == 2:
#     print(' its a prime number')
# else:
#     print(' not a prime no')    


# a = "SAJAL"
# print(a[::-1])

# a = "NAMAN"
# b = ""
# for i in range(len(a)-1,-1,-1):
#     b= b+(a[i])

# if b==a:
#     print('its a palindrome')    
# else:
#     print('not a palindrome')

# a="sms1224@##$$$%%%%%%()*&(*^&%^sdagd0)"
# char=0
# dig=0
# spchr=0
# for i in a:
#     if i.isdigit():
#         dig+=1
#     elif i.isalpha():
#         char+=1
#     else:
#         spchr+=1
#         print(f' your digits are {dig} \n your albhabets are {char}\n your special characters are {spchr}')

# while loop

# a=1

# while a<=30:
#     print(a)
#     a=a+1

# a=int(input('Tell your number to print each digit of number '))

# while a>0:
#     print(a%10)
#     a=a//10


# a=int(input('Tell your number to reverse '))
# rev=0

# while a>0:
#     rev=rev*10+a%10
#     a=a//10

# print(rev)


# a=int(input('Check if its pallindromic number   '))
# rev=0
# copy=a

# while a>0:
#     rev=rev*10+a%10
#     a=a//10
# if copy==rev:
#     print("its a pallindromc number")
# else:
#     print('not a pallindrome')

# RANDOM NUMBER GUESSING GAME 

import random
num = random.randint(1,10)
tries=0

while True:
    guess=int(input(" Please Guess Your Number Between 1 to 10 "))

    if num==guess:
        tries+=1
        print(f" You are Right You guessed the number in {tries} tries")
        break

    elif num<guess:
        print(' Go a little lower ')
        tries+=1

    elif num>guess:
        print(' Go little Higher ')
        tries+=1

    else:
        tries+=1
        print(" Sorry, You are Wrong")





     

