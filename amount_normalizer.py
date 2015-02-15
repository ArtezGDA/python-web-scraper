"""
amount_normalizer.py

Script that normalizes the amount string to an integer number in USD
"""

def normalize_amount(stringInput):
	#
	# Only if the amount starts with a '$'
	if stringInput.startswith('$'):
		
		# Strip of the '$'
		stringInput = stringInput.strip('$')
		
		# Get rid of all comma's
		stringInput = stringInput.replace(',','')
		
		# Calculate the multiplier
		multiplier = 1
		
		# million
		if stringInput.endswith('million'):
			multiplier = 1000000
			stringInput = stringInput.strip('million')

		# billion
		if stringInput.endswith('billion'):
			multiplier = 1000000000
			stringInput = stringInput.strip('billion')
			
		# print stringInput + " " + str(multiplier)
		amount = int(round(float(stringInput) * multiplier))
		return amount
		
	else:
		return None

def main():
	"""
		To test just print each line
	"""
	testfile = open('box_office_amounts.txt', 'r')
	for line in testfile.readlines():
		# Strip white space around the line (in this case the newline \n )
		test_text = line.strip()
		print normalize_amount(test_text)
	testfile.close()
	
	
if __name__ == '__main__':
	main()