"""
Trova i picchi nella derivata del video.
@ 2021, Francesco Roberto Dani

Utilizzo:

python3 path/to/this/script.py path/to/video.mp4 threshold=0.05
"""

"""
TODO:
3) Aggiungere modalità R, G, B, BW
"""

import os
import sys
import cv2
import numpy as np
from datetime import datetime
from scipy.signal import find_peaks
from matplotlib import pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', help="Input video file path (required)", type= str)
parser.add_argument('-o', help="Output txt file path (required)", type= str, default="./out.txt")
parser.add_argument('-r', help="Rect specifying portion of image to be processed [x1, y1, x2, y2]", nargs="+", type= int, default=[0, 0, -1, -1])
parser.add_argument('-f', help="Start:End frames to process [sf, ef]", nargs="+", type= int, default=[0, -1])
parser.add_argument('-t', help="Threshold for peaks", type= float, default=0.05)

args=parser.parse_args()

FILE_PATH = args.i
OUT_FILE_NAME = args.o
RECT = args.r
FRAMES = args.f
PEAK_HEIGHT = args.t



print("ARGS:")
print(args)

"""
if len(sys.argv) == 2:
	FILE_PATH = sys.argv[1]
	PEAK_HEIGHT = 0.05

if len(sys.argv) == 3:
	FILE_PATH = sys.argv[1]
	PEAK_HEIGHT = float(sys.argv[2])
"""

cap = cv2.VideoCapture(FILE_PATH)
frameCount = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
frameWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frameHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
frameRate = int(cap.get(cv2.CAP_PROP_FPS))

if RECT[2] == -1:
	RECT[2] = frameWidth
if RECT[3] == -1:
	RECT[3] = frameHeight

if FRAMES[1] == -1:
	FRAMES[1] = frameCount
#frameCount = FRAMES[1] - FRAMES[0]

newWidth = 320
newHeight = 240
buf = np.zeros((frameCount, newHeight, newWidth)) # add ", 3" to shape for RGB.
fc = 0
ret = True
print("Reading Video...")
while (fc < frameCount  and ret):
	ret, frame = cap.read()
	if (fc >= FRAMES[0]) and (fc <= FRAMES[1]):
		frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)[RECT[1]:RECT[3], RECT[0]:RECT[2]]
		frame = cv2.resize(frame, (newWidth, newHeight))
		buf[fc] = frame
	fc += 1
cap.release()
print("Processing Difference...")
diff = np.zeros((frameCount-1))
for i in range(frameCount-1):
	diff[i] = (np.sum(buf[i+1]) - np.sum(buf[i])) / (newWidth * newHeight * 255)
print("Difference Processed.   Dims:", diff.shape)
peaks = find_peaks(np.abs(diff), height=PEAK_HEIGHT)[0]
peak_times = np.divide(peaks, frameRate)
with open(os.path.dirname(FILE_PATH) + "/" + OUT_FILE_NAME, "w") as file:
	for peak_t in peak_times:
		print("Peak at:", peak_t, "s")
		file.write(str(peak_t) + "\n")
	file.close;
	print("File saved:", os.path.dirname(FILE_PATH) + OUT_FILE_NAME)

print("Plotting Difference and Peaks...")
plt.plot(diff)
plt.plot(peaks, diff[peaks], 'o', color='red')
plt.show()
print("Done.")












