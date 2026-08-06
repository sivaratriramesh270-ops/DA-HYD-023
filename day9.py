'''
product = list(map(int,input().split(',')))
total = 0
for i in product:
       total = total+i
print(total)

#Passward Analyzer
passward = input("Enter password")
upper = 0
lower = 0
digit = 0
special = 0
for i in password:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower += 1
    elif i.isdigit():
        digit += 1
    else:
        special += 1

        
print("upper letter:",upper)
print("lower letter:",lower)
print("digit letter:",digit)
print("special characters:",special)
'''
#Domain
email = input().split()
for mail in email:
    print(mail.split('@')[1])
























