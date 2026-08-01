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



 : Student maks and grade analayzer
90 - 100 --> 'A'
80 - 89 --> 'B'
70- 79 --> 'c'
60 - 69 --> 'd'
<60 --> Fail
#also -ve cases should not be allowed and marks shouldnt be greater 100

mark = int(input("Entet the marks (1-100):"))
if marks > 0 and marks <=100:
    if marks >=90:
              prinmt("User has secured Grade A")
    if marks >=80 and mark <= 89:
        print("User has secured Grade B")
    if marks >=70 and marks <=79:
        print("User has secured Grade D")
    if marks >= 60 and marks <= 69:
        print("user has secure Grade D")
    if marks < 60:
        print("User has falsed,study again")
else:
     print("Enter only +ve value greater than 0 less thsn 100")
'''
#elif keyword -->if-else-if

'''
if<condition1>:
   statement (s)......
elif<coundition2>:
   statement
    


marks = int(input("Enter the student marks:"))
if marks >=!00:
  print("Entered value should be greater than 1 and less than 100")
e  
      















#Voter Eligibility checkcase -->marke sure to satisfy all possiblie conditions
#>=18 and of years eligibility should tell
#negative value --> not acceptable

age = int(input("Enter the age:"))
if age>=18 and age <=100:
    print('------ User has Vote Eligibility -----')
    print("------ Access Granted -------')
elif age<18 and >0:
    print('------ User atill need to get Vote Eligibility -----')
    print('------User need to wait for more',(18-age),'yer(s)------')
else:
    print('-----Only +v e value and less than 100 Acceptable-----')

#prwfer if -elif-else....
'''
#output -->print() -->we can pass any value also use sepnand
#Output formatting -->old style formatting (using commas)
#% usage (%f,%d), .format() usage,fstring notation
a,b = 7,9
print(a)
print(b)
print(a,b)
name = "Codegnan";batch = "DataAnalysis"
print(name,batch) #by default sep is having space
print(name,batch,sep=',')
print(name,batch,end='\t')
print(a,b,end='')
print("Hyderabad")'''

name='Codegnan';age
          







                









              
           







                  













