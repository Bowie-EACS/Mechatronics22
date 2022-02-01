"""LED Challenge 1A"""
import mechatronics as mech
import time

#Defines Leds to make code more readable
LED_1 = 17
LED_2 = 27
LED_3 = 22
LED_4 = 10
LED_5 = 9
LED_6 = 11

#initializes leds
mech.initialize_led(LED_1)
mech.initialize_led(LED_2)
mech.initialize_led(LED_3)
mech.initialize_led(LED_4)
mech.initialize_led(LED_5)
mech.initialize_led(LED_6)

#defines variables that control the led's states
ON = 1
OFF = 0

#next two functions compact code so we dont have to type as much
def toggleLightsOn():
    mech.set_led(LED_1, ON)
    mech.set_led(LED_2, ON)
    mech.set_led(LED_3, ON)
    mech.set_led(LED_4, ON)
    mech.set_led(LED_5, ON)
    mech.set_led(LED_6, ON)

def toggleLightsOff():
    mech.set_led(LED_1, OFF)
    mech.set_led(LED_2, OFF)
    mech.set_led(LED_3, OFF)
    mech.set_led(LED_4, OFF)
    mech.set_led(LED_5, OFF)
    mech.set_led(LED_6, OFF)
    

#initializes light dependent resistor
RIGHT_LDR = 0
LEFT_LDR = 2
POTENTIOMETER = 7



#main
try:
    while True:
        #Detects the brightness outside
        brightness_right = mech.read_ldr(RIGHT_LDR)
        brightness_left = mech.read_ldr(LEFT_LDR)
        
        #Reads the potentiometer value
        potentiometer_value = mech.read_ldr(POTENTIOMETER)
        potentiometer_value = potentiometer_value/10 + 0.2

        #prints the brightness detected on both sides
        print ("Left LDR level is: ", brightness_left, " Right LDR level is: ", brightness_right)
        time.sleep(0.1)
        
        #determines which LEDs should be lit up based on the readings of the light-dependent resistors
        if brightness_right < 1.4 + potentiometer_value:
            
            if brightness_left < 2.69 + potentiometer_value:
                toggleLightsOn()
                
            elif brightness_left < 2.75 + potentiometer_value:
                toggleLightsOn()
                mech.set_led(LED_2, OFF)
                
            else:
                toggleLightsOn()
                mech.set_led(LED_1, OFF)
                mech.set_led(LED_2, OFF)
                mech.set_led(LED_3, OFF)
               
                
                
        elif brightness_right >= (1.4 + potentiometer_value) and brightness_right < (1.95 + potentiometer_value) :
            
            if brightness_left < 2.69 + potentiometer_value:
                toggleLightsOn()
                mech.set_led(LED_5, OFF)
                
            elif brightness_left < 2.75 + potentiometer_value:
                toggleLightsOn()
                mech.set_led(LED_2, OFF)
                mech.set_led(LED_5, OFF)
                
            else:
                toggleLightsOff()
                mech.set_led(LED_6, ON)
                mech.set_led(LED_4, ON)
                
                
        else:
            
            if brightness_left < 2.69 + potentiometer_value:
                toggleLightsOn()
                mech.set_led(LED_4, OFF)
                mech.set_led(LED_5, OFF)
                mech.set_led(LED_6, OFF)
                
            elif brightness_left < 2.75 + potentiometer_value:
                toggleLightsOff()
                mech.set_led(LED_1, ON)
                mech.set_led(LED_3, ON)
                
            else:
                toggleLightsOff()
            
      
  
# stops the programwhen teh user presses control + "C"            
except KeyboardInterrupt:
    toggleLightsOff()
    mech.cleanup()
    print ("You stopped the program :)")
    


