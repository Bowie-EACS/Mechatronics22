"""Challenge 1 A Mario R. 8th"""  

import mechatronics as mech
import time
#associate led, spkr, and ranger with GPIO pins
LED_1 = 11
LED_2 = 9
LED_3 = 10
LED_4 = 13
LED_5 = 6
LED_6 = 5
SPKR = 12
LOW_FREQ = 300
TRIG_1 = 22
ECHO_1 = 27
TRIG_2 = 15
ECHO_2 = 24
ON = 1
OFF = 0


#initialize LED, speaker, and ranger
mech.initialize_led(LED_1)  
mech.initialize_led(LED_2)
mech.initialize_led(LED_3)
mech.initialize_led(LED_4)  
mech.initialize_led(LED_5)
mech.initialize_led(LED_6)
mech.initialize_speaker(SPKR)
mech.initialize_ranger(TRIG_1, ECHO_1)
mech.initialize_ranger(TRIG_2, ECHO_2)

#this function senses an object at whatever distance and based on the distance will turn on/off the spkr along with ceratin lights
def print_distance_then_wait():
    distance = mech.get_distance(TRIG_1, ECHO_1)
    print("The distance 1 is ", distance)
    if distance != None:
        if distance == 10:
            time. sleep(8)
            mech.play_speaker(SPKR, ON, LOW_FREQ) #Turn speaker on
        elif (distance < 10) and (distance >= 5):
            mech.set_led(LED_1, ON)
            mech.set_led(LED_3, ON)
            time.sleep(1)
            mech.set_led(LED_1, OFF)
            mech.set_led(LED_3, OFF)
        elif (distance > 10) or (distance < 30) or (distance < 5):
            mech.set_led(LED_2, ON)
            mech.play_speaker(SPKR, ON, LOW_FREQ)
            time.sleep(1.5)
            mech.set_led(LED_2, OFF)
            mech.play_speaker(SPKR, OFF, 0)
        else:
            mech.play_speaker(SPKR, OFF, 0)#Turn speaker off
            mech.set_led(LED_1, OFF)
            mech.set_led(LED_2, OFF)
            mech.set_led(LED_3, OFF)
    else:
        print("The distance 1 is ", distance)

#this is the same funtion as the one above just for the back sensor
def print_distance_then_wait_2():
    distance_2 = mech.get_distance(TRIG_2, ECHO_2)
    print("The distance 2 is ", distance_2)
    if distance_2 != None:
        if distance_2 == 10:
            time. sleep(8)
            mech.play_speaker(SPKR, ON, LOW_FREQ) #Turn speaker on
        elif (distance_2 < 10) and (distance_2 >= 5):
            mech.set_led(LED_4, ON)
            mech.set_led(LED_6, ON)
            time.sleep(1)
            mech.set_led(LED_4, OFF)
            mech.set_led(LED_6, OFF)
        elif (distance_2 > 10) or (distance_2 < 30) or (distance_2 < 5):
            mech.set_led(LED_5, ON)
            mech.play_speaker(SPKR, ON, LOW_FREQ)
            time.sleep(1.5)
            mech.set_led(LED_5, OFF)
            mech.play_speaker(SPKR, OFF, 0)
        else:
            mech.play_speaker(SPKR, OFF, 0)#Turn speaker off
            mech.set_led(LED_4, OFF)
            mech.set_led(LED_5, OFF)
            mech.set_led(LED_6, OFF)
    else:
        print("The distance 2 is ", distance_2)
           
     
try:
    #runs the code until you press ctrl + c, it will read the distance
    #in the front and then the back and continuosly do this until user stop it
    while True:
        print_distance_then_wait()
        print("moving on to #2")
        print_distance_then_wait_2()
        print("moving on to #1")
#stops the code when user presses ctrl + c
except KeyboardInterrupt:  
    mech.set_led(LED_1, OFF)
    mech.set_led(LED_2, OFF)
    mech.set_led(LED_3, OFF)
    mech.set_led(LED_4, OFF)
    mech.set_led(LED_5, OFF)
    mech.set_led(LED_6, OFF)
    mech.play_speaker(SPKR, OFF, 0)
    mech.cleanup()
    print ("You stopped the program")    


