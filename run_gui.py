"""
Insert media items at specific time stamps.

Copyright 2021, Francesco Roberto Dani
www.francesco-dani.com
f.r.d@hotmail.it
"""

import os
import sys
RPR_AddProjectMarker2(0, False, 1, 1, "Hey", -1, 0)
RPR_include("dep/insert_markers_from_times_func.py")

# Path to file containing time stamps
TIME_STAMPS_FILE_PATH = "/Users/admin/Desktop/LABA - Sound Design - Video Files/Horror_lights_01/video/peaks.txt"
# Default marker name (if file is formatted as FORMAT A)
MARKERS_DEFAULT_NAME = "FRDMarker"
# Start time (s)
START_TIME = 0.0
insert_markers_from_times(TIME_STAMPS_FILE_PATH, START_TIME, MARKERS_DEFAULT_NAME)
