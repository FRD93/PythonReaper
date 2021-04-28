"""
Generate a random step envelope for the desired parameter.

Copyright 2021, Francesco Roberto Dani
www.francesco-dani.com
f.r.d@hotmail.it

"""

##############################
### CHANGE PARAMETERS HERE ###
##############################

# Number of points
N = 150

# Min value
MIN = 0.3

# Max value
MAX = 1.0 

# Step (value)
STEP_VAL = 0.01

# Is envelope in dB?
DB = False

# Start time (s)
START_TIME = 0.0

# End time (s)
END_TIME = 60.0

# Step (time) (s)
STEP_TIME = 0.0001

#########################
### END OF PARAMETERS ###
#########################

import os
import sys
import random

"""
for i in range(RPR_CountSelectedMediaItems(0) - 1):
	media = RPR_GetSelectedMediaItem(0, i)
	for j in range(RPR_CountTakes(media) - 1):
		take = RPR_GetMediaItemTake(media, j)
"""

# RPR_GetFXEnvelope(MediaTrack track, Int fxindex, Int parameterindex, Boolean create)

env = RPR_GetSelectedTrackEnvelope(0)
times = [round(random.uniform(START_TIME, END_TIME) / STEP_TIME) * STEP_TIME for i in range(N * 2)]
times.sort()
times = list(zip(*[iter(times)] * 2))

values = [round(random.uniform(MIN, MAX) / STEP_VAL) * STEP_VAL for i in range(N)]


RPR_SetEditCurPos(0, True, True)
_, _, _, _, _, _, _, _ = RPR_InsertEnvelopePoint(env, 0, values[0], 0, 0, 0, True)
	
for index, time in enumerate(times):
	value = values[index]
	
	last_index = max(0, min(index - 1, len(times) - 1))
	next_index = max(0, min(index + 1, len(times) - 1))

	last_time = max(START_TIME, times[last_index][1] - 0.0005)
	last_value = values[last_index]

	next_time = min(times[-1][1], times[next_index][0] + 0.0005)
	next_value = values[next_index]

	if DB:
		RPR_ShowConsoleMsg(str(value) + " ")
		scale = RPR_GetEnvelopeScalingMode(env)
		value = RPR_ScaleToEnvelopeMode(scale, value)
	RPR_ShowConsoleMsg("Times:" + str(last_time) + " " + str(time) + " " + str(next_time) + "\n")
	RPR_ShowConsoleMsg("Values:" + str(last_value) + " " + str((value, value)) + " " + str(next_value) + "\n\n")

	RPR_SetEditCurPos(max(0, time[0] - 0.005), True, True)
	_, _, _, _, _, _, _, _ = RPR_InsertEnvelopePoint(env, max(0, time[0] - 0.005), last_value, 0, 0, 0, True)
	
	RPR_SetEditCurPos(time[0], True, True)
	_, _, _, _, _, _, _, _ = RPR_InsertEnvelopePoint(env, time[0], value, 0, 0, 0, True)
	
	RPR_SetEditCurPos(time[1], True, True)
	_, _, _, _, _, _, _, _ = RPR_InsertEnvelopePoint(env, time[1], value, 0, 0, 0, True)
	RPR_SetEditCurPos(min(0, time[1] + 0.005), True, True)
	_, _, _, _, _, _, _, _ = RPR_InsertEnvelopePoint(env, min(0, time[1] + 0.005), next_value, 0, 0, 0, True)
	
RPR_Envelope_SortPoints(env)





