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


#outfile='/tmp/serial-temperature.tsv'

#ser = serial.Serial(
#    port='/dev/ttyUSB0',
#    baudrate=9600,
#)

#sio = io.TextIOWrapper(
#    io.BufferedRWPair(ser, ser, 1),
#    encoding='ascii', newline='\r'
#)

#with open(outfile, 'a') as f:
#    while ser.isOpen():
#        datastring = sio.readline()
#        f.write(datetime.utcnow().isoformat() + '\t' + datastring + '\n')
#        f.flush()

#ser.close()


from csv import reader
infile='/tmp/serial-temperature.tsv'
outfile='sensor-data.nc'

def convert_time(tm):
    tm =  datetime.strptime(tm, "%Y-%m-%dT%H:%M:%S.%f")
    return tm
def  convert_temp(temp):
    value = temp.strip("+").strip("C").lstrip("0")
    return float(value) + 273.15

times = []
temps = []

with open(infile, 'rb') as tsvfile:
    tsvreader = reader(tsvfile, delimiter='\t')
    for row in tsvreader:
        times.append(convert_time(row[0]))
        temps.append(convert_temp(row[1]))

