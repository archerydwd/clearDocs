from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
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
	comment_file = ""
	list_of_attributes = []
	for line in read_data:
		
		# Identify name of the class to be used in the class summary section
		# Ignore 'class' if inside a comment section
		if 'class' in line and '*' not in line and '//' not in line:
			comment_file = "Class Summary"
			class_name = getClassName(line) 
			comment_file = comment_file + "\n" + class_name
			comment_file = comment_file + "\n" + "Access Modifier: "
			line_items = line.split()
			comment_file = comment_file + "\n" + line_items[0] + "\n"
		
		# Identify methods and attributes adding the methods to the output and storing the attributes to be added after the loop
		if 'public' in line or 'private' in line or 'protected' in line:
			if inserted == False: 
				comment_file = comment_file + "\nMethods in file:\n"
				inserted = True
			if class_name not in line and 'public static void main(String[] args)' not in line and '(' in line:
				comment_file = comment_file + line.lstrip() + "\n"
	
			if '(' not in line and class_name not in line:
				list_of_attributes.append(line)
	
	comment_file = comment_file + "\nClass Attributes in file:\n"
	for line in list_of_attributes:
		comment_file = comment_file + line.lstrip() + "\n"

	comment_file = comment_file + "\nCode:\n"
	for line in read_data:
		comment_file = comment_file + line + "\n"
		
	with open(class_name + "Comments.html", 'w') as html_file:
		html_file.write(highlight(comment_file, PythonLexer(), HtmlFormatter()))
else:
	print("it's not supported")



