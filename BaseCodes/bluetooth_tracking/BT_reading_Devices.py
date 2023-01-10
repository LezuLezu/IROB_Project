# Find BLE (low energy) devices using bluepy

from bluepy.btle import Scanner
 
scanner = Scanner()
devices = scanner.scan(10.0)
 
for device in devices:
    devRssi = device.rssi
    devMac = device.addr
    devDes = device.addrType
    distance = 10 ** ((-69 - (device.rssi)) / (10*2))
    connectionAvail = device.connectable

    #
    # print("DEV = {} RSSI = {}".format(device.addr, device.rssi))
    print("device type : %s ; MAC : %s ; RRSI : %s ; distance : %s ; connectable : %s" %(devDes, devMac, devRssi, distance, connectionAvail))