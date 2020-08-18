import cv2
from grabscreen import grab_screen
from getkeys import key_check
from alexnet import alexnet
from directkeys import PressKey, ReleaseKey, W, A, S, D
import numpy as np
import time
from os import system

WIDTH = 100
HEIGHT = 80
LR = 1e-3
EPOCHS = 8
MODEL_NAME = 'F12019-Mercedes-{}-{}-{}-{}-epochs.model'.format("Britain", LR, 'alexnetv2',EPOCHS)
ROI = (5, 150, 1015, 510)

W_Condition = [1, 0, 0, 0, 0, 0, 0, 0, 0]
A_Condition = [0, 1, 0, 0, 0, 0, 0, 0, 0]
S_Condition = [0, 0, 1, 0, 0, 0, 0, 0, 0]
D_Condition = [0, 0, 0, 1, 0, 0, 0, 0, 0]
WA_Condition = [0, 0, 0, 0, 1, 0, 0, 0, 0]
WD_Condition = [0, 0, 0, 0, 0, 1, 0, 0, 0]
SA_Condition = [0, 0, 0, 0, 0, 0, 1, 0, 0]
SD_Condition = [0, 0, 0, 0, 0, 0, 0, 1, 0]
NK_Condition = [0, 0, 0, 0, 0, 0, 0, 0, 1]

def ReleaseAllKeys():
	ReleaseKey(W)
	ReleaseKey(A)
	ReleaseKey(D)
	ReleaseKey(S)

def PressOneKey(key):
	if key == "W":
		PressKey(W)
		ReleaseKey(A)
		ReleaseKey(S)
		ReleaseKey(D)
	elif key == "A":
		PressKey(A)
		ReleaseKey(W)
		ReleaseKey(S)
		ReleaseKey(D)
	elif key == "S":
		PressKey(S)
		ReleaseKey(W)
		ReleaseKey(A)
		ReleaseKey(D)
	elif key == "D":
		PressKey(D)
		ReleaseKey(W)
		ReleaseKey(A)
		ReleaseKey(S)

def PressTwoKey(key):
	if key == "WA":
		PressKey(W)
		PressKey(A)
		ReleaseKey(S)
		ReleaseKey(D)
	elif key == "WD":
		PressKey(W)
		PressKey(D)
		ReleaseKey(A)
		ReleaseKey(S)
	elif key == "SA":
		PressKey(S)
		PressKey(A)
		ReleaseKey(W)
		ReleaseKey(D)
	elif key == "SD":
		PressKey(S)
		PressKey(D)
		ReleaseKey(W)
		ReleaseKey(A)

def main():
	model = alexnet(WIDTH, HEIGHT, LR)
	model.load(MODEL_NAME)
	system("cls")
	print("\t\t\t+-------------STARTED---------------+-----------------+")
	print("\t\t\t|   Q : QUIT     |    P : PAUSED    |    M : CLRSCR   |")
	print("\t\t\t+--------------- + -----------------+-----------------|\n\n")

	for i in list(range(7))[::-1]:
		print(i+1)
		time.sleep(1)

	run, paused = True, False
	while run:
		if not paused: 
			screen = grab_screen(ROI)
			screen = cv2.resize(screen, (WIDTH, HEIGHT))
			screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)

			prediction = model.predict([screen.reshape(WIDTH, HEIGHT, 1)])[0]
			action = list(np.around(prediction))
			print(action," : ", prediction, "\n")

			if action == W_Condition:
				PressOneKey("W")
				# print("W")
			elif action == A_Condition:
				PressOneKey("A")
				# print("A")
			elif action == S_Condition:
				PressOneKey("S")
				# print("S")
			elif action == D_Condition:
				PressOneKey("D")
				# print("D")

			elif action == WA_Condition:
				PressTwoKey("WA")
				# print("WA")
			elif action == WD_Condition:
				PressTwoKey("WD")
				# print("WD")
			elif action == SA_Condition:
				PressTwoKey("SA")
				# print("SA")
			elif action == SD_Condition:
				PressTwoKey("SD")
				# print("SD")
			elif action == NK_Condition:
				ReleaseAllKeys()
				# print("NK")

		Key = key_check()
		if "P" in Key:
			if paused: 
				print("Un-Pausing in...")
				ReleaseAllKeys()
				for j in list(range(5))[::-1]:
					print(j+1)
					time.sleep(1)
				paused = False
			else:
				print("Paused.")
				paused = True
				ReleaseAllKeys()
				time.sleep(1)
		if "M" in Key:
			system("cls")
		if "Q" in Key:
			print("Quiting...")
			ReleaseAllKeys()
			paused, run = True, False
			break


if __name__ == "__main__":
	main()
