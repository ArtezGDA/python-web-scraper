"""
amount_normalizer.py

Script that normalizes the amount string to an integer number in USD
"""

def normalize_amount(stringInput):
	return 0

def main():
	"""
		To test just print each line
	"""
	testfile = open('box_office_amounts.txt', 'r')
	for line in testfile.readlines():
		print line
	testfile.close()
	
	
if __name__ == '__main__':
	main()