from __future__ import division

print "Today is " + "%s" % "Monday."

print "%d/%02d/%d" % (1008*2, 300/100, 31-3)

print "Do you know how to compute 6^6? It is %d." % 6**6

print "Integer division 3.5/2 =", 3.5//2

print "101 % 24 =", 101 % 24

print "< > <= >= == !=/<>"

#list
zoo = ['pig','tiger','dog']
print zoo
#tuple
country = ('bj', ['sh','gd'])
print country
#dictionary
dict = {'name':'Pei', 'age':'26'}
print dict

def minus(f):
	print 'minus'
	f()

def plus(f):
	print 'plus'
	f()

def test(a):
	if a > 3:
		print "pass"
		return plus
	else:
		print "fail"
		return minus

@test(5)
def xxx():
	print 'ok'

@minus
def xxx():
	print 'ok'

#@dec2  
#@dec1  
#def func(arg1, arg2, ...):  
#    pass 

#def func(arg1, arg2, ...):  
#    pass  
#func = dec2(dec1(func))   

print "OK, Lesson37 finished!";