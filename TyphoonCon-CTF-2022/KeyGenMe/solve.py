# To get Lyrics_Metallica.json: $ python -m lyricsgenius artist "Metallica" --max-songs 1000 --save 
# This took around ten minutes
# Remember to generate a Genius API token at https://genius.com/api-clients and export the environment variable as GENIUS_ACCESS_TOKEN
# LyricsGenius: https://lyricsgenius.readthedocs.io/en/master/

import re
import json
from tqdm import tqdm
import pwn

pwn.context.log_level = 'error'

def bruteforce(arg):
	"""
	This function takes in an argument, passes it in to the binary we have to brute-force (ctf-challenge), and records the output.
	"""
	bf = pwn.process("./ctf-challenge", stdin=pwn.PIPE, stdout=pwn.PIPE) # Spawns the process.
	bf.sendline(bytearray(arg, "UTF-8"))
	output = bf.recv()
	bf.close()

	return output

def gen(example):
	"""
	This function 'gens' (generates) possible three word strings from the song lyrics we're given.
	"""
	example = re.sub(r"[\[].*?[\]]",""," ".join(example.split("\n"))).replace(",","").replace('"',"").lower().split(" ") 
	# This cleans up the lyrics by removing annotations such as [Chorus], [Verse 1], etc.
	# It then takes away all the newlines, removes all commas and quotes, puts everything in lowercase, and splits it all by spaces

	while True:
		try:
			example.remove("")
		except ValueError:
			break
	# This removes empty strings from the list resulting from the last command until no more are found.

	possible = [str(example[example.index(x)-2] + "_" + example[example.index(x)-1] + "_" + x) for x in example[:] if len(example[example.index(x)-2] + "_" + example[example.index(x)-1] + "_" + x) < 41]
	# This goes through the list and generates all possible three word 'flags' by concatenating the words and underscores and ensuring it is not over 40 characters. (This is as when investigating the binary, a teammate found a buffer of 40 for the entered flag.) 
	
	return possible
	# The resulting list of combinations is then returned.

with open("Lyrics_Metallica.json") as f:
	info = json.load(f) # Loads all songs from the lyrics file

print("[!] Generating all possible flags")
songs = [song["lyrics"] for song in info["songs"]] # Gets the lyrics string for each song in the list of songs
songs = [gen(song) for song in songs] # Generates a list of possible flags for each song
maybe = [possible for song in songs for possible in song] # Unpacks the list of lists into one list
maybe = list(set(maybe)) # Removes duplicates
print("[!] " + str(len(maybe)) + " possible flags generated")

for poss in tqdm(maybe): # Tqdm is a fancy progress bar :)
	run = bruteforce(poss) 
	if b"Nice try but no. Try again" not in run: # Runs the binary with each possible flag and checks if the output is negative. If it isn't, prints out the flag
		print("[!] Flag found! " + poss)
		print("-" * 10)
		print(run.decode('utf-8'))
		print("-" * 10)
		break