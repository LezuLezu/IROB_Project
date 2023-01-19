import serial
import time

arduino = serial.Serial('COM3', 115200, timeout=.1)

with arduino:
    time.sleep(0.1)
    if arduino.isOpen():
        print("{} connected".format(arduino.port))
        try:
            while True:
                cmd = input("Enter input to send to Arduino: ")
                cmd = cmd + "\n\r"
                arduino.write(cmd.encode())
                while arduino.inWaiting() == 0: pass
                if arduino.inWaiting() > 0:
                    received = arduino.readline()
                    print(received.decode())
                    arduino.flushInput()
        except KeyboardInterrupt:
            print("KeyboardInterrupt")
    
