#

print "1. global\n"

def showGlobal():
	global x
	x = 32767
	print x

x = 520

print x
showGlobal()
print x