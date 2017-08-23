import Serial
import sys
import os

arduino = serial.Serial('/dev/ttyACM0',9600)
celular = sys.argv[1]

arduino.write(celular)

arduino.close()