

def parseTextMessage(str):
	
	forIndex = str.index("From")
	fromString = str[4:forIndex]
	toString = str[forIndex+6:]
	print fromString
	print toString


if __name__ == "__main__":
	inputString = input('From \n')
	inputString2 = input('To \n')
	directionString = 'To: ' + inputString + 'From: '+ inputString2
	print 'Argument List:', directionString
	parse1(directionString)