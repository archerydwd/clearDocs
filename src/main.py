import sys
# why are we using python? need to be able to answer this.

try:
	with open(sys.argv[1], "r") as code:
		read_data = code.read()
except IOError:
	print("Cannot open file! please include correct file extension") 
except ValueError:
	print("Input file is empty!")
except:
	print("Unexpected error:", sys.exc_info()[0])
	raise

def getExt(file_name):
	my_array = file_name[::-1].split('.')
	return my_array[0][::-1]

def checkLanguage(ext):
	try:
		with open('supported-languages.txt', "r") as supplang:
			supported = False
			for extension in supplang:
				if ext in extension:
					 supported = True
			return supported
	except IOError:
		print("Cannot open file! please include correct file extension") 
	except ValueError:
		print("Input file is empty!")
	except:
		print("Unexpected error:", sys.exc_info()[0])
		raise

ext = getExt(sys.argv[1])
if checkLanguage(ext):

	#continue with parsing
	print("it's supported")
	pass
else:
	print("it's not supported")
