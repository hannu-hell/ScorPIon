from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
import time
import os


print("                          ___")
print("                        /   /") 
print("                       |   |")
print("                        \  |")
print("                         | |")
print("                         | |")
print("                          \ \\")
print("                       _____\ \______")
print("                     /                \\")
print("              ____ /                    \ ____")
print("            /     |                      |     \\")
print("          /    ___ ---------------------- ____   \\")
print("         \   |                               |   /")
print("           \  \                              / /")
print("             ```                            '''")
print("                          _____   ______")
print("                         ||   ||    ||")
print("  ___    __  ___   ___   ||___||    ||     ___       ___")
print(" ||__  ||   || || ||_||  ||         ||    || ||  ||/   ||")
print("  __|| ||__ ||_|| || \\\  ||       __||__  ||_||  ||    ||")

print("\n")
print("Powered by Raspberry Pi zero W")
print("Based on Python")
print("Raspberry Pi Camera Interface - (github:silvanmelchior/RPi_Cam_Web_Interafce)")
print("Program and 3D model - Hannu (github:hannu-hell)")
print("This is an open source project and all rights granted to modify and reproduce")
print("and sell as the user may deem fit provided credit is given where credit is due :)")
print("\n\n")

time.sleep(2)

# ScorPiion servo arrangement diagram

#         15
#          |
#         14
#        | |
#   13--9   7--11
#      |     |
#      |     |
#   10--6   8--12
#        .^.

#leg1Base = 6
#leg2Base = 7
#leg3Base = 8
#leg4Base = 9
#leg1Tip = 10
#leg2Tip = 11
#leg3Tip = 12
#leg4Tip = 13
#camBase = 14
#camTip = 15

def test_move(s, limit_x, limit_y):
    kit.servo[s].angle = limit_x
    time.sleep(2)
    kit.servo[s].angle = 90
    time.sleep(2)
    kit.servo[s].angle = limit_y
    time.sleep(2)
    kit.servo[s].angle = 90


def move_angle():
    while True:
        option = input("Move single servo? y/n")
        if option == "y":
            single = True
        else:
            single = False

        if not single:
            servos = input("Enter servos to move in the format <servonumber1.servonumber2..>")
            angles = input("Enter angle to move")
            try:
                a = int(angles)
                s = servos.split(".")
                for i in s:
                    kit.servo[int(i)].angle = a
            except:
                print("Input Invalid")


        if single:
            servo = input("Please enter servo number")
            angle = input("Please enter rotation angle")

            if servo == "q" or angle == "q":
                break
            
            try:
                servo = int(servo)
                angle = int(angle)
                kit.servo[servo].angle = angle
            except:
                print("Write valid numbers")


def walk_forward(t):
    kit.servo[14].angle = 140
    kit.servo[15].angle = 90

    kit.servo[6].angle = 90
    kit.servo[10].angle = 50
    
    kit.servo[7].angle = 90
    kit.servo[11].angle = 60
    
    kit.servo[8].angle = 90
    kit.servo[12].angle = 140
    
    kit.servo[9].angle = 90
    kit.servo[13].angle = 130


    kit.servo[10].angle = 70
    time.sleep(t)
    kit.servo[6].angle = 120
    time.sleep(t)
    kit.servo[10].angle = 50
    time.sleep(t)

    kit.servo[11].angle = 80
    time.sleep(t)
    kit.servo[7].angle = 60
    time.sleep(t)
    kit.servo[11].angle = 60
   
    time.sleep(0.1)
    kit.servo[6].angle = 90
    time.sleep(0.05)
    kit.servo[7].angle = 90


    kit.servo[12].angle = 110
    time.sleep(t)
    kit.servo[8].angle = 60
    time.sleep(t)
    kit.servo[12].angle = 140
    time.sleep(t)
   
    kit.servo[13].angle = 110
    time.sleep(t)
    kit.servo[9].angle = 120
    time.sleep(t)
    kit.servo[13].angle = 130
    time.sleep(t)

    time.sleep(0.1)
    kit.servo[8].angle = 90
    time.sleep(0.05)
    kit.servo[9].angle = 90


def walk_backward(t):
    kit.servo[14].angle = 140
    kit.servo[15].angle = 90

    kit.servo[6].angle = 90
    kit.servo[10].angle = 50
    
    kit.servo[7].angle = 90
    kit.servo[11].angle = 60
    
    kit.servo[8].angle = 90
    kit.servo[12].angle = 140
    
    kit.servo[9].angle = 90
    kit.servo[13].angle = 130


    kit.servo[10].angle = 70
    time.sleep(t)
    kit.servo[6].angle = 60
    time.sleep(t)
    kit.servo[10].angle = 50
    time.sleep(t)

    kit.servo[11].angle = 80
    time.sleep(t)
    kit.servo[7].angle = 120
    time.sleep(t)
    kit.servo[11].angle = 60
   
    time.sleep(0.1)
    kit.servo[6].angle = 90
    time.sleep(0.05)
    kit.servo[7].angle = 90


    kit.servo[12].angle = 110
    time.sleep(t)
    kit.servo[8].angle = 120
    time.sleep(t)
    kit.servo[12].angle = 140
    time.sleep(t)
   
    kit.servo[13].angle = 110
    time.sleep(t)
    kit.servo[9].angle = 60
    time.sleep(t)
    kit.servo[13].angle = 130
    time.sleep(t)

    time.sleep(0.1)
    kit.servo[8].angle = 90
    time.sleep(0.05)
    kit.servo[9].angle = 90


def turn_right(t):
    kit.servo[14].angle = 140
    kit.servo[15].angle = 90

    kit.servo[6].angle = 90
    kit.servo[10].angle = 50
    
    kit.servo[7].angle = 90
    kit.servo[11].angle = 60
    
    kit.servo[8].angle = 90
    kit.servo[12].angle = 140
    
    kit.servo[9].angle = 90
    kit.servo[13].angle = 130


    kit.servo[10].angle = 70
    time.sleep(t)
    kit.servo[11].angle = 80
    time.sleep(0.1)
    kit.servo[7].angle = 120
    time.sleep(t)
    kit.servo[6].angle = 120
    time.sleep(t)
    kit.servo[10].angle = 50
    time.sleep(t)
    kit.servo[11].angle = 60   
   
    time.sleep(0.1)

    kit.servo[12].angle = 110
    time.sleep(t)
    kit.servo[13].angle = 110
    time.sleep(0.1)
    kit.servo[8].angle = 120
    time.sleep(t)
    kit.servo[9].angle = 120
    time.sleep(t)
    kit.servo[12].angle = 140
    time.sleep(t)
    kit.servo[13].angle = 130

    time.sleep(0.1)


    for i in range(120, 90, -1):
        kit.servo[6].angle = i
        kit.servo[7].angle = i
        kit.servo[8].angle = i
        kit.servo[9].angle = i
        time.sleep(0.01)


def turn_left(t):
    
    kit.servo[14].angle = 140
    kit.servo[15].angle = 90

    kit.servo[6].angle = 90
    kit.servo[10].angle = 50
    
    kit.servo[7].angle = 90
    kit.servo[11].angle = 60
    
    kit.servo[8].angle = 90
    kit.servo[12].angle = 140
    
    kit.servo[9].angle = 90
    kit.servo[13].angle = 130


    kit.servo[10].angle = 70
    time.sleep(t)
    kit.servo[11].angle = 80
    time.sleep(0.1)
    kit.servo[7].angle = 60
    time.sleep(t)
    kit.servo[6].angle = 60
    time.sleep(t)
    kit.servo[10].angle = 50
    time.sleep(t)
    kit.servo[11].angle = 60   
   
    time.sleep(0.1)

    kit.servo[12].angle = 110
    time.sleep(t)
    kit.servo[13].angle = 110
    time.sleep(0.1)
    kit.servo[8].angle = 60
    time.sleep(t)
    kit.servo[9].angle = 60
    time.sleep(t)
    kit.servo[12].angle = 140
    time.sleep(t)
    kit.servo[13].angle = 130

    time.sleep(0.1)


    for i in range(60, 90):
        kit.servo[6].angle = i
        kit.servo[7].angle = i
        kit.servo[8].angle = i
        kit.servo[9].angle = i
        time.sleep(0.01)


def tail_movement():
    kit.servo[14].angle = 140
    kit.servo[15].angle = 80
    for i in range(140, 10, -1):
        kit.servo[14].angle = i
        time.sleep(0.01)
    time.sleep(0.1)
    for j in range(2):
        for i in range(10, 50):
            kit.servo[14].angle = i
            time.sleep(0.01)
        for i in range(50, 10, -1):
            kit.servo[14].angle = i
            time.sleep(0.01)
    time.sleep(2)

    kit.servo[14].angle = 120

    time.sleep(2)

    for i in range(80,170):
        kit.servo[15].angle = i
        time.sleep(0.01)
    time.sleep(0.1)
    for i in range(170, 50, -1):
        kit.servo[15].angle = i
        time.sleep(0.01)
    for i in range(50, 80):
        kit.servo[15].angle = i
        time.sleep(0.01)

    for i in range(120, 140):
        kit.servo[14].angle = i
        time.sleep(0.01)



def dance():

    kit.servo[14].angle = 140
    kit.servo[15].angle = 90

    kit.servo[6].angle = 90
    kit.servo[10].angle = 50
    
    kit.servo[7].angle = 90
    kit.servo[11].angle = 60
    
    kit.servo[8].angle = 90
    kit.servo[12].angle = 140
    
    kit.servo[9].angle = 90
    kit.servo[13].angle = 130

    for i in range(50, 100):
        kit.servo[10].angle = i
        time.sleep(0.01)
    for i in range(130, 80, -1):
        kit.servo[13].angle = i
        time.sleep(0.01)
    
    for j in range(2):
        for i in range(90, 120):
            kit.servo[6].angle = i
            kit.servo[9].angle = i
            time.sleep(0.01)
        for i in range(120, 60, -1):
            kit.servo[6].angle = i
            kit.servo[9].angle = i
            time.sleep(0.01)
        for i in range(60, 90):
            kit.servo[6].angle = i
            kit.servo[9].angle = i
            time.sleep(0.01)

    for i in range(80, 130):
        kit.servo[13].angle = i
        time.sleep(0.01)
    for i in range(100, 50, -1):
        kit.servo[10].angle = i
        time.sleep(0.01)

    time.sleep(2)

    for i in range(140, 90, -1):
        kit.servo[12].angle = i
        time.sleep(0.01)
    for i in range(60, 110):
        kit.servo[11].angle = i
        time.sleep(0.01)
    
    for j in range(2):
        for i in range(90, 120):
            kit.servo[8].angle = i
            kit.servo[7].angle = i
            time.sleep(0.01)
        for i in range(120, 60, -1):
            kit.servo[8].angle = i
            kit.servo[7].angle = i
            time.sleep(0.01)
        for i in range(60, 90):
            kit.servo[8].angle = i
            kit.servo[7].angle = i
            time.sleep(0.01)

    for i in range(110, 60, -1):
        kit.servo[11].angle = i
        time.sleep(0.01)
    for i in range(90, 140):
        kit.servo[12].angle = i
        time.sleep(0.01)

    time.sleep(1)

    kit.servo[10].angle = 70
    time.sleep(0.01)
    kit.servo[12].angle = 110
    time.sleep(0.1)
    kit.servo[6].angle = 120
    time.sleep(0.01)
    kit.servo[8].angle = 60
    time.sleep(0.01)
    kit.servo[10].angle = 50
    time.sleep(0.01)
    kit.servo[12].angle = 140

    time.sleep(1)

    for i in range(50, 180):
        kit.servo[10].angle = i
        time.sleep(0.01)
    for j in range(3):
        for i in range (120, 90, -1):
            kit.servo[6].angle = i
            time.sleep(0.01)
        for i in range(90, 120):
            kit.servo[6].angle = i
            time.sleep(0.01)
    for i in range(180, 150, -1):
        kit.servo[10].angle = i
        time.sleep(0.01)
    for i in range(140, 40, -1):
        kit.servo[12].angle = i
        time.sleep(0.01)
    for i in range(40, 140):
        kit.servo[12].angle = i
        time.sleep(0.01)
    for i in range(150, 50, -1):
        kit.servo[10].angle = i
        time.sleep(0.01)
        
    time.sleep(1)

    kit.servo[10].angle = 70
    time.sleep(0.01)
    kit.servo[12].angle = 110
    time.sleep(0.1)
    kit.servo[6].angle = 90
    time.sleep(0.01)
    kit.servo[8].angle = 90
    time.sleep(0.01)
    kit.servo[10].angle = 50
    time.sleep(0.01)
    kit.servo[12].angle = 140

    time.sleep(1)

    kit.servo[14].angle = 80
    kit.servo[15].angle = 120
    os.system("/home/pi/RPi_Cam_Web_Interface/start.sh")
    time.sleep(8)
    os.system("/home/pi/RPi_Cam_Web_Interface/stop.sh")
    time.sleep(2)
    for i in range(120, 80, -1):
        kit.servo[15].angle = i
        time.sleep(0.01)
    for i in range(80, 140):
        kit.servo[14].angle = i
        time.sleep(0.01)



def show_off():
    for i in range(3):
       walk_forward(0.01)
    
    time.sleep(3)
    
    for i in range(3):
        walk_backward(0.01)
    
    time.sleep(3)
    
    for i in range(2):
        turn_left(0.01)
        time.sleep(0.1)
    
    time.sleep(3)
    
    for i in range(2):
        turn_right(0.01)
        time.sleep(0.1)
    
    time.sleep(1)

    tail_movement()
    time.sleep(2)
    dance()

#move_angle()
#tail_movement()
#dance()














