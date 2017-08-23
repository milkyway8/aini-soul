import serial
import time
arduino = serial.Serial('/dev/ttyACM0',9600)
#time.sleep(1.5)

comando='H'
if comando:
	arduino.write(comando)

arduino.close()#FINALIZA LA COMUNICACION
