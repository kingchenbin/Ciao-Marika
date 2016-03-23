from sys import argv
from sys import exit
import os

script, txt = argv

NPC = []

def adventure():
	print "In a very beautiful village, there are three brilliant boys. They are "
	names = ""
	for char in NPC:
		names += char + " "
	print "\t%s" % names

def quit(why):
	print why, "Good bye!"
	exit()

def start(text):
	if not os.path.exists(text):
		quit("Text not exists.")
	else:
		text = open(text, 'r')

	for line in text.readlines():
		line = line.strip('\n')
		NPC.append(line)

	adventure()

start(txt)