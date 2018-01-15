from pyuipc import *
import sys
import os
import time
import math
import base64

# Connect To Simulator
def simConnect(simversion):
    ''' Sim Versions by Number
    SIM_ANY = 0
    SIM_FS98 = 1
    SIM_FS2K = 2
    SIM_CFS2 = 3
    SIM_CFS1 = 4
    SIM_FLY = 5
    SIM_FS2K2 = 6
    SIM_FS2K4 = 7
    SIM_FSX = 8
    SIM_ESP = 9
    '''
    try:
        open(0)
        print "Conected"
    except FSUIPCException:
        print "Couldn't Connect"
#


# Prepare Data 
def prepareWrite(offhex,datasize):
    '''
  - b: a 1-byte unsigned value, to be converted into a Python int
  - c: a 1-byte signed value, to be converted into a Python int
  - h: a 2-byte signed value, to be converted into a Python int
  - H: a 2-byte unsigned value, to be converted into a Python int
  - d: a 4-byte signed value, to be converted into a Python int
  - u: a 4-byte unsigned value, to be converted into a Python long
  - l: an 8-byte signed value, to be converted into a Python long
  - L: an 8-byte unsigned value, to be converted into a Python long
  - f: an 8-byte floating point value, to be converted into a Python double
   '''
    global Data
    OffsetHex = offhex
    offset = [(OffsetHex, datasize), (OffsetHex, datasize)]
    Data = prepare_data(offset, True)
    return Data
#


# Write Data Function
def writeData(Data, value, value2):
    ''' Write Usage example)
    1. First Prepare Data With OffsetHex and DataSize value
    2. Write data With variable used from PrepareWrite and then Value you want to Write
    '''
    write(Data, [value,value2])
#

# Read Data from Simulator
def readData(offSetHex, DataSize):
    
    '''
    # data size 
     - b: a 1-byte unsigned value, to be converted into a Python int
      - c: a 1-byte signed value, to be converted into a Python int
      - h: a 2-byte signed value, to be converted into a Python int
      - H: a 2-byte unsigned value, to be converted into a Python int
      - d: a 4-byte signed value, to be converted into a Python int
      - u: a 4-byte unsigned value, to be converted into a Python long
      - l: an 8-byte signed value, to be converted into a Python long
      - L: an 8-byte unsigned value, to be converted into a Python long
      - f: an 8-byte floating point value, to be converted into a Python double
      '''
    global DataRead
    DataRead = read([(offSetHex, DataSize),])
    return DataRead
#

# Example Reading Data 
'''
simConnect(0)
zuluHour = readData(0x023B, "b")
print ZuluHour

'''


# Example Writing Data
 '''
simConnect(0)
a = prepareWrite(0x0251, 'b')
writeData(a, 100,100)
'''    


