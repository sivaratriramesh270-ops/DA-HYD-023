'''
Lists,Tuple..
'''
#List --> Multle,Ordered,Heterogenous

#index(),cout(),copy(),sort(),reverse()
'''
details =['codegnan',7,2018,'Hyderabad']
print(len(details))
print(details.index(7))
print(details.index('codegnan'))
details.extend([7,21,45,21])
print(details.index(21)) #it returns first occurance
print(details.index(21,6))
#print(details.index('python') #ValueError

print(details.count(21))
print(details.count('python')) #it returns 0 as we dont have it

data = ['codegnan','saketh','python','java'] #input
#output should be as follows

0 : codegnan
1 : saketh
2 : python
3 : java

for obj in data:
    print(data.index(obj),':',obj)

for obj in range(len(data)):
    print(obj,':',data[obj])

#copy() -->shallow copy of the given collection

new = data.copy()
print(new)
print(type(new))
print(len(data))

new[2] = 'Agentic AI'
print(new)
print(data)

data.append('saketh')
print(data)
print(new)

data = [1,4,5,[21,34,45],23]
print(data)
new = data.copy()
print(new)

new[3][2] = 'Agents' #whenever we make changes in nested list original will
#also be effected
print(new)
print(data)

new[1] = 'python'
print(new)
print(data)


marks = [14,24,-45,27,35]
print(marks)
#print(marks.sort()) #returns None
#print(marks) #returns iin accending order
marks.sort(reverse = True) #return in Descending order...
print(marks)
marks.insert(2,'code')
#marks.sort()
#reverse() --> return in reverse order
marks.reverse()
print(marks)
print(marks[::-1])

#type(),len(),max(),min(),print()

print(sorted('codegnan'))#returns List in ascending order
#print(sorted(['code','23',34,45]) #raise Error


#Tuples --> Tuples are Indexed,Ordered,Hetrogenous,Immutable collection
#dimensions,coordinates,database records,we prefer () for tuple notation

a = ()
print(type(a))
print(len(a))

dimensions = 1,5,2.5
print(dimensions)
print(type(dimensions))
print(len(dimensions))
        
#Operations -->Indexing,Slicing,Striding,Membership,Merging,Repetition

courses = ('PFS','JFS',('DA','DS','agenticAI',[100,6,6]))
print(courses)
print(len(courses))

print(courses[-2][-2:])
#coursres[2] = Tuple are Immutable
courses[-1].append('codegnan') #we can make any modifications inside list
print('PFS' in courses)
d = courses * 2 #repetition
print(d)
e = courses + (2,3,4,5) #merging
print(e)


#Tuples Immutable -->count(),index()
print(courses.index('AgenticAI')) #returns first occuracy
print(courses.count('Agents'))

#print(courses.sort() #AttributeError -->sort() is in Lists not in Tuples

print(sorted(courses[-1])
#print(sorted(courses)) #as we have mixed type

#TypeCasting
d = tuple(sorted((23,12,3,4,5)))
print(a,b)

a = tuple(map(int,input("Enter the values").split(',')))
print('9+4'))
#evel() function can take any kind of input
print(eval('9+4'))

a = eval(input("Enter a list")) #in this case u exactly enter data as len
print(a)
print(type(a))'''

#Task:Take a user input as strings,do this in two ways..
'''
1) give the count of each repeating character
Test case 1: programming

r is repeating 2times
g is repeating 2times
m is repeating 2times

