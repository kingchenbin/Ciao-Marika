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

print "\n2. assert\n"

def greater(a, b):
	if a >= b:
		return True
	elif a < b:
		return False
	else:
		assert(0)

print "Does %r greater that %r? %r" %(15, 1.75, greater(15, 1.75))