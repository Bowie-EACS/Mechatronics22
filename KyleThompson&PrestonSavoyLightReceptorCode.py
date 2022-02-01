import mechatronics as mech
import time

# Associate LED with GPIO pin
LED_1 = 17
LED_2 = 27
LED_3 = 22
LED_4 = 10
LED_5 = 9
LED_6 = 11

# Initialize LED
mech.initialize_led(LED_1)
mech.initialize_led(LED_2)
mech.initialize_led(LED_3)
mech.initialize_led(LED_4)
mech.initialize_led(LED_5)
mech.initialize_led(LED_6)

# Define constants designating On and Off
ON = 1
Off = 0

# Associate LDR with channel on the MCP3008 ADC
LDR = 0

while True :
     #Create a local variable that holds current LDR value
    brightness = mech.read_ldr(LDR)
    print("LDR level is", brightness)  #Show LDR value in window
    time.sleep(1)          #wait 1 second
    if brightness == 2.0:
        time.sleep(8)
    elif (brightness < 2.0) and (brightness >= 1.0):
        time.sleep(2.5)
    elif (brightness > 2.0) or (brightness < 3.5):
        time.sleep(0.1)
        
try:
    print_brightness_then_wait()
except KeyboardInterrupt:
    mech.set_led(LED_1, OFF)
    mech.set_led(LED_2, OFF)
    mech.set_led(LED_3, OFF)
    mech.set_led(LED_4, OFF)
    mech.set_led(LED_5, OFF)
    mech.set_led(LED_6, OFF)
    mech.cleanup()
    print ("You stopped the program")

    
    
    