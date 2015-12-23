"""
wiki_scraper.py

Simple scraper that pulls multiple pages from wikipedia.
"""

# Importing the necessary modules
from urllib import urlopen
from xml.etree import ElementTree
import json

from amount_normalizer import normalize_amount


def get_all_movies():
	"""
		get_all_movies()

		Scrapes a single page with a list of movies.
		Adds each movie to an array.
		And returns that array
	"""
	#
	# Scraping Settings
	#
	# Set the url of all the movies
	all_movies_url = "http://en.wikipedia.org/wiki/List_of_Walt_Disney_Animation_Studios_films"
	# Set the xpath for all titles
	titles_xpath = './/td[@class="summary"]'


	# open (and load) the site, then read the html
	site = urlopen(all_movies_url)
	html = site.read()
	
	# parse the html as an XML-tree
	tree = ElementTree.fromstring(html)
	
	# find all titles
	title_elements = tree.findall(titles_xpath)
	# print len(title_elements)
	
	# Create an empty array
	movies = []
	
	# Get the title and the link from the elements
	for elem in title_elements:
		
		# Create empty movie dictionary
		movie = {}
		
		# Get the <a> sub element
		sub_element_xpath = ".//a"
		anchor_elem = elem.find(sub_element_xpath)

		# Only try to get the anchor if there is one
		if anchor_elem is not None:
			
			# Only add the movie if the title is not None
			title = anchor_elem.text
			if title is not None:
				
				# Set the title
				movie['title'] = title

				# Get the href as link
				movie['link'] = anchor_elem.get('href')

				# Append the dict to the array
				movies.append(movie)
			
	# Return the array
	return movies


def get_box_office_number(movie):
	"""
		get_box_office_number(movie)

		Returns the box office number for the given movie (dict).
		Expects a dictionary with at least the 'link' key
	"""
	# 
	# Scraping Variables 
	# 
	# Set a Base URL
	base_url = "http://en.wikipedia.org"
	# The xpath to get the table header "Box Office"
	# table_header_xpath = './/table[contains(@class, "infobox")]//th[contains(.,"Box office")]'
	
	# create full url
	full_url = base_url + movie['link']
	
	# open (and load) the site, then read the html
	site = urlopen(full_url)
	html = site.read()
	
	# parse the html as an XML-tree
	tree = ElementTree.fromstring(html)

	# Construct a parent map
	parent_map = dict((c, p) for p in tree.getiterator() for c in p)
	
	# find all the tables
	tables = tree.findall(".//table")
	
	# Go through all the tables to find the one with class = "infobox"
	for t in tables:
		
		# Get the class of the table
		t_class = t.get('class')
		
		# Only if the table contains "infobox"
		if "infobox" in t_class:
			
			# Now we know that the element t is the infobox table!
			
			# Get all the table headers (th)
			ths = t.findall(".//th")
			
			# Go through all the table heaers to find the th with "Box office"
			for th in ths:
				
				# Get the text of this th
				text = th.text
				
				# Only if the text contains "Box office"
				if text and "Box office" in text:
					
					# Now we know that the element th is the table header for Box office
					
					# Get the parent of this th
					box_office_row = parent_map[th]
					
					# Get the td of this tr
					td = box_office_row.find("td")
					
					# The amount is in the text
					amount_text = td.text
					
					# Return the normalized amount
					return normalize_amount(amount_text)
				
	

def add_box_office_numbers(movies):
	"""
		add_box_office_numbers(movies)

		Adds the Box office number to each of the movies provided.
		Does not return anything, but modifies the given array.
		Expects an array with dicts. Each dict should be our "movie dict"
	"""
	# Find the box office number for each movie
	for movie in movies:
		# 
		# Print the title for debugging
		print movie['title']
		# Set the box office in the dict
		movie['box_office'] = get_box_office_number(movie)


def main():
	"""
		main()

		Main function with overall the recipe / strategy for scraping. 
	"""
	#
	# Get all the movies from the overview page
	movies = get_all_movies()
	
	# Add release dates to the movies
	add_box_office_numbers(movies)

	# Outputs the movies as JSON
	with open('disney_movies.json', 'w') as outfile:
		json.dump(movies, outfile)
	
if __name__ == '__main__':
	main()