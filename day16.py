'''
Seqences --> Strings,Lists,Tuples,set,Frozenset
Mapping --> Dictionary

#sets --> A Set is a Unique Collection of objects,Unordered,Mutable,
#Hashing,Unindexed,Unique,Heterogenous
#set(),{}
#a = {} its an empty dictionary
a = set()
print(type(a))
stud_ids = {123,345,234,564,234}
print(stud_ids)
print(type(stud_ids))
print(len(stud_ids))
#print(stud_ids[2]) #TypeError

print(234 in stud_ids)
#print(stud_ids *2)
#print(stud_ids + stud_ids) #Two sets cannot be Merged

#data = (12,3,4,5,[12,3,4],'ramesh')
#print(data) #No lists inside a set (hashing technique) Lists are Mutable

data = {12,3,4,5,(12,3,4),'ramesh'}
print(data)
print(len(data))
for i  in data:
    print(i)

#method on sets -->add(),Update(),remove(),discad(),pop()
names = {'sai','saketh','kiran','codegnan'}
print(len(names))
names.add('python')
print(names)
#names.add( 'saketh','poll')
#print(names)
names.add(('poll','police'))
print(names)
#updae 
da_names = {'main','akash','sai','sonu'}
names.update(da_names)
print(names)
print(len(names))
print(da_names)
print(len(da_names))
da_names(len(da_names))
print(len(names))
print(len(da_names))

#remove(),discard(),pop(),clear()
#remove() removes an elemet from the set (it must be a member)
da_names.remove('sai')
print(da_names)
#da_names.remove('sai') #KeyError
#discard() will remove an element if its present else it ignores
da_names.discard('codegnan')

da_names.pop()
print(da_names)
print(da_names.pop()) #removes and returns an arbritrary eleent
print(da_names)
da_names.clear()
print(da_names)
da_names.add('saira')
print(da_names)
da_names.update(['sai','saketh'])
print(da_names)

#copy() #creates a shallow copy of set(independent of each other)
d = da_names.copy()
print(d)
d.update({'python','codegnan'})
print(d)
print(da_names)

#mathametical operations -->union(),intersection(),difference(),symmetric_da()
#issubset(),issuperset(),isdisjoit()

da_23 = {12,23,34,45,23,36}
da_24 = {34,46,47,23}
event = da_23.union(da_24)
print(event)
print(len(event))
#common = da_23.intersetion(da_24)
common = da_23 & da_24 #& intersetion()
print(common)
#print(len(common))
common = da_23,intersetion_update(da_24)
print(common) #it returns None
print(da_23) #common elements are finally stored

print(da_23)
print(da_24)
#difference() removes common elements and print remaining elements from fiurst sets
#diff = da_23.difference(da_24)
#print(diff)
#f = da_23 - da_24
#print(f)
#symmetic_difference() -->removre common elements and print all rmng
#elements from two sets
symm = da_23.symmetric_difference(da_24)
print(symm)
h = da_23 ^ da_24
#print(h)

#issubset() -->check for all elements to be present in other set
da_24.remove(46)
da_24.remove(47)

print(da_24.issubset(da_23))
print(da_23.issuperset(da_24))

#isdisjoint() returns False for sets having common elements
print(da_23.isjoint(da_24))
'''








