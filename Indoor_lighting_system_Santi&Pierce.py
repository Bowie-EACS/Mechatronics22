"""
Lighting System Code
Santiago Montesinos
Began 1.18.22
"""
import mechatronics as mech
import time

#sets LED's to their pin numbers
LED_1 = 17
LED_2 = 27
LED_3 = 22
LED_4 = 10
LED_5 = 9
LED_6 = 11

#initializes each Pi pin
mech.initialize_led(LED_1)
mech.initialize_led(LED_2)
mech.initialize_led(LED_3)
mech.initialize_led(LED_4)
mech.initialize_led(LED_5)
mech.initialize_led(LED_6)

#sets an on and off variable
ON = 1
OFF = 0

#Associate LDR with its channel
LDR = 0


while True:
    brightness = mech.read_ldr(LDR)#gathers data from the light resistor
    print(brightness)
    time.sleep(1)
    


#light show :)
"""for i in range (20):
    mech.set_led(LED_1, ON)
    time.sleep(0.041)
    mech.set_led(LED_1, OFF)
    
    mech.set_led(LED_2, ON)
    time.sleep(0.041)
    mech.set_led(LED_2, OFF)
    
    mech.set_led(LED_3, ON)
    time.sleep(0.041)
    mech.set_led(LED_3, OFF)
    
    mech.set_led(LED_4, ON)
    time.sleep(0.041)
    mech.set_led(LED_4, OFF)
    
    mech.set_led(LED_5, ON)
    time.sleep(0.041)
    mech.set_led(LED_5, OFF)
    
    mech.set_led(LED_6, ON)
    time.sleep(0.041)
    mech.set_led(LED_6, OFF)
"""




