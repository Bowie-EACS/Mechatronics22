"Table Project"
"By Decker and Connor, 1/18/2022"

import mechatronics as mech
import time
#Pin variable
MOTOR = 18
mech.initialize_motor(MOTOR)

TRIG = 24
ECHO = 7
mech.initialize_ranger(TRIG, ECHO)
while True:
    distance = mech.get_distance(TRIG, ECHO)
    print (distance)
    if distance != None:
        motor_input = (35/30 * float(distance))+30
        if (distance < 30):
            mech.rotate_motor(MOTOR, float(motor_input))
            time.sleep(0.1)
        #elif (distance < 25):
            #mech.rotate_motor(MOTOR, motor_input)
            #time.sleep(0.01)
        #elif (distance > 25) and (distance <= 50):
            #mech.rotate_motor(MOTOR, motor_input)
            #time.sleep(0.01)
