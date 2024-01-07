import random 

guess = 0.0
cube = 27
increment = 0.1
elipsion = 0.1
cnt = 0


while abs(guess**3 - cube) >= elipsion:
    guess = guess + increment
    cnt=cnt+1
    print( cnt, ")" , guess)
    
if abs(guess**3 - cube) >= elipsion:
    print("faild on the cude root of" , cube)
else:
    print("\n")
    print(  cnt, ")" ,  guess , "is the cude root of" , cube)



    