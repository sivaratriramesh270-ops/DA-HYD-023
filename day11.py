'''
code = "1006"
max_attempts = 3
current_attempt = 0
while current_attempt <= max_attempts:
    entered_pin = input("enter the moibile code:")
    if entered_pin == pin:
        print("login sucessful")
        break
    print("entered PIN is wrong..try again carefully")
    current_attempt +=1
else:
    print("account locked")
    

secrect = 123
guess = int(input())
while guess != secrect:
    if guess < secrect:
        print("too low")
    else:
        print("too high")
    guess = int(input())
print("correct guess")

food=input()
count=0
while food != "exit":
    count +=1
    food=input()
print("total no of items ordered",count)
'''   
Secrect="python"
current=0
max_attempts = 3
while current< max_attempts:
    a = input()
    if(a==secrect):
        print("access again")
        break
    use:
        remaining = max attempts currect
        print(f"wrong gess & you have only")
        currect +=



