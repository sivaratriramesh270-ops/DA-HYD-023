'''
Identify












a = [1,3,5,6]
b = a
print(id(a))
print(id(b))
c = [1,3,5,6]
print(id(c))
#As we have Lists (Mutable collection both c and a list will have different
#ids whereas values are same
print(c is a) #output false
print(c == a) #output True
print(c is a)
#Bitwise Operators --> we perform bitwise operators over operands
#& (and) , | (or),shifting operators (<<,>>)
#Number will be converted to binary format

print(5&3) #both 5 and 3 to be converted binary and bitween and is performed

print(5|3) #bitwise OR

print(5^3) #Bitwise XOR

print(5 and 3) #here and is logical operator checks for both existances
#returns 5 in above case

print(5 or 3) #return 3 in this case

#Leftshift Operator << ,right shift Operator >>

print(5 < 1) #False Comparision
print(5<< 1)
print(5 >>1) #Right shift operation by 1 positio

print(15 << 2) #convert 15 to binary and perform 2 times left shifti

print(15 >> 2)#same 2 times right shifting

#Input Formatting --> input(),int(input()0,float(input())
#You know -->single input
#2 or 3 input --> map()
#group of integers --> listr(map(int,input().split(',')

name = input("Enter the name:").split(',')
print(name)

name1,name2 = map(str,input("Enter the Friends Names:").split(',')                  
print(name1,name2)
                  
#Tokns --> Numeric Datatypees --> Operators -->flow of the program
#Conditional State




#age = 15
age = int(input("Enter the age:"))
if age >=18 and age in [19,21,20]:
    print('Your Age is',age)
print(age)

#else keyword --> if -else

If <condition>:
    statement(s)...
    ....
'''

#Vote Eligiblity -->To check his/her voter eligiblity and give access...
if age >0:
  if age = int(input("Enter the age:"))
  if age>=18:
      print("You have Voter eligibility and age is",age)
      print("Access Grand")
else:    
    age = 18-age
    print("You need to wait for more",age,'years')
else:
    print("you have entered -ve values/zero enter only +ve")


'''
task : Student maks and grade analayzer
90 - 100 --> 'A'
80 - 89 --> 'B'
70- 79








                  













