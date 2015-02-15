"""
wiki_scraper.py

Simple scraper that pulls multiple pages from wikipedia.
"""

# Importing the necessary modules
from urllib import urlopen
from xml.etree import ElementTree


"""
	get_all_movies()
	
	Scrapes a single page with a list of movies.
	Adds each movie to an array.
	And returns that array
"""
def get_all_movies():
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


"""
	get_box_office_number(movie)
	
	Returns the box office number for the given movie (dict).
	Expects a dictionary with at least the 'link' key
"""
def get_box_office_number(movie):
	# 
	# Scraping Variables 
	# 
	# Set a Base URL
	base_url = "http://en.wikipedia.org"
	# The xpath to get the table header "Box Office"
	table_header_xpath = './/table[contains(@class, "infobox")]//th[contains(.,"Box office")]'
	
	# create full url
	full_url = base_url + movie['link']
	
	# open (and load) the site, then read the html
	site = urlopen(full_url)
	html = site.read()
	
	# parse the html as an XML-tree
	tree = ElementTree.fromstring(html)
	
	# find the box office header
	box_header = tree.find(table_header_xpath)
	
	

"""
	add_box_office_numbers(movies)
	
	Adds the Box office number to each of the movies provided.
	Does not return anything, but modifies the given array.
	Expects an array with dicts. Each dict should be our "movie dict"
"""
def add_box_office_numbers(movies):
	# Find the box office number for each movie
	# For testing first only get the 1st one.
	for movie in movies[0:1]:
		# Simply print the box office number (for now)
		print get_box_office_number(movie)


"""
	main()

	Main function with overall the recipe / strategy for scraping. 
"""
def main():
	#
	# Get all the movies from the overview page
	movies = get_all_movies()
	
	# Add release dates to the movies
	add_box_office_numbers(movies)
	# print movies
	
	
if __name__ == '__main__':
	main()