"""
Utility function to create random notes and save them to file.

A variation is a mutation of a set of rhythmic-melodic sequence (in this case, a "notes" matrix), which can be
achieved by:
 - applying rhythmic variations of the notes of the sequence
 - doubling one or more notes (Do[1/4]->Re[1/4] becomes Do[1/8]->Do[1/8]->Re[1/4], etc.)
 - adding one or more auxiliary notes between two notes (Do->Mi becomes Do->Re->Mi) without changing the resulting
 	rhithm (Do[1/4]->Mi[1/4] becomes Do[1/8]->Re[1/8]->Mi[1/4], etc.)
 - mutating the order of triads where possible (Do->Mi->Sol can become Mi->Do->Sol, etc.)
 - adding or eliminating intervals (where possible, following the rules of reduction, condensation and omission)
 - combining two or more of the previous rules

Notes are formatted as: [start_time, midi_note, duration]

notes = [
	[0.0, 34, 1],
	[1.0, 22, 0.5],
	[1.5, 25, 1],
	[2.5, 41, 0.75],
	[3.25, 44, 1.5],
	[4.75, 43, 1.25],
	[6.0, 11, 1]
]

Copyright 2021, Francesco Roberto Dani
www.francesco-dani.com
f.r.d@hotmail.it

# Appunto:
Esempi sonori da Schonberg, "Elementi di composizione musicale" ascoltabili in https://www.diariomusicale.com/001Armonia/51bQ.html
"""

import random


def generateNotesVariation(notes, rhythmic=False, doubling=False, auxiliary=False, triadOrder=False, omission=False):
	"""
	*** Rhythmic variation ***
	1) Decompose the length of notes vector in a vector of numbers P containing only values of 2 or 3 (eg 7 = 2 + 2 + 3)
	2) Scramble the order of appearence of the numbers of P
	3) Get a random number N ranging from 1 to the length of P
	4) Choose N items from P
	5) For each i in N, modify the attack and duration values of the corresponding notes according to the following rules

	RULES:
	* P[i] == 2 *
	- Halves the first note duration and shift back in time the latter
	- Halves the first note duration, mantaining the second note unaltered
	- Halves the second note duration, stretching the first note's duration
	- Halves the second note duration, mantaining the first note unaltered
	- Halves the second note duration, and shift ahead in time the matter
	- - Same as above, but doubled
	* P[i] == 3 *
	- Choose one of the three notes and apply one of the rules for P[i] == 2 for the selected note and the previous or next one
	"""
	# 1) & 2)
	notes_length = len(notes)
	P = decomposeNumberIn23(notes_length)
	# 3)
	N = random.randint(1, len(P))
	# 4)
	choices = random.sample(range(len(P)), k=N)
	print(P, N, choices)
	# 5)
	for choice in choices:
		num_notes_before = sum(P[:choice])
		num_notes = P[choice]
		print(choice, num_notes_before, num_notes, notes[num_notes_before:num_notes_before + num_notes])
		notes_to_be_modifyed = notes[num_notes_before:num_notes_before + num_notes]
		case = random.randint(0, 4)

		if case == 0: # - Halves the first note duration and shift back in time the latter
			notes_to_be_modifyed[0][2] /= 2
			notes_to_be_modifyed[1][0] -= notes_to_be_modifyed[0][2]
			notes_to_be_modifyed[1][2] += notes_to_be_modifyed[0][2]
			notes[num_notes_before:num_notes_before + num_notes] = notes_to_be_modifyed
			print("case 0:", notes)
		elif case == 1: # - Halves the first note duration, mantaining the second note unaltered
			notes_to_be_modifyed[0][2] /= 2
			notes[num_notes_before:num_notes_before + num_notes] = notes_to_be_modifyed
			print("case 1:", notes)
		elif case == 2: # - Halves the second note duration, stretching the first note's duration
			notes_to_be_modifyed[1][2] /= 2
			notes_to_be_modifyed[0][2] += notes_to_be_modifyed[1][2]
			notes[num_notes_before:num_notes_before + num_notes] = notes_to_be_modifyed
			print("case 2:", notes)
		elif case == 3: # - Halves the second note duration, mantaining the first note unaltered
			notes_to_be_modifyed[1][2] /= 2
			notes[num_notes_before:num_notes_before + num_notes] = notes_to_be_modifyed
			print("case 3:", notes)
		elif case == 4: # - Halves the second note duration, and shift ahead in time the matter
			notes_to_be_modifyed[1][2] /= 2
			notes_to_be_modifyed[1][0] += notes_to_be_modifyed[0][2]
			notes[num_notes_before:num_notes_before + num_notes] = notes_to_be_modifyed
			print("case 4:", notes)



def decomposeNumberIn23(number):
	result = []
	if number < 2:
		raise ValueError
	while number > 2:
		if number == 2:
			result.append(2)
			return result
		if number == 3:
			result.append(3)
			return result
		sub = random.choice([2, 3])
		number -= sub
		result.append(sub)
	if number == 1:
		try:
			index_to_increase = result.index(2)
			result[index_to_increase] += 1
		except:
			result.pop()
			result.append(2)
			result.append(2)
	else:
		result.append(2)
	return result






if __name__ == "__main__":
	notes = notes = [
		[0.0, 34, 1],
		[1.0, 22, 0.5],
		[1.5, 25, 1],
		[2.5, 41, 0.75],
		[3.25, 44, 1.5],
		[4.75, 43, 1.25],
		[6.0, 11, 1]
	]
	generateNotesVariation(notes)

