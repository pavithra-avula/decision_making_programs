
#string is palindrome or not
n=input("Enter a string:")
if n[::1]==n[::-1]:
    print("palindrome")
else:
    print("not palindrome")

#number is palindrome or not
s=input("Enter a number:")
if s[::1]==s[::-1]:
    print("palindrome")
else:
    print("not palindrome")

#year is leap year or not
m=int(input("Enter a year:"))
if m%4==0:
    print("leap year")
else:
    print("not leap year")

#number is perfect square or not
i=int(input("Enter:"))
s=i**0.5
if s*s==i:
    print(i,'is a perfect square')
else:
    print(i,'is not a perfect square')

#char is alphabet or number or special character
n=input("Enter a char:")
if n.isalpha():
    print("alphabet")
elif n.isnumeric():
    print("number")
elif not n.isalnum():
    print("special character")

n=input("Enter:")
if len(n)==1 and  n.isalpha():
    print("alphabet")
elif len(n)==1 and n.isnumeric():
    print("number")
elif len(n)==1 and n.isalnum():
    print("special character")
else:
    print("enter one character")

#pass mark is greater than 35
m=int(input("Enter a number:"))
if 35<=m<60:
    print("pass")
elif m<35:
    print("fail")
elif m>35:
    print("first class")

#startting char is vowel
s=input("Enter a string:")
start_char=s[0]
if start_char in 'aeiouAEIOU':
    print("vowel")
else:
    print("not vowel")

#list has even length
elements=input("enter the elements:").split()
if len(elements)%2==0:
    print("even length")
else:
    print("odd length")

#no.of keys in dict is even 
d={}
d.update({4:5,'a':4,5:'b'})
if len(d)%2==0:
    print(d)
else:
    d['b']='apple'
    print(d)

d={}
d.update({4:5,'a':4,5:'b'})
if len(d)%2==0:
    print(d)
else:
    key=input("enter a key:")
    value=input("enter a value:")
    d[key]=value
    print(d)

#to get largest number from 3 numbers
n1=int(input("Enter:"))
n2=int(input("Enter:"))
n3=int(input("Enter:"))
if n1>=n2 and n1>=n3:
    print(n1,'is greatest')
elif n2>=n1 and n2>=n3:
    print(n2,'is greatest')
else:
    print(n3,'is greatest')

import random
print(random.randint(1,10))

#returns index
import random
l=[4,4.5,12,67]
print(random.randint(0,len(l)-1))

#returns elements
import random
l=[4,4.5,12,67]
index=random.randint(0,len(l)-1)
print(l[index])

#choice
import random
places=['goa','varakala','karnataka','ap']
print("let's visit",random.choice(places),":)")

#program to get tail or head
import random
num=random.randint(0,1)
if num==0:
    print('head')
else:
    print('tail')

#program to guess a number
import random
name=input("what is your name:")
print("hey",name,"let's start the game")
computer_guess=random.choice((1,2,3,4,5,6,7,8,9,10))
user_guess=int(input("guess a number:1 to 10"))
print(computer_guess)
if user_guess==computer_guess:
    print("you win")
elif user_guess<computer_guess:
    print("guess larger number")
elif user_guess>computer_guess:
    print("guess lower number")
else:
    print("guess only numbers in the tuple")

#rock,paper,scissor
import random
computer_items=random.choice(['scissor','rock','paper'])
user_input=input("scissor or rock or paper:")
if computer_items==user_input:
    print('draw')
elif computer_items=='scissor':
    if user_input=='rock':
        print('you won rock hits scissor')
    else:
        print('you lost scissor cuts the paper')
elif computer_items=='rock':
    if user_input=='paper':
        print('you won paper wrap the rock')
    else:
        print('you lost rock hits the scisssor')
else:
    if user_input=='scissor':
        print('you won scissor cuts the paper')
    else:
        print('you lose paper wrap the rock')
