#!/usr/bin/env python

'''
Created on Dec 29, 2014

@author: frans
'''
import td
import time
import sys

def myRawDeviceEvent(data, controllerId, callbackId):
    evaluate(data)
    print '%d: RawDeviceEvent: %s' %(time.time(), data)
    print '  controllerId: ', controllerId
    
    fh = open("/tmp/remote.txt","a")
    fh.writelines(data)
    fh.close()
#16080458

def evaluate(data):
    on = None
    off = None
    button = None

    for i in range(1,5):
        commandstring = 'class:command;protocol:arctech;model:selflearning;house:16080458;unit:'+str(i)+';group:0;method:'
#14660198
        print commandstring
        if commandstring in data:
            button = i
            if 'method:turnon' in data:
                on = True
            elif 'method:turnoff' in data:
                off = True
            fh = open("/tmp/remote.txt","a")
            fh.writelines(commandstring)
            fh.close()

    if on and button == 1:
        time.sleep(0.5)
        td.turnOn(1)
        td.turnOn(2)
        td.turnOn(3)
        td.turnOn(4)
        td.turnOn(5)
        #td.turnOn(6)
    elif off and button == 1:
        time.sleep(0.5)
        td.turnOff(1)
        td.turnOff(2)
        td.turnOff(3)
        td.turnOff(4)
        td.turnOff(5)
        #td.turnOff(6)
    elif on and button == 2:
        time.sleep(0.5)
        td.turnOn(1)
        #td.turnOn(4)
    elif off and button == 2:
        time.sleep(0.5)
        td.turnOff(1)
        #td.turnOff(4)
    elif on and button == 3:
        time.sleep(0.5)
        td.turnOn(3)
        #td.turnOn(5)
    elif off and button == 3:
        time.sleep(0.5)
        td.turnOff(3)
        #td.turnOff(5)
    elif on and button == 4:
        time.sleep(0.5)
        td.turnOn(6)
    elif off and button == 4:
        time.sleep(0.5)
        td.turnOff(6)

def run():

    fh = open("/tmp/remote.txt","a")
    fh.write("Testing")
    fh.close()

    td.init( defaultMethods = td.TELLSTICK_TURNON | td.TELLSTICK_TURNOFF )
    
    cbId = []
    cbId.append(td.registerRawDeviceEvent(myRawDeviceEvent))
    print 'Register raw device event returned:', cbId[-1]
    
    try:
        while(1):
            time.sleep(1)
    except KeyboardInterrupt:
        print 'KeyboardInterrupt received, exiting'
        for i in cbId:
            td.unregisterCallback(i)
            
    td.close()




if __name__ == '__main__':    
    run()
