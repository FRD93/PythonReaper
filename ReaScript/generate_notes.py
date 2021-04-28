"""
Utility function to create random notes and save them to file.

Notes are formatted as: [start_time, midi_note, duration, fade_out_time]

Copyright 2021, Francesco Roberto Dani
www.francesco-dani.com
f.r.d@hotmail.it
"""

import random
import math
import os

# Number of notes
N = 20

# Possible notes (MIDI)
POSSIBLE_NOTES = [36, 41, 43, 45, 48, 53, 55, 57, 60]

# Start time of sequence (s)
START_TIME = 12.0

# End time of sequence (s)
END_TIME = 24.0

# Step of sequence (s)
STEP = 0.125

# Fade out time (s)
FADE_OUT_TIME = 0.125

# Output file path
OUT_FILE = "/Users/admin/Documents/BackupGoogleDrive/PythonReaper/preposizioni/prep_3.txt"

def generateRandomNotes(N, POSSIBLE_NOTES, START_TIME, END_TIME, STEP, OUT_FILE):
	start_times = list(sorted([math.floor(random.uniform(START_TIME, END_TIME) / STEP) * STEP for x in range(N)]))
	start_times = list(dict.fromkeys(start_times))
	durations = [start_times[min(index + 1, len(start_times) - 1)] - time for index, time in enumerate(start_times)]
	durations[-1] = max(STEP, END_TIME - start_times[-1])
	fadeout_times = [FADE_OUT_TIME for i in range(len(start_times))]
	midi_notes = [random.choice(POSSIBLE_NOTES) for x in range(len(start_times))]
	with open(OUT_FILE, "a") as file:
		for index, time in enumerate(start_times):
			file.write("[" + str(time) + ", " + str(midi_notes[index]) + ", " + str(durations[index]) + ", " + str(fadeout_times[index]) + "],\n")
		file.close()

# Test
def genBass():
	try:
		os.remove("/Users/admin/Documents/BackupGoogleDrive/PythonReaper/preposizioni/bass.txt")
	except:
		pass
	N = 20
	POSSIBLE_NOTES = [36, 41, 43, 48]
	START_TIME = 0.0
	END_TIME = 12.0
	STEP = 0.125
	OUT_FILE = "/Users/admin/Documents/BackupGoogleDrive/PythonReaper/preposizioni/bass.txt"
	generateRandomNotes(N, POSSIBLE_NOTES, START_TIME, END_TIME, STEP, OUT_FILE)
	POSSIBLE_NOTES = [43, 48, 50, 55]
	START_TIME = 12
	END_TIME = 24
	generateRandomNotes(N, POSSIBLE_NOTES, START_TIME, END_TIME, STEP, OUT_FILE)
	POSSIBLE_NOTES = [36, 41, 43, 48]
	START_TIME = 24
	END_TIME = 36
	generateRandomNotes(N, POSSIBLE_NOTES, START_TIME, END_TIME, STEP, OUT_FILE)



def genLead():
	try:
		os.remove("/Users/admin/Documents/BackupGoogleDrive/PythonReaper/preposizioni/lead.txt")
	except:
		pass
	N = 12
	POSSIBLE_NOTES = [36, 41, 43, 45, 48, 53, 55, 57, 62]
	START_TIME = 0.0
	END_TIME = 12.0
	STEP = 2
	OUT_FILE = "/Users/admin/Documents/BackupGoogleDrive/PythonReaper/preposizioni/lead.txt"
	generateRandomNotes(N, POSSIBLE_NOTES, START_TIME, END_TIME, STEP, OUT_FILE)
	POSSIBLE_NOTES = [43, 48, 50, 52, 55, 60, 62, 64, 67, 72]
	START_TIME = 12
	END_TIME = 24
	generateRandomNotes(N, POSSIBLE_NOTES, START_TIME, END_TIME, STEP, OUT_FILE)
	POSSIBLE_NOTES = [36, 41, 43, 45, 48, 53, 55, 57, 62]
	START_TIME = 24
	END_TIME = 36
	generateRandomNotes(N, POSSIBLE_NOTES, START_TIME, END_TIME, STEP, OUT_FILE)


def genKey():
	try:
		os.remove("/Users/admin/Documents/BackupGoogleDrive/PythonReaper/preposizioni/key.txt")
	except:
		pass
	N = 12
	POSSIBLE_NOTES = [36, 41, 43, 45, 48, 53, 55, 57, 62]
	START_TIME = 0.0
	END_TIME = 12.0
	STEP = 2
	OUT_FILE = "/Users/admin/Documents/BackupGoogleDrive/PythonReaper/preposizioni/key.txt"
	generateRandomNotes(N, POSSIBLE_NOTES, START_TIME, END_TIME, STEP, OUT_FILE)
	POSSIBLE_NOTES = [43, 48, 50, 52, 55, 60, 62, 64, 67, 72]
	START_TIME = 12
	END_TIME = 24
	generateRandomNotes(N, POSSIBLE_NOTES, START_TIME, END_TIME, STEP, OUT_FILE)
	POSSIBLE_NOTES = [36, 41, 43, 45, 48, 53, 55, 57, 62]
	START_TIME = 24
	END_TIME = 36
	generateRandomNotes(N, POSSIBLE_NOTES, START_TIME, END_TIME, STEP, OUT_FILE)

def genSampler():
	try:
		os.remove("/Users/admin/Documents/BackupGoogleDrive/PythonReaper/preposizioni/sampler.txt")
	except:
		pass
	N = 23
	POSSIBLE_NOTES = [48, 55, 57, 62]
	START_TIME = 0.0
	END_TIME = 12.0
	STEP = 0.25
	OUT_FILE = "/Users/admin/Documents/BackupGoogleDrive/PythonReaper/preposizioni/sampler.txt"
	generateRandomNotes(N, POSSIBLE_NOTES, START_TIME, END_TIME, STEP, OUT_FILE)
	POSSIBLE_NOTES = [55, 64, 67, 72]
	START_TIME = 12
	END_TIME = 24
	generateRandomNotes(N, POSSIBLE_NOTES, START_TIME, END_TIME, STEP, OUT_FILE)
	POSSIBLE_NOTES = [48, 53, 55, 62]
	START_TIME = 24
	END_TIME = 36
	generateRandomNotes(N, POSSIBLE_NOTES, START_TIME, END_TIME, STEP, OUT_FILE)

genBass()
genLead()
genKey()
genSampler()
