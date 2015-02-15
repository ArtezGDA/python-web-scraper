"""
	json_read_example.py
	
	Simple example script that reads a pre-saved JSON file
"""

import json


def main():
	"""
		Simply read the JSON from file and print the number of movies
	"""
	
	with open('disney_movies.json') as movies_file:
		data = json.load(movies_file)
		
	print len(data)
	print data[0]
	

if __name__ == '__main__':
	main()