import mechatronics as mech
import time

MOTOR = 18 #GPIO PIN

mech.initialize_motor(MOTOR)
for i in range (5):
    mech.rotate_motor(MOTOR, 1) #spin clockwise at speed 35
    time.sleep(3.5) #wait 3.5 seconds
    mech.rotate_motor(MOTOR, 100)
    time.sleep(2)
    mech.rotate_motor(MOTOR, 50)
    time.sleep(3)
