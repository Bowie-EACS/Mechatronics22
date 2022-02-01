import mechatronics as mech
import time

MOTOR = 18 #GPIO PIN
TRIG = 24
ECHO = 7


mech.initialize_motor(MOTOR)
mech.initialize_ranger(TRIG, ECHO)

distance = mech.get_distance(TRIG, ECHO)

while True:
    distance = mech.get_distance(TRIG, ECHO)
    if distance == None:
        print (distance)
        mech.rotate_motor(MOTOR, 50)
    elif distance < 50:
        print(distance)
        mech.rotate_motor(MOTOR, 60)
    elif distance == 50:
        print(distance)
        mech.rotate_motor(MOTOR, 50)
    else:
        print(distance)
        mech.rotate_motor(MOTOR, 30)

