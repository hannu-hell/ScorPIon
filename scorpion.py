from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
import time
import os

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
    #kit.servo[14].angle = 140
    #kit.servo[15].angle = 90

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
    #kit.servo[14].angle = 140
    #kit.servo[15].angle = 90

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


def turn_left(t):
    #kit.servo[14].angle = 140
    #kit.servo[15].angle = 90

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


def turn_right(t):
    #kit.servo[14].angle = 140
    #kit.servo[15].angle = 90

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

#------------------------------------------------------------------------------------------
#*************************  BLUETOOTH *****************************************************

import bluetooth

server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

port = 1
server_sock.bind(("",port))
server_sock.listen(1)

client_sock, address = server_sock.accept()
print("Accepted Connection from ", address)

while True:
    recvdata = client_sock.recv(1024)
    print("Received {} through Bluetooth".format(recvdata))
    if (recvdata == b'Q'):
        print("Exiting")
        break
    if (recvdata == b'f'):
        for i in range(2):
            walk_forward(0.01)
            time.sleep(0.1)
    if (recvdata == b'b'):
        for i in range(2):
            walk_backward(0.01)
            time.sleep(0.1)
    if (recvdata == b'r'):
        for i in range(2):
            turn_right(0.01)
            time.sleep(0.1)
    if (recvdata == b'l'):
        for i in range(2):
            turn_left(0.01)
            time.sleep(0.1)
    if (recvdata == b's'):
        show_off()
    if (recvdata == b'c'):
        os.system("/home/pi/RPi_Cam_Web_Interface/start.sh")
    if (recvdata == b'x'):
        os.system("/home/pi/RPi_Cam_Web_Interface/stop.sh")
    if (recvdata == b'u'):
        kit.servo[14].angle = 60
        kit.servo[15].angle = 100
    if (recvdata == b'm'):
        kit.servo[14].angle = 80
        kit.servo[15].angle = 80
    if (recvdata == b'd'):
        kit.servo[14].angle = 110
        kit.servo[15].angle = 80

client_sock.close()
server_sock.close()

#------------------------------------------------------------------------------------------
#******************************************************************************************



#------------------------------------------------------------------------------------------
#************************************** WIFI **********************************************


#import socket
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#time.sleep(20)
#
#
#HOST = "192.168.0.104"
#PORT = 5555
#
#s.connect((HOST, PORT))
#
#while True:
#    s_msg = s.recv(1024)
#    s_msg = s_msg.decode()
#    if s_msg == "Q":
#        break
#
#    if s_msg == "F":
#        for i in range(3):
#            walk_forward(0.01)
#    if s_msg == "SF":
#        walk_forward(0.01)
#    if s_msg == "FF":
#        for i in range(5):
#            walk_forward(0.01)
#
#    if s_msg == "B":
#        for i in range(3):
#            walk_backward(0.01)
#    if s_msg == "SB":
#        walk_backward(0.01)
#    if s_msg == "FB":
#        for i in range(5):
#            walk_backward(0.01)
#
#    if s_msg == "R":
#        for i in range(3):
#            turn_right(0.01)
#    if s_msg == "SR":
#        turn_right(0.01)
#    if s_msg == "FR":
#        for i in range(5):
#            turn_right(0.01)
#
#    if s_msg == "L":
#        for i in range(3):
#            turn_left(0.01)
#    if s_msg == "SL":
#        turn_left(0.01)
#    if s_msg == "FL":
#        for i in range(5):
#            turn_left(0.01)
#
#    if s_msg == "C":
#        os.system("/home/pi/RPi_Cam_Web_Interface/start.sh")
#    if s_msg == "X":
#        os.system("/home/pi/RPi_Cam_Web_Interface/stop.sh")
#
#    if s_msg == "T":
#        tail_movement()
#    if s_msg == "S":
#        show_off()
#    if s_msg == "U":
#        kit.servo[14].angle = 10
#        kit.servo[15].angle = 100
#    if s_msg == "M":
#        kit.servo[14].angle = 90
#        kit.servo[15].angle = 90
#    if s_msg == "D":
#        kit.servo[14].angle = 120
#        kit.servo[15].angle = 70
#    if s_msg == "RT":
#        kit.servo[15].angle = 80
#        kit.servo[14].angle = 140
#        
#
#    if len(s_msg) > 2:
#        a = s_msg.split(",")
#        base_angle = int(a[0].strip("BT"))
#        tail_angle = int(a[1].strip("TT"))
#        kit.servo[14].angle = base_angle
#        kit.servo[15].angle = tail_angle
#
#    if s_msg == "Q":
#        break
#
#
#s.close()
#os.system("/home/pi/RPi_Cam_Web_Interface/stop.sh")
#time.sleep(1)
#
#kit.servo[14].angle = 140
#kit.servo[15].angle = 90
#kit.servo[6].angle = 90
#kit.servo[10].angle = 50
#kit.servo[7].angle = 90
#kit.servo[11].angle = 60
#kit.servo[8].angle = 90
#kit.servo[12].angle = 140    
#kit.servo[9].angle = 90
#kit.servo[13].angle = 130
#
#time.sleep(1)
#
#os.system("cd /home/pi")
#os.system("sudo shutdown -h now")
#
