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

print "\n3. exec\n"

globals = {'x': 7, 'y': 10, 'birds': ['Parrot', 'Swallow', 'Albatross']}

exec "for b in birds: print b" in globals

print "\n4. try, except\n"

try:
	f0 = open("Lesson37_not_exists.py", "r")
	print "Opening file Lesson37_not_exists.py..."
except IOError:
	print "Oops, file not exists!"
except:
	print "Oops, unknown error!"

print "\n5. finally\n"
f1 = open("Lesson37.py", "r")
try:
	print f1.readline()
except:
	print "Oops, read file error!"
finally:
	f1.close()
	print "Resource freed!"

print "\n6. raise\n"

try:
	s = None
	if s is None:
		print "s is NULL"
		raise TypeError
	print len(s)
except TypeError:
     print "NULL doesn't have length"