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

print "\n7. yield\n"

def fab(max):
    n, a, b = 0, 0, 1
    L = []
    while n < max:
        L.append(b)
        a, b = b, a + b
        n = n + 1
    return L

def fab_yield(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1

for n in fab(5): # return a List
	print n,

print "\n"

for n in fab_yield(5): # not return a List, but a iterable object
	print n,

print "\n"

print "8. is\n"

List1 = [21, 'clock']
List2 = [21, 'clock']

print "List1 = [21, 'clock']"
print "List2 = [21, 'clock']"
print "Does %r == %r ?\n> %r, they have same member and value." %( List1, List2, List1 == List2)
print "Does %r is %r ?\n> %r, they are different object(correspond to different memory)." %( List1, List2, List1 is List2)

print "\n9. lambda\n"

def foo():
	return 'Being with you is Amazing !'

bar = lambda:'Being with you is Amazing !' # a function object

print foo()
print bar()

def add(x,y):
	return x+y
add2 = lambda x,y : x+y
print add(1,2)
print add2(1,2)

def sum(x,y=10):
	return x+y
sum2 = lambda x,y=10 : x+y
print sum(11)
print sum2(11)

print "\n10. with, as\n"

with open("lesson22.txt", 'r') as file:
    for line in file:
    	print line

somefile = open('lesson22.txt', 'r')
try:
	for line in somefile:
		print line
finally:
	somefile.close()

print "\n11. class\n"

class MyClass:
	idx = 0
	somefile
	def __init__(self):
		print "MyClass initialize."
		self.somefile = open('lesson22.txt', 'r')
		self.idx = 1
		print "Open lesson22.txt for reading."
	def out(self):
		print self.somefile.readline()
	def __del__(self):
		self.somefile.close()
		print "File closed. Bye bye!"


classA = MyClass()
classA.out()
del classA