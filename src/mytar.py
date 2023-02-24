import os, sys

def tarXandC(fd, fileName, encodeFlag, directory):
	bytes = os.read(fd,100)
	if encodeFlag:
		with open(directory+fileName+".tar", 'wb') as cFile:
			cFile.write(bytes)
	else:
		os.remove(directory+fileName)
		with open(fileName[-4:], 'wb') as xFile:
			xFile.write(bytes)

directory = ""
if sys.argv[1] == 'c' or sys.argv[1] == 'C':
	encodeFlag = True
	if sys.argv[-2] == 'f':
		if sys.argv[-1][0] != '/':
			directory = "".join(sys.argv[2:-2])
		else:
			directory = os.getcwd() + sys.argv[-1] + '/'
		files = sys.argv[2:-2]
	else:
		files = sys.argv[2:]
elif sys.argv[1] == 'x' or sys.argv[1] == 'X':
	encodeFlag = False
	if sys.argv[-2] == 'f':
		if sys.argv[-1][0] == '/':
			directory = os.getcwd() + sys.argv[-1] + '/'
			allFiles = os.listdir(directory)
			files = list(filter(lambda file: file[-4:] == '.tar', allFiles))
		else:
			sys.exit("'"+sys.argv[-1]+"' is not a valid directory.")
	else:
		allFiles = os.listdir(os.getcwd())
		files = list(filter(lambda file: file[-4:] == '.tar', allFiles))
else:
	sys.exit("'"+sys.argv[1]+"' is not recognized as a command.")
for file in files:
	fd = os.open(file, os.O_RDONLY)
	tarXandC(fd, file, encodeFlag, directory)
