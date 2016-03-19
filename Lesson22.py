from sys import argv
import os

script, file_name = argv

if os.path.exists(file_name):
	print ("File already exist and it will be truncated. Continue?")
	key = raw_input("Press N to skip...")
	if key == 'N' or key == 'n':
		exit()
else:
	print ("New file created.")

to = open(file_name, 'w')
to.write("Hello Stranger!\n")

to.close()