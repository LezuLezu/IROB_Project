from evdev import InputDevice, categorize, ecodes

print("Nintendo Swtich Pro controller map")

#creates object 'gamepad' to store the data
gamepad = InputDevice('/dev/input/event0')

#button code variables (switch pro controoller)
aBtn = 305
bBtn = 304
yBtn = 306
xBtn = 307

plsBtn = 313       # plus button
mnBtn = 312         # minus button
scnBtn = 317        # screenshot button
hmBtn = 316        # home button

zlBtn = 310
lBtn = 308
zrBtn = 311
rBtn = 309

#loop and filter by event code and print the mapped label
for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY:
        if event.value == 1:
            if event.code == aBtn:
                print("A")
            elif event.code == bBtn:
                print("B")
            elif event.code == yBtn:
                print("Y")
            elif event.code == xBtn:
                print("X")
            elif event.code == plsBtn:  
                print("+")
            elif event.code == mnBtn:
                print("-")
            elif event.code == scnBtn:
                print("screenshot")
            elif event.code == hmBtn:
                print("home")
            elif event.code == zlBtn:
                print("ZL")
            elif event.code == lBtn:
                print("L")
            elif event.code == zrBtn:
                print("ZR")
            elif event.code == rBtn: 
                print("R")

