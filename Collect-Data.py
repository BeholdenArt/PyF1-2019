import cv2
from grabscreen import grab_screen
from getkeys import key_check
import numpy as np
import os
import time

# Controls
W = [1, 0, 0, 0, 0, 0, 0, 0, 0]
A = [0, 1, 0, 0, 0, 0, 0, 0, 0]
S = [0, 0, 1, 0, 0, 0, 0, 0, 0]
D = [0, 0, 0, 1, 0, 0, 0, 0, 0]
WA = [0, 0, 0, 0, 1, 0, 0, 0, 0]
WD = [0, 0, 0, 0, 0, 1, 0, 0, 0]
SA = [0, 0, 0, 0, 0, 0, 1, 0, 0]
SD = [0, 0, 0, 0, 0, 0, 0, 1, 0]
NK = [0, 0, 0, 0, 0, 0, 0, 0, 1]
ROI = (5, 150, 1015, 510)    # Region of interest
WIDTH, HEIGHT = 100, 80


def CheckDataExistance(filename):
	if os.path.isfile(file_name):
	        training_data = list(np.load(file_name, allow_pickle= True))
	        print("Previous Data loaded!")
	else:
	        print("Starting fresh")
	        training_data = []

	return training_data      

def CheckKey(PressedKeys):
	output = [0, 0, 0, 0, 0, 0, 0, 0, 0]	# [W, A, S, D, WA, WD, SA, SD, NK]

	if "W" in PressedKeys and "A" in PressedKeys:
		output = WA
	elif "W" in PressedKeys and "D" in PressedKeys:
		output = WD
	elif "S" in PressedKeys and "A" in PressedKeys:
		output = SA
	elif "S" in PressedKeys and "D" in PressedKeys:
		output = SD
	elif "W" in PressedKeys:
		output = W
	elif "A" in PressedKeys:
		output = A
	elif "S" in PressedKeys:
		output = S
	elif "D" in PressedKeys:
		output = D
	else:
		output = NK

	return output


def main():
	file_name = "Training-Data.npy"
	TrainingData = CheckDataExistance(file_name)

	for i in list(range(3))[::-1]:
		print(i+1)
		time.sleep(1)

	print("Started", "\n", "P : Quit")

	run = True
	while run:
		screen = grab_screen(ROI)
		screen = cv2.resize(screen, (WIDTH, HEIGHT))
		screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
		
		PressedKey = key_check()
		if "P" in PressedKey:
			run = False
		else:
			action = CheckKey(PressedKey)
		TrainingData.append([screen, action])

		if len(TrainingData) % 1000 == 0:
			print("Completed : ", len(TrainingData))
			np.save(file_name, TrainingData)


if __name__ == "__main__":
	main()
