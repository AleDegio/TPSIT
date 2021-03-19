import RPi.GPIO as GPIO
import time
from AlphaBot import AlphaBot

DR = 16
DL = 19

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(DR,GPIO.IN,GPIO.PUD_UP)
GPIO.setup(DL,GPIO.IN,GPIO.PUD_UP)

def gestioneOstacoli(comando, valore, Ab):

	 comandi = {"forward": "alphaBot.forward()", "backward": "alphaBot.backward()",
     "left": "alphaBot.setMotor(50, 0)", "right": "alphaBot.setMotor(0, 50)"}
	finito = True

	try:
		while finito:
			DR_status = GPIO.input(DR)
			DL_status = GPIO.input(DL)
			if((DL_status == 1) and (DR_status == 1)):
				if(comando is not "left" and comando is not "right"):
					eval(comandi[comando]) #evita di fare le if annidate 
				else:
					eval(comandi[comando])
					alphaBot.forward()

				print("L'aphabot si sta muovendo per: " + str(tempo_attesa) + " secondi (attendo)")
				#attendo lo spostamento
				time.sleep(tempo_attesa)
				#interrompo lo spostamento
				alphaBot.stop()
				finito = False
			elif((DL_status == 1) and (DR_status == 0)):
				Ab.left()
				print("left")
			elif((DL_status == 0) and (DR_status == 1)):
				Ab.right()
				print("right")
			else:
				Ab.backward()
				time.sleep(0.2)
				Ab.left()
				time.sleep(0.2)
				Ab.stop()
				print("backward")

	except KeyboardInterrupt:
		GPIO.cleanup()