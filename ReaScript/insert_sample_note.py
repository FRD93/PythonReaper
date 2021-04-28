"""
Utility function to easily insert MediaItem with specified params.

Copyright 2021, Francesco Roberto Dani
www.francesco-dani.com
f.r.d@hotmail.it
"""

import os
import sys


MEDIA_FILE_PATH = "/Users/admin/Documents/Samples/SoundLibrary/Instruments/House/bass/bass_30/36.wav"

"""
# Insert new media
media = RPR_InsertMedia(MEDIA_FILE_PATH, 1) # 1=add new track
# Select last inserted media from index returned from RPR_InsertMedia()
#media = RPR_GetMediaItem(0, media) # *** this doesn't work properly :(
media = RPR_GetMediaItem(0, RPR_CountMediaItems(0) - 1) # *** instead, this works! :)
# Change media item duration
RPR_SetMediaItemInfo_Value(media, 'D_LENGTH', 0.5)
# Change media item fade-out length
RPR_SetMediaItemInfo_Value(media, 'D_FADEOUTLEN', 0.5)
"""

# INSERT A SAMPLE WITH PARAMETERS
# USAGE:
# insertMediaItemWithParams(MEDIA_FILE_PATH, 0.5, 1, [['D_LENGTH', 0.5], ['D_FADEOUTLEN', 0.25], ['D_FADEINLEN', 0.24]])

def insertMediaItemWithParams(path, start_time, INSERTION_MODE=1, args=[['D_LENGTH', 0.5], ['D_FADEOUTLEN', 0.25]]):
	RPR_SetEditCurPos(start_time, True, True)
	RPR_InsertMedia(path, INSERTION_MODE) # 1=add new track
	media = RPR_GetMediaItem(0, RPR_CountMediaItems(0) - 1) # *** instead, this works! :)
	for arg in args:
		RPR_SetMediaItemInfo_Value(media, arg[0], arg[1])




instr_samples_dir = "/Users/admin/Documents/Samples/SoundLibrary/Instruments/House/bass/bass_30/"
notes = [
	[0.0, "36", 0.5, 0.8, 0.05, 0.25], # [start_time, note, duration, amplitude, fade_in_t, fade_out_t]
	[0.5, "36", 0.5, 0.8, 0.05, 0.25],
	[1.0, "43", 1.0, 0.8, 0.05, 0.50],
	[2.0, "36", 2.0, 0.8, 0.05, 0.50]
]

for index, note in enumerate(notes):
	path = instr_samples_dir + note[1] + ".wav"
	RPR_ShowConsoleMsg("" + path + "\n")
	if index == 0:
		insertMediaItemWithParams(path, note[0], 1, [["D_LENGTH", note[2]], ["D_VOL", note[3]], ["D_FADEINLEN", note[4]], ["D_FADEOUTLEN", note[5]]])
	else:
		insertMediaItemWithParams(path, note[0], 0, [["D_LENGTH", note[2]], ["D_VOL", note[3]], ["D_FADEINLEN", note[4]], ["D_FADEOUTLEN", note[5]]])












