"""
wiki_scraper.py

Simple scraper that pulls multiple pages from wikipedia.
"""

# Importing the necessary modules
from urllib import urlopen
from xml.etree import ElementTree


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
		
		if anchor_elem is not None:
			# Get the text as title
			movie['title'] = anchor_elem.text

			## Getting the keys
			# anchor_elem.keys()
			# anchor_elem.get

			# Get the href as link
			movie['link'] = anchor_elem.get('href')

			# Append the dict to the array
			movies.append(movie)
		else:
			ElementTree.dump(elem)
			
	# Return the array
	return movies

def main():
	movies = get_all_movies()
	print movies
	
if __name__ == '__main__':
	main()