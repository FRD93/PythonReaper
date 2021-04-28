"""
Generate a random envelope for the desired parameter.

Copyright 2021, Francesco Roberto Dani
www.francesco-dani.com
f.r.d@hotmail.it
"""

##############################
### CHANGE PARAMETERS HERE ###
##############################

# Number of points
N = 50

# Min value
MIN = -0.23

# Max value
MAX = 0.23

# Step (value)
STEP_VAL = 0.01

# Is envelope in dB?
DB = False

# Start time (s)
START_TIME = 0.0

# End time (s)
END_TIME = 60.0

# Step (time) (s)
STEP_TIME = 1.0

#########################
### END OF PARAMETERS ###
#########################

import os
import sys
import random
from reaper_python import *

"""
for i in range(RPR_CountSelectedMediaItems(0) - 1):
	media = RPR_GetSelectedMediaItem(0, i)
	for j in range(RPR_CountTakes(media) - 1):
		take = RPR_GetMediaItemTake(media, j)
"""

# RPR_GetFXEnvelope(MediaTrack track, Int fxindex, Int parameterindex, Boolean create)

env = RPR_GetSelectedTrackEnvelope(0)

for index in range(N):
	time = round(random.uniform(START_TIME, END_TIME) / STEP_TIME) * STEP_TIME
	value = round(random.uniform(MIN, MAX) / STEP_VAL) * STEP_VAL
	if DB:
		RPR_ShowConsoleMsg(str(value) + " ")
		scale = RPR_GetEnvelopeScalingMode(env)
		value = RPR_ScaleToEnvelopeMode(scale, value)
	RPR_SetEditCurPos(time, True, True)
	RPR_ShowConsoleMsg("" + str(time) + " " + str(value) + "\n")
	#_, _, _, _, _, _, _, _, _ = RPR_SetEnvelopePoint(env, -1, time, value, -1, -1, -1, -1)
	_, _, _, _, _, _, _, _ = RPR_InsertEnvelopePoint(env, time, value, 0, 0, 0, True)
RPR_Envelope_SortPoints(env)






