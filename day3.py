#Numeric datatype --> int,float,complex along with boolen

#Input formatting -->Accepting input from the user --> input()

#Accepting integer input from user
#by defalt input() accepts any input -->
#int(input()) -->will accept any input -->str
'''age = int(input('enter the age:')
print(age)
print(type(age))

#float(input()) -->accepts integers,float values
age=float(input('enter the age:'))
print(age)
print(type(age))





print(type(name))

#accept group of values

marks = int(input("Enter the marks:")).split(
print(marks)'''
'''
a = input().split() #by default split() has space
print(a)

#comma separated values
a = input().selit() #now you enter spaces in input
print(a)
#comma seperate value
a = input("Enter the value:").split(',')
print(a)

#List of integers
marks = list(map(int,input("Enter the value").split(',')))
print(marks)

#now we want to accept 2 values from user
age,salary = map(int,input("Enter the value").split(','))
print(age)
print(salary)

#Single input --> int(input())
#two inputs -->a,b = map(int,input().split(','))
#any number result as list -->ArithmeticError a = list(map(int,input(),split(',')))

marks = list(map(float,input("Enter the value").split(',')))
print(marks)

age,salary = map(float,input("Enter the value").split(','))
print(age)
print(salary)
'''


#Acceping input frpom uder --> int,float -> input formating

#Operators --> Operators perfect operstors between values (operands)
#7 types -->Arithemetic,Assignment,Comparasision (Relationship)
#Membership,Identity,Logical,Bitwise

#Arithemetic Operator -->Artithemetic Operations
#+ , -,*,/
print(5+3)
print(5-3)
print(5*3)
print(5/3)
print(5//3)#floor division -->return quotient
print(5%3)#modulus -->divisiable rules ->return reminder
print(4**2)#power (exponenential)'''

1=int(input(input("Enter the Length"))
b=int(input(input("Enter the Breadth:"))
area=1*b
print("The area of Recatngle is:"
'''
      

      
















#Comparission Operators -->we compare the value -->boolen
#==(equal to),!=(not equal to) , != (not equal to)
# <= (equal to) , !










print(-5 < -1)

#Membership Operators --> in,not in -->boolen
#it checks for the existance of an object in a collection

marks = [56,75,45,85]
print(35 in marks)      
#print(35 in 355) #TypeError

print(25 not in marks)
print('code' in 'codegnan')
print('$' in 'abc$frg')


#Logical Operators -->logical decision making -->and ,or,not
#and -->all aonditions to be satisified
'''
a = (25 in [25,45,65] and 45 < 56
print(b)
c = not (true)
print(c)

#Identity operators -->check for 
      













