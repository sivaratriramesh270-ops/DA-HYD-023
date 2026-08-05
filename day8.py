#Strings --> Group of characters,we use single or double or triple quotes
#for representation of string...
#Strings are Immutable,Ordered,Indexed Collection
#space is also a character
name = 'codegnan'
'''print(name)
print(type(name))
print(let(name)) #len -->returns the number of items in container

#index() --> fetch the object (position) starts at 0 and ends at len(obj) - 3
#we use [] representation
print(name[0])
print(name[5])
#print(name[25]) #IndexError --> as its out of range

#Negetive Indexing --> -1 to len(obj)
print(name[-1]) #it returns last charater
print(name[-3])
print(name[-33]) #indexerror

#Sliceing -->We can access grpup of characters(objects)
#we use [start:end] default --> is included,end is excluded

print(name[:]) #return entire string
print(name[0:]) #returns entire string
print(name[:2]) #starts at 0th index before 4th index
print(name[1:3])

name='python'
print(name[3:7])
print(name[7:3]) #returns enpty as strings are immutable
#Slicing is applicable from lower inex to higher index
print(name[:44]) #return till end of the string
print(name[45:])

print(name[-1:-5]) #return empty string
print(name[-5:-1]) #starts at -5 and ends at -2
#prit 'on' from above string
print(name[4:])
print(name[4:6])
print(name[-2:])

print(name[1:-2])
print(name[2:-6])
#observe +v,+v ,-v-ve & +ve,-v all possibilities


#Striding --> [start:end:step]

course = 'DataAnalysis'
print(let(course))
#Data -->result
print(course[:4])
print(course[4:])
print(course[-3:])

print(course[::1]) #returns all characters
print(course[::2]) #includes start to end skipping character

print(course[1:6:3]) #[1:6] -->ataAn -->[1:6:3] -->aA

#tnys
print(course[2::3])

print(course[::-1]) #it returns the reverse of astring

print(course[::-2])

#task: Workout with all possibilities of slicing an striding on a example

name = 'codegnan'
#name[3] = 'w' #String -->Inddexing,Concatenation,Repetion
print(name * 3)
print('*' * 25) #repetition

#Concatenation --> combining string

data = 'ramesh' + 'python' + 'database'
print(data)
print('123' * 4) #Numeric String
print('code' in 'codegnan')

for i in 'codegnan':
    print(i,':')
#in above case we grt every character line by line

for i in 'codegnan':
    print(i,end=' ')

names = "Codegnan"
#Built-in function --> len(),min(),sorted()
print(len(name))
print(min(name)) #alphabetical order ASCII orderning
print(ord('A'))
'''

#Methods on String --> Cas-conversions,Finding/Searching...
name = 'Codegnan data'
#Case-conversions -->upper(),lower(),title(),capitalize()
a = name.upper()
print(a)
b = name. lower()
print(b)
#Capitalize() --> converts first letter to upprercase
c = name.capitalize()
print(c)
d = name.title() #converts every word first letter to uppercase
print(d)

#Task : A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
#loops and strings to return to A-Z



















      
