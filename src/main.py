import argparse # this is a python library for taking in arguments from the terminal 
								# https://docs.python.org/2/library/argparse.html#module-argparse

# why are we using python? need to be able to answer this.

# create a parser object
parser = argparse.ArgumentParser(description='Process source code files.')


def getinput(source):
	with open(source, "r") as code:
		read_date = code.read()


