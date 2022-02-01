"Spin Motor"
import mechatronics as mech
import time

MOTOR = 5

mech.initialize_motor(MOTOR)

mech.rotate_motor(MOTOR, 35) # spin clockwise at a certain speed
time.sleep(3.5)     # wait 3 seconds
mech.rotate_motor(MOTOR, 60) # spin counterclockwise at a certain speed
time.sleep(2)      # wait 2 seconds
mech.rotate_motor(MOTOR, 90) # stop motor



LDR = 0 # associat LDR with channel on the MCP3008 ADC

while True:
    #create a local veriable that holds current LDR value
    brightness = mech.read_ldr(LDR)
    print ("LDR level is", brightness)  # showLDR value in window
    time.sleep(.25)     #wait 1 second
    if brightness > 2.0:
        time.sleep(1)
    else:
        time.sleep(.75)
    
    
try:
    print_brightness_then_wait()
except KeyboardInterrupt:
    mech.rotate_motor(MOTOR,0)
    mech.cleanup()
    print ("You stopped the program")
    
def calculate_speed(rpm, diameter):
    """
        find the speed of a  ar using a wheel's diameter and rpm.
        arguments:
            rpm (in 1/minute; can be either interer or float)
            diameter (in meters; cna be either intergers fo float)
        Returns: speen (in meters/minute)
    """
    PI = 3.14
    speed = PI * rpm * diameter
    return speed

#print a sentence that gives the speed uning the calculate_speed() function
print("at", 50, "rpm and with", .64, "meter wheels", end="")
print("a car moves at", calculate_speed(50, .64), "meter per minute")

#create two variables
rpm1 = 100
diam1 = 1

#print a sentence that gives the speed using the calculate_speed() function
print("At", rpm1, "rpm and with", diam1, "meter wheels,", end="")
print("a car moves at", calculate_speed(rpm1, diam1),"meters per minute.")
    
