"""You are in a hallway lined with 100 lockers. You start with one pass and open the lockers, so that the opened lockers are now with their doors opened out. You begin by closing every second locker. Then you go to close every third locker and close it if it is open or open it if it’s closed — we will refer to this as "toggling" the lockers. You continue toggling every nth locker on pass number n. After your hundredth pass of the hallway, in which you toggle only locker number 100, how many lockers are open?"""
#0 = closed
#1 = open

#Locker doors are closed
locker = [0] * 100

#Locker doors are opened
locker = [1] * 100

#Every second locker is opened
for i in range(0,100,2):
        locker[i] = 0

print(locker)

#Locker which is divisible by pass number is toggled
for i in range(3,100):
    for j in range(0,100):
        
        if(j != 0 and j % i == 0):
            if(locker[j] == 0):
                locker[j] = 1

            else:
                locker[j] = 0

#Final locker is toggled
if(locker[99] == 0):
    locker[99] = 1

else:
    locker[99] = 0

print(locker)
num = 0

#Counting number of opened lockers
for i in range(100):
    if(locker[i] == 1):
        num += 1

print("Number of open lockers: ",num)

