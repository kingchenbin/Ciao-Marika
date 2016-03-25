# ~ https://docs.python.org/2.7/library/stdtypes.html#string-formatting-operations

from sys import argv

script = argv

print "%d. This is sample code for %s.\n" % (1, script)

print "%i. Actually %%d and %%i are the same.\n" % 2

print "3. 25 = %o in octal.\n" % 25

print "4. 25 = %x or %X in hexadecimal.\n" % (28, 28)

print "5. What's the difference between %%d and %%u? %%u is obsolete.\n"

print "6. Floating point decimal %5.5f or %5.5F.\n" % (87.26, 1.2866987)

print "7. Floating point exponential %5.5e or %5.5e.\n" % (87.26, 0.0066987)

print "8. %%g is really compicated, it varies between decimal and exponential.\n"

print "9. %c and %c are the same.\n" %('V', 86)

print "%r. Thank God! We have %%r. %r.\n" % (10, 'It\'s versatile')