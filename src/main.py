import sys, io, os

file_dir = os.path.dirname(__file__)
rel_supported_languages = 'supported-languages.txt'
abs_supported_languages = os.path.join(file_dir, rel_supported_languages)
class_name = ""

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

def getClassName(line):
	pos = line.index('class')
	words_in_line = line[7:].split()
	return words_in_line[1]

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
	inserted = False
	comment_file = "<html><head><title>ClearDocs</title></head><body>"
	list_of_attributes = []
	count = 0
	counter = 0
	attr_count = 0
	for line in read_data:
		# Identify name of the class to be used in the class summary section
		# Ignore 'class' if inside a comment section
		if 'class' in line and '*' not in line and '//' not in line:
			comment_file = comment_file + "<u><b>Class Summary</b></u><br> <b>Class Name</b><br>"
			class_name = getClassName(line) 
			comment_file = comment_file + class_name
			comment_file = comment_file + "<br>" + "<b>Access Modifier</b>"
			line_items = line.split()
			comment_file = comment_file + "<br>" + line_items[0] + "<br>"
		
		# Identify methods and attributes adding the methods to the output and storing the attributes to be added after the loop
		if 'public' in line or 'private' in line or 'protected' in line:
			if class_name not in line and 'public static void main(String[] args)' not in line and '(' in line:
				if inserted == False: 
					comment_file = comment_file + "<br><u><b>Method Summary</b></u><br>"
					inserted = True
				comment_file = comment_file + "&emsp;<b>Method Name and Formal Parameters</b><br>"
				comment_file = comment_file + "&emsp;<a href='#method" + str(count) + "'>" + line.lstrip() + "</a><br>"
				count += 1
				line_items = line.split()
				comment_file = comment_file + "&emsp;<b>Access Modifier: " + line_items[0] + "</b><br>"	
				if 'static' in line:
					 comment_file = comment_file + "&emsp;<b>Type: " + line_items[1] + " " + line_items[2] + "</b><br><br>"
				else:
					comment_file = comment_file + "&emsp;<b>Type: " + line_items[1] + "</b><br><br>"
			if '(' not in line and class_name not in line:
				list_of_attributes.append(line)
			
			# Identify Default Constructors
			if class_name in line and '()' in line:
				comment_file = comment_file + "<br><u><b>Constructor summary</b></u><br>"	
				comment_file = comment_file + "&emsp;Default Constructor: <a href='#constructor" + str(counter) + "'>" + line + "</a><br>"
				counter += 1		
			# List containing Java data types 
			data_types=['byte','short','int','long','float','double','char','String','boolean','(' + class_name]
			# Identify any other Constructors
			if class_name in line and not '()' in line and any(word in line for word in data_types):
				comment_file = comment_file + "&emsp;Other Constructor: <a href='#constructor" + str(counter) + "'>" + line + "</a><br>"
				counter += 1		
	
	comment_file = comment_file + "<br><u><b>Class Attribute summary</b></u><br>"
	for line in list_of_attributes:
		comment_file = comment_file + "&emsp;<a href='#attribute" + str(attr_count) + "'>" + line.lstrip() + "</a><br>"
		attr_count += 1

	comment_file = comment_file + "<br><u><b>Code</b></u><br>"
	
	countm = 0
	countc = 0
	counta = 0
	for line in read_data:
		if 'public' in line or 'private' in line or 'protected' in line:
			if class_name not in line and 'public static void main(String[] args)' not in line and '(' in line:
				comment_file = comment_file + "<a name='method" + str(countm) + "'></a>"
				countm += 1
			if '(' not in line and class_name not in line:
				comment_file = comment_file + "<a name='attribute" + str(counta) + "'></a>"
				counta += 1
			if class_name in line and '()' in line:
				comment_file = comment_file + "<a name='constructor" + str(countc) + "'></a>"
				countc += 1
			if class_name in line and '(' in line and any(word in line for word in data_types):
				comment_file = comment_file + "<a name='constructor" + str(countc) + "'></a>"
				countc += 1		
		comment_file = comment_file + line + "<br>"
	
	comment_file = comment_file + "<br></body></html>"

	with open(class_name + "Comments.html", 'w') as html_file:
		html_file.write(comment_file)
else:
	print("it's not supported")



