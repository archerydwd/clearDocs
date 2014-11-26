import argparse # this is a python library for taking in arguments from the terminal
# why are we using python? need to be able to answer this.
#https://docs.python.org/2/library/argparse.html#module-argparse
# create 
parser = argparse.ArgumentParser(description='Process source code files.')


def getinput(source):
	with open(source, "r") as code:
		read_date = code.read()


