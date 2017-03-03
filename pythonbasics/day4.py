#!/usr/bin/python2.7

import serial, io
from datetime import datetime

#ser = serial.Serial(
#    port='/dev/ttyUSB0',
#    baudrate=9600,
#)

#while ser.isOpen():
#    datastring = ser.read(size=8)
#    print datetime.utcnow().isoformat(), datastring

#ser.close()


outfile='/tmp/serial-temperature.tsv'

ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=9600,
)

sio = io.TextIOWrapper(
    io.BufferedRWPair(ser, ser, 1),
    encoding='ascii', newline='\r'
)

with open(outfile, 'a') as f:
    while ser.isOpen():
        datastring = sio.readline()
        f.write(datetime.utcnow().isoformat() + '\t' + datastring + '\n')
        f.flush()

ser.close()
