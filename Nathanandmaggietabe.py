import mechatronics as mech
import time

MOTOR = 18 # Associate motore with GPIO pin
mech.initialize_motor(MOTOR)  #Initialize motor

TRIG = 24 # Associate Trigger with GPIO pin
ECHO = 7 # Associate Echo with GPIO pin
mech.initialize_ranger(TRIG, ECHO) # Initilize Ultrasonic Ranger
#motor_input = (3.3 * distance) + 1
#mech.rotate_motor(MOTOR, motor_input)

def print_distance_then_wait():
    while True:
        distance = mech.get_distance(TRIG, ECHO)
        print ("The distance is", distance)
        if distance != None:
            if distance > 20:
                print("D = greater than 20")
                mech.rotate_motor(MOTOR, 50)
                time.sleep(2)
            elif (distance < 20) and (distance >= 5):
                print("D is between 5 and 20")
                mech.rotate_motor(MOTOR, 85)
                time.sleep(1)
            #elif (distance > 20) or (distance , 5):
            else:
                print("D is something else")
                mech.rotate_motor(MOTOR, 20)
                time.sleep(1.5)


try:
    print_distance_then_wait()
except KeyboardInterrupt:
    mech.rotate_motor(MOTOR, 0)
    mech.cleanup()
    print ("You stopped the program")