import serial

arduino = serial.Serial('/dev/ttyACM0',9600)

print("comenzamos!")

while True:
	comando = raw_input('Introduce un comando: ')
	arduino.write(comando)
	if comando == 'h':
		print('LED ENCENDIDO')
		arduino.close()#FINALIZA LA COMUNICACION
	elif comando == 'l':
		print('LED APAGADO')
		arduino.close()#FINALIZA LA COMUNICACION


