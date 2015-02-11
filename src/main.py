from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
import sys, io, os

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
	inserted = False
	for line in read_data:
		
		# Identify name of the class to be used in the class summary section
		# Ignore 'class' if inside a comment section
		if 'class' in line and '*' not in line and '//' not in line:
			comment_file = "Class Summary"
			pos=line.index('class')
			wordsof = line[7:].split()
			comment_file = comment_file + "\n" + wordsof[1]
			comment_file = comment_file + "\n" + "Access Modifier: "
			line_items = line.split()
			comment_file = comment_file + "\n" + line_items[0] + "\n"
			
		if 'public' in line or 'private' in line:
			if inserted == False: 
				inserted = True
				comment_file = comment_file + "\nMethods in file:\n"
			comment_file = comment_file + line + "\n"
		
	#	if '*' in line or '//' in line:
	#	 	comment_file = comment_file + "\nComments in file:\n"
	#	 	comment_file = comment_file + line + "\n"
		
	with open(wordsof[1] + "Comments.html", 'w') as html_file:
		html_file.write(highlight(comment_file, PythonLexer(), HtmlFormatter()))
else:
	print("it's not supported")



