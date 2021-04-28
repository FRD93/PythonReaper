"""
Insert markers at specific time stamps.

Copyright 2021, Francesco Roberto Dani
www.francesco-dani.com
f.r.d@hotmail.it


Time stamps file formats:

## FORMAT A: ##
time
time
time
.
.
.

## FORMAT B: ##
time marker_name
time marker_name
time marker_name
.
.
.
"""

##############################
### CHANGE PARAMETERS HERE ###
##############################

# Path to file containing time stamps
TIME_STAMPS_FILE_PATH = "/Users/admin/Desktop/LABA - Sound Design - Video Files/Horror_lights_01/video/peaks.txt"

# Default marker name (if file is formatted as FORMAT A)
MARKERS_DEFAULT_NAME = "FRDMarker"

# Start time (s)
START_TIME = 0.0

#########################
### END OF PARAMETERS ###
#########################

import os
import sys



with open(TIME_STAMPS_FILE_PATH, "r") as file:
	times = file.read().split("\n")
	times = list(filter(lambda x: len(x) > 0, times))
	for time in times:
		time = time.split(" ")
		if len(time) == 1:
			time.append(MARKERS_DEFAULT_NAME)
		time[0] = float(time[0]) + START_TIME
		# True per Regioni, False per Marker!
		RPR_AddProjectMarker2(0, False, time[0], time[0] + 0.0, time[1], -1, 0)
    










