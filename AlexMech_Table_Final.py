#Imports
import mechatronics as mech
import time

#cont
motor = 18
trig = 24
echo = 7
cspeed = 0
SPKR = 12
ON = 1
OFF = 0

#Rotate function
def rotate(speed = 0, seconds = -1):
    '''
    This is to be used to turn the specifed motor\n teset
    Where you rotate the motor with an x ammount of speed an y ammount of seconds\n
    If it is -1 then spin forever\n
    Ex: I want to rotate the motor with a speed of 10 for 2 seconds\n
    >>>rotate(10,2)
    '''
    global cspeed#Grab global speed
    
    if (speed < 0):#If it is -
        speed = (100 + speed)#Set it so it is positive
        
    if (cspeed != speed):#If the speed needs to be updated
        mech.rotate_motor(motor, speed)#Change the speed!
        
    cspeed = speed#Update the global speed
    
    if (seconds != -1):#If there is a delay
        time.sleep(seconds)#Sleep
        mech.rotate_motor(motor, 0)#Stop the motor after
        cspeed = 0#Update global speed

#Inits
mech.initialize_motor(motor)
mech.initialize_ranger(trig, echo)
mech.initialize_speaker(SPKR)


#For keyboard except
try:
    
    while (True):#Main loop
        
        distance = mech.get_distance(trig, echo)#Get motor distance
        
        if (distance is not None):#If the distance is not None
            
            if (distance == 15 or distance > 30):#If it is at the middle or too far away
                
                rotate(0)#Stop motor
                mech.play_speaker(SPKR, OFF, 300)#Stop speaker
                
            elif (distance > 15 and distance < 30):#If it is at the first range
                
                rotate(3 * (30 - distance))#Spin motor given distance multiplyer
                mech.play_speaker(SPKR, ON, 300)#Start Speaker
                
            elif (distance < 15):#If it falls in the last range
                
                rotate(distance*-3)#Spin motor given distance multiplyer
                mech.play_speaker(SPKR, ON, 300)#Start speaker
                
except KeyboardInterrupt:#If the users presses (Ctrl + C)
    
    print("Exit!")#Print exit
    mech.play_speaker(SPKR, OFF, 300)#Stop the speaker
    rotate(0)#Stop the motor

