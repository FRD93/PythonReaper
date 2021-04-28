"""
Utility function to easily insert MediaItem with specified params.

Copyright 2021, Francesco Roberto Dani
www.francesco-dani.com
f.r.d@hotmail.it
"""

import os
import sys

notes_path = "/Users/admin/Documents/BackupGoogleDrive/PythonReaper/preposizioni/key.txt"
instr_path = "/Users/admin/Documents/Samples/SoundLibrary/Instruments/Lo-Fi/key/key_101/"


# INSERT A SAMPLE WITH PARAMETERS
# USAGE:
# insertMediaItemWithParams(MEDIA_FILE_PATH, 0.5, 1, [['D_LENGTH', 0.5], ['D_FADEOUTLEN', 0.25], ['D_FADEINLEN', 0.24]])

def insertMediaItemWithParams(path, start_time, INSERTION_MODE=1, args=[['D_LENGTH', 0.5], ['D_FADEOUTLEN', 0.25]]):
	RPR_SetEditCurPos(start_time, True, True)
	RPR_InsertMedia(path, INSERTION_MODE) # 1=add new track
	media = RPR_GetMediaItem(0, RPR_CountMediaItems(0) - 1) # *** instead, this works! :)
	for arg in args:
		RPR_SetMediaItemInfo_Value(media, arg[0], arg[1])


# READ NOTES FILE
# USAGE:
# notes = readNotesFile(PATH)
def readNotesFile(PATH):
	with open(PATH, "r") as file:
		return [eval(line)[0] for line in file.readlines()]


# READ NOTES FILE
# USAGE:
# notes = readNotesFile(PATH)
def insertNotesFile(notes_path, instr_path):
	notes = readNotesFile(notes_path)
	for index, note in enumerate(notes):
		path = instr_path + str(note[1]) + ".wav"
		#RPR_ShowConsoleMsg("" + path + "\n")
		if index == 0:
			insertMediaItemWithParams(path, note[0], 1, [["D_LENGTH", note[2]], ["D_FADEOUTLEN", note[3]]])
		else:
			insertMediaItemWithParams(path, note[0], 0, [["D_LENGTH", note[2]], ["D_FADEOUTLEN", note[3]]])





insertNotesFile(notes_path, instr_path)










