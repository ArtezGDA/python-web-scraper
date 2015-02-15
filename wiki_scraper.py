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
	
	# Dump all elements (only for debugging)
	for elem in title_elements:
		
		# Dump each element
		ElementTree.dump(elem)
		
	# Return the array
	return movies

def main():
	movies = get_all_movies()
	print movies
	
if __name__ == '__main__':
	main()