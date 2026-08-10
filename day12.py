'''
Strings --> CaseConversions,Searching & finding,String testing method.
Replace,Space removal


#Searching,Finding,Replacing,Joining...
a = "Codegnan"
print(len(a))
print(min(a))
print(max(a))

b = a.index('g') #it returns the index position
print(b)
c = a.index('n') #it returns only the first occurance
print(c)
d = a.index('n',6)#it retiurns the next occurance
print(d)
#e = a,index('n',8) #ValueError
#print(e)
#f = a.index('t') #ValueError
#print(f)
g = a.index('n',1,4)
print(g)

#rindex() --> returns last occurance
b = a.rindex('g')
print(b)
c = a.rindex('n') #here 'n' is occuring at 7th index
print(c)
#d = a.rindex('n',8) #it returns ValueError
#print(d)

#count() -->returns the number of items object is repeating

print('Codegnan'.cpount('n'))
print('Code'.count('w')) #it returns 0 as we dont 'w' in 'code'
print('Cakshjasaksajs'.count('r'))

#find() -->foirst occurance but it avoid error returns -1 if substracting is
#not found
print('codegnan'.find('r')) #it returns -1

print('codegnan'.find('n'))

a = "Data"
print(len(a))
for i in a:
    #print(i)
    print(a.count(i),a.index(i))


#Replacing,Splitting,Joining

#Strings are Immutable
a = 'Cpdegnan'
#a[4] = 's'
print(a.replace('g','s'))
print(a)
a = a.replace('g','s')
print(a)
print('fghyujiki#jkasjkajska#nmasnam'.replace('#',''))
print(a.replace('x','ramesh'))

a = 'code Ramesh python'
print(lin(a))
b = a.split() #by default it we have space if split (returns list)
print(b)
print(len(b))
c = 'code ramesh python'
d = c.split(',')
print(d)
e = c.split(',')
print(e)


#join(interable)-->concatenate any number of strings

a = 'code'
b= 'gnan'
print(a,join(b))
print(b,join (a))
print('#' ,join('saketh')
print(' ' ,joint('saketh')

#string testing methods (bolean)
#isalpha(), isalpha(), isdigit(), issupper(), isslower()....

a = 'codegnan123'
print(a,isalnum())# returns to from alpha numeric strings else false
b = 'codegna'
print(b.isalnum())
print(a.isalpha()) #returns true only for alphabets
print(a.isalpha()) #returns True only for digit string
print('8106429771'.isdigit()) #this has upper edge (numbers,fractions,romans)
#startawith() -->how its starting
print('codegnan'.startswith('c'))
print('codegnan'.startswith('g',4))
print('codegnan'.endswith('f'))


print('codegnan'.islower()) #returns True for all lowercase
print('codegnan'.isupper()) #returns True for all uppercase
print('codegnan python'.istitle())

#Space removal --> strip() (removes leading and trailing spaces)

a=' codegnan '
print(a.strip())
b = input("Enter the string:").strip().lower()
print(b)
'''
#zfill() filling with zeros as per the given numeric string
print('234'.zfill(4))
print('234'.zfill(7))
#Center(),1jusr(), -->Aligment of stroing (check length and the
#modify the width accordingly)
print('hai'.center(6))
print('hai'.center(6,'#'))

print('hai'.ljust(6,'#'))
print('hai'.rjust(6,'#'))


















