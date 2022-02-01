import mechatronics as mech
import time

#associates motor with pin
MOTOR = 5


mech.initialize_motor(MOTOR) #Initializes motor
L_LDR = 2 # associates the left LDR with the 3rdnd channel on the MCP3008
R_LDR = 0 # associates the right LDR with the 1st channel on the MCP3008 

mech.rotate_servo(MOTOR,120) #puts the carbaord upright in the begining to reset it


# If there is more light on the right side, the carboard will "point" to it, and vise versa
while True:
    L_brightness = mech.read_ldr(L_LDR)
    R_brightness = mech.read_ldr(R_LDR)
    time.sleep(0.1)
    if L_brightness > R_brightness:
        mech.rotate_servo(MOTOR, 90)
    elif R_brightness > L_brightness:
        mech.rotate_servo(MOTOR,150)
    
        







