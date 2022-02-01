import mechatronics as mech
import time

MOTOR = 18 #GPIO PIN
TRIG = 24
ECHO = 7


mech.initialize_motor(MOTOR)
mech.initialize_ranger(TRIG, ECHO)

distance = mech.get_distance(TRIG, ECHO)

def motor_move(distance):
    global motor_speed
    if distance == None:
        print (distance)
        motor_speed = 50
    elif distance >= 100:
        print (distance)
        motor_speed = 50
    else:
        print (distance)
        motor_speed = distance
    print (motor_speed)
    return(motor_speed)


motor_speed = 50
while True:
    distance = mech.get_distance(TRIG, ECHO)
    speed = motor_move(distance)
    mech.rotate_motor(MOTOR, speed)

