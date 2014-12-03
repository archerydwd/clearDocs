import sys
# why are we using python? need to be able to answer this.

try:
	with open(sys.argv[1], "r") as code:
		read_data = code.read()

	def getExt(file_name):
		my_array = file_name[::-1].split('.')
		return my_array[0][::-1]

	print(getExt(sys.argv[1]))

except IOError:
	print("Cannot open file! please include correct file extension")
	
except ValueError:
	print("Input file is empty!")

except:
	print("Unexpected error:", sys.exc_info()[0])
	raise

