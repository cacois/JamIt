'''
JamIt - a script to generate scaffolding for Google Code Jam problems. 
'''

import os
import sys
import jamit

# create new file for problem, name from input parameter
appname = sys.argv[1]
print(appname)
if not os.path.exists(appname):
    os.makedirs(appname)
filepath = os.path.join(appname, appname + ".py")
print(filepath)
outfile = open(filepath,"w")

# open template file
## Need to find template file location based on location of jamit library 
templatefile = open("jamit/template","r")
template = templatefile.read()
outfile.write(template.format(appname))