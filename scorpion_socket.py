import socket
import time
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = ""
PORT = 5555


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
print("\n")

time.sleep(1)


print("ScorPiion servo arrangement diagram")
print("\n")
print("         15")
print("          |")
print("         14")
print("        | |")
print("   13--9   7--11")
print("      |     |")
print("      |     |")
print("   10--6   8--12")
print("        .^.")
print("\n")
time.sleep(1)

print("[alert] Please turn on the scoPIOn to establish connection")
print("[notice] Waiting to establish connection..[on_hold]")

s.bind((HOST, PORT))
s.listen(1)
conn, address = s.accept()
print("[status] Connected to ScorPIon [OK]\n")

commands = ["Q", "RT", "F", "SF", "FF", "B", "SB", "FB", "R", "SR", "FR", "L", "SL", "FL", "C", "X", "T", "S", "U", "M", "D", "CC"]

while True:
	print("                             =======ACTIVE FUNCTIONS========\n")
	print("[F][SF][FF] Walk forward -> SF for less steps and FF for more steps (default set to normal)")
	print("[B][SB][FB] Walk backward -> SB for less steps and FB for more steps (default set to normal)")
	print("[R][SR][FR]Turn Right -> SR for less steps and FR for more steps (default set to normal)")
	print("[L][SL][FL] Turn Left -> SL for less steps and FL for more steps (default set to normal)")
	print("[C] Camera On")
	print("[X] Camera Off")
	print("[T] Flick tail")
	print("[RT] Reset tail to resting position")
	print("[S] Show-Off")
	print("[U] Camera set to high position")
	print("[M] Camera set to mid position")
	print("[D] Camera set to low position")
	print("[CC] Custom Camera control")
	print("[Q] QUIT")
	print("\n")
	command = input("[alert] Please enter a command from the above menu to control scorPIon\n")
	command = command.upper()

	base = ""
	tail = ""

	if command in commands:
		if command == "CC":
			BT = input("[alert] Enter angle for base tail movement between 0 - 140 (140-forward and 0-backward)\n")
			TT = input ("[alert] Enter angle for tail tip movement between 50 - 170 (50-forward and 170-backward)\n")
			try:
				BT = int(BT)
				TT = int(TT)
				if (0 <= BT <= 140):
					base = "BT"+str(BT)
				else:
					print("[warning] Tail Base angle should be between 0-140")
				if (50 <= TT <= 170):
					tail = "TT"+str(TT)
				else:
					print("[warning] Tail Tip angle should be between 50-170")
				command = base+","+tail
				if len(command) < 8:
					command = ""
			except:
				print("[warning] Not a valid input")

		msg = command.encode()
		conn.send(msg)
		if command == "Q":
			break

print("\n")
conn.close()
print("[notice] Adios Amigo, Hasta La vista, Goodbye, 再见, Ciao, Das Vidanya")
time.sleep(1)
print("[notice] Killing all processes..")
time.sleep(2)
print("[notice] Shutting down scorPion")
for i in range(15, 0, -1):
	print(f"[alert]Shutting Down progress [{i}]")
	time.sleep(1)
print("[alert] Please switch off scorPi")

	
