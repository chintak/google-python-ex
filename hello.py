#!/usr/bin/python -tt
import sys
import os
import commands

def Cat(filename):
	try:
		f = open(filename, 'rU')
		text = f.read()
		f.close()
		print '---', filename
		print text
	except IOError:
		print 'IO Error', filename

# def List(dir):
# 	cmd = 'ls -l ' + dir
# 	print 'about to do this: ', cmd
# 	(stat, out) = commands.getstatusoutput(cmd)
# 	if stat:
# 		sys.stderr.write('there was an error:' + out)
# 		sys.exit(1)
# 	print out
	
	# filenames = os.listdir(dir)
	# for filename in filenames:
	# 	path = os.path.joint(dir, filename)
	# 	print path
	# 	print os.path.abspath(path)
		
def main():
	args = sys.argv[1:] 
	for arg in args:
		Cat(arg)

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
