"""
Insert media item at random time stamps, N times.

Copyright 2021, Francesco Roberto Dani
www.francesco-dani.com
f.r.d@hotmail.it

"""

##############################
### CHANGE PARAMETERS HERE ###
##############################

# Path to media item
#MEDIA_FILE_PATH = "/Users/admin/Desktop/LABA - Sound Design - Video Files/Horror_lights_01/audio/Light.wav"
MEDIA_FILE_PATH = "/Users/admin/Documents/Samples/SoundLibrary/Instruments/House/drum/drum_30/52.wav"

# Number of insertions
N = 23

# Start time (s)
START_TIME = 0.0

# End time (s)
END_TIME = 60.0

# Step (s)
STEP = 0.125

# Python: Boolean RPR_SetMediaItemInfo_Value(MediaItem item, String parmname, Float newvalue)

#########################
### END OF PARAMETERS ###
#########################

import os
import sys
import random
times = [round(random.uniform(START_TIME, END_TIME) / STEP) * STEP for i in range(N)]
times = list(dict.fromkeys(times))
for index in range(N):
	time = round(random.uniform(START_TIME, END_TIME) / STEP) * STEP
	RPR_SetEditCurPos(time, True, True)
	if index == 0:
		media = RPR_InsertMedia(MEDIA_FILE_PATH, 1) # 1=add new track
	else:
		media = RPR_InsertMedia(MEDIA_FILE_PATH, 0) # 0=add to current track







