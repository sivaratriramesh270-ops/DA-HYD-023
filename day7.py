#same program with break esage
'''
work_log = [0,1,1,1,0,1]
#result variable -->longest_streak
longest_streak = 0
current_streak = 0
for day in work_log:
    if day == 1:
        #print(day)
        current_streak = current_streak + 1
        if current_streak > longest_streak:
            longest_streak = current_streak
    else:
        current_streak = 0 #streak breaks
else:
    print(f'Longest_streak is {longest_streak}')
print("Execution done")

#for_else with Notifications scenario

notification = [0,0,0,1,0]
notifications = list(map(int,input("Enter the value --> 0 or 1:"). split(',')))
print(notifications)
for notification in notifications:
    if notification == 1:
        print('Unread Notification')
        break
else:
    print('All caught Up')

Syntax while:

while <condition>:
    statement(s).....
    ........
    .......


while true:
    print("yes")

#It runs as infinate loop we need to press we need to press Ctrl+C (keyboard interrupt)

i = 0 #initialised statement
while i<=10:
    print(i)
    i=i+1 #counter

#Get the counter from 10 to 1
i = 10
while i>=1:
    print(i)
    i = 10
    print(i)
    i = i - 1 #decrement i-=1


i = 0
while i<=10:
    prinyt(10-i)
    i = i +1
'''

#banking scenario --> PIN authentication if more than 3 attempts
#Account locked..

pin = "2612"
max_attempts = 3
current_attempt = 0
while current_attempt <= max_attempts:
    entered_pin = input("Enter the ATM PIN:")
    if entered_pin == pin:
        print("Login Successful")
        break
        #continue #it holdes 
    else:
        print("Entered PIN is wrong..Try again carefully")
        current_attempt +=1
else:
    print("Account locked,try after24hours...")


























