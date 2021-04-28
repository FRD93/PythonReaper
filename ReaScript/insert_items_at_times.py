"""
Insert media items at specific time stamps.

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

# Path to media item
MEDIA_FILE_PATH = "/Users/admin/Desktop/LABA - Sound Design - Video Files/Horror_lights_01/audio/Light.wav"

# Media file duration (s)
MEDIA_FILE_DUR = 1.0

# Start time (s)
START_TIME = 0.0

#########################
### END OF PARAMETERS ###
#########################

import os
import sys

def unselectTracks():
	for track_id in range(RPR_CountTracks(0)):
		RPR_SetTrackSelected(RPR_GetTrack(0, track_id), False)

def selectTrack(track_id):
	unselectTracks()
	RPR_SetTrackSelected(RPR_GetTrack(0, track_id), True)
	RPR_ShowConsoleMsg("Selected track: " + str(track_id) + "\n")

with open(TIME_STAMPS_FILE_PATH, "r") as file:
	track_last_times = []
	times = file.read().split("\n")
	times = list(filter(lambda x: len(x) > 0, times))
	for index, time in enumerate(times):
		unselectTracks()
		time = time.split(" ")
		RPR_SetEditCurPos(float(time[0]) + START_TIME, True, True)
		if index == 0:
			# insert media into new track
			media = RPR_InsertMedia(MEDIA_FILE_PATH, 1) # 1=add new track
			# set media position
			#RPR_SetMediaItemPosition(media, float(time[0]) + START_TIME, False) # False: no refresh UI
			# get index of first track
			firstTrack = RPR_CountTracks(0) - 1
			# get last time for overlapping tracks
			track_last_times.append([RPR_CountTracks(0) - 1, float(time[0]) + START_TIME])
			msg = "First media inserted at: " + str(float(time[0]) + START_TIME) + "\n"
			RPR_ShowConsoleMsg(msg)
		elif index < len(times):
			new_track_needed = True
			for ltt_id, last_track_time in enumerate(track_last_times):
				if last_track_time[1] < (float(time[0]) + START_TIME):
					selectTrack(last_track_time[0])
					media = RPR_InsertMedia(MEDIA_FILE_PATH, 0) # 0=add to current track
					#RPR_SetMediaItemPosition(media, float(time[0]) + START_TIME, False) # False: no refresh UI
					track_last_times[ltt_id][1] = float(time[0]) + START_TIME
					msg = "Media inserted in existing track: " + str(last_track_time[0]) + ", time: " + str(float(time[0]) + START_TIME) + "\n"
					RPR_ShowConsoleMsg(msg)
					new_track_needed = False
					break
				break
			if new_track_needed:
				media = RPR_InsertMedia(MEDIA_FILE_PATH, 1) # 0=add to current track
				RPR_SetMediaItemPosition(media, float(time[0]) + START_TIME, False) # False: no refresh UI
				track_last_times.append([RPR_CountTracks(0) - 1, float(time[0]) + START_TIME])
				msg = "Media inserted in new track: " + str(track_last_times[-1][0]) + ", time: " + str(float(time[0]) + START_TIME) + "\n"
				RPR_ShowConsoleMsg(msg)
			
		else:
			for ltt_id, last_track_time in enumerate(track_last_times):
				if last_track_time[1] < (float(time[0]) + START_TIME):
					selectTrack(last_track_time[0])
					media = RPR_InsertMedia(MEDIA_FILE_PATH, 0) # 0=add to current track
					#RPR_SetMediaItemPosition(media, float(time[0]) + START_TIME, False) # False: no refresh UI
					track_last_times[ltt_id][1] = float(time[0]) + START_TIME
					break
			media = RPR_InsertMedia(MEDIA_FILE_PATH, 1) # 0=add to current track
			#RPR_SetMediaItemPosition(media, float(time[0]) + START_TIME, True) # True: refresh UI
		print(track_last_times)








