import sys, io, os
# why are we using python? need to be able to answer this.

file_dir = os.path.dirname(__file__)
rel_supported_languages = 'supported-languages.txt'
abs_supported_languages = os.path.join(file_dir, rel_supported_languages)

try:
	with open(sys.argv[1], "r") as code:
		read_data = code.read().split('\n')
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
		with open(abs_supported_languages, "r") as supplang:
			supported = False
			for extension in supplang:
				if ext in extension:
					 supported = True
			return supported
	except IOError:
		print("Cannot open supported languages file!") 
	except ValueError:
		print("Supported languages file is empty!")
	except:
		print("Unexpected error:", sys.exc_info()[0])
		raise

ext = getExt(sys.argv[1])
if checkLanguage(ext):
	for line in read_data:
		if 'public' in line or 'private' in line:
			print(line)
		
		if '*' in line:
			print(line)
			

else:
	print("it's not supported")
