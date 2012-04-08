'''
JamIt - Google Code Jam Scaffold Generator

Copyright (C) 2012 C. A. Cois

Permission is hereby granted, free of charge, to any person obtaining a copy of 
this software and associated documentation files (the "Software"), to deal in 
the Software without restriction, including without limitation the rights to 
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies 
of the Software, and to permit persons to whom the Software is furnished to do 
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all 
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
SOFTWARE.
'''

import os
import sys
from shutil import copyfile

# create new file for problem, name from input parameter

if len(sys.argv) < 2:
	print "jamit-gen.py\n\nUsage: $ python jamit-gen.py <problem_name> <filepath?>\n"
	exit()

appname = sys.argv[1]

filepath = None
basepath = ""

#set base path if one was specified
if len(sys.argv) > 2:
	basepath = sys.argv[2]
	if not os.path.exists(basepath):
		os.makedirs(basepath)

filepath = os.path.join(basepath, appname + ".py")




outfile = open(filepath,"w")

print("Generating scaffold for problem: " + appname + " at path " + filepath)

# open template file
templatefile = open("jamit/template","r")
template = templatefile.read()

# create problem code from template file
outfile.write(template.format(appname))

# copy jamit.py base code 
copyfile("jamit/jamit.py",os.path.join(basepath, "jamit.py"))