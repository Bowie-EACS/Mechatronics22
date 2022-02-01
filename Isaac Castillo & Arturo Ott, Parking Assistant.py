import mechatronics as mech
import time


# assosiate leds with GPIO pins
# front
LED_FAR = 10
LED_MID = 9
LED_NEAR = 11

# back
LED_FAR2 = 5
LED_MID2 = 6
LED_NEAR2 = 13

# Initialize LEDs
#front
mech.initialize_led(LED_FAR)
mech.initialize_led(LED_MID)
mech.initialize_led(LED_NEAR)

# back
mech.initialize_led(LED_FAR2)
mech.initialize_led(LED_MID2)
mech.initialize_led(LED_NEAR2)

# initialize speaker
SPKR = 12

mech.initialize_speaker(SPKR)

LOW_FREQ = 300

# assosiate trig and echo with GPIO pins
# front
TRIG = 22
ECHO = 27

# back
TRIG2 = 15
ECHO2 = 24

# initialize ranger
mech.initialize_ranger(TRIG, ECHO)
mech.initialize_ranger(TRIG2, ECHO2)

# initialize constants
ON = 1
OFF = 0


# sensor function
# gets distance, lights up leds and makes noise 
def sensor():
    while True:
        # FRONT SENSOR
        
        # get distace
        distance = mech.get_distance(TRIG, ECHO)
        
        # check for none distance (avoid no values)
        # turn everyting off
        if distance == None:
          print("no distance")
          mech.set_led(LED_FAR, OFF)
          mech.set_led(LED_MID, OFF)
          mech.set_led(LED_NEAR, OFF)
          mech.play_speaker(SPKR, OFF, 0)
        # turns on one led if distance is greater than 10
        elif distance > 20:
            mech.set_led(LED_MID, OFF)
            mech.set_led(LED_NEAR, OFF)
            mech.set_led(LED_FAR, ON)
            mech.play_speaker(SPKR, ON, 300)
        # turns on two leds when distance is inbetween 5 qnd 10
        elif (distance < 20) and (distance >= 10):
            mech.set_led(LED_FAR, ON)
            mech.set_led(LED_NEAR, OFF)
            mech.set_led(LED_MID, ON)
            mech.play_speaker(SPKR, ON, 900)
        # turns on all leds when distance is less than 5
        elif  distance < 10:
            mech.set_led(LED_MID, ON)
            mech.set_led(LED_FAR, ON)
            mech.set_led(LED_NEAR, ON)
            mech.play_speaker(SPKR, ON, 1200)


        # BACK SENSOR
        
        # get distance
        distance = mech.get_distance(TRIG2, ECHO2)
        
        # check for none distance (avoid no values)
        # turn everyting off
        if distance == None:
          print("no distance")
          mech.set_led(LED_FAR2, OFF)
          mech.set_led(LED_MID2, OFF)
          mech.set_led(LED_NEAR2, OFF)
          mech.play_speaker(SPKR, OFF, 0)
      # turns on one led if distance is greater than 10
        elif distance > 20:
            mech.set_led(LED_MID2, OFF)
            mech.set_led(LED_NEAR2, OFF)
            mech.set_led(LED_FAR2, ON)
            mech.play_speaker(SPKR, ON, 300)
        # turns on two leds when distance is inbetween 5 qnd 10
        elif (distance < 20) and (distance >= 10):
            mech.set_led(LED_FAR2, ON)
            mech.set_led(LED_NEAR2, OFF)
            mech.set_led(LED_MID2, ON)
            mech.play_speaker(SPKR, ON, 900)
        # turns on all leds when distance is less than 5
        elif  distance < 10:
            mech.set_led(LED_MID2, ON)
            mech.set_led(LED_FAR2, ON)
            mech.set_led(LED_NEAR2, ON)
            mech.play_speaker(SPKR, ON, 1200)
    
# always run sensor function  
try:
    sensor()
# if ctrl + c then turn everyting off and stop program
except KeyboardInterrupt:
    mech.set_led(LED_FAR, OFF)
    mech.set_led(LED_MID, OFF)
    mech.set_led(LED_NEAR, OFF)
    mech.set_led(LED_FAR2, OFF)
    mech.set_led(LED_MID2, OFF)
    mech.set_led(LED_NEAR2, OFF)
    mech.play_speaker(SPKR, OFF, 0)
    mech.cleanup()
    print("You stopped the program")