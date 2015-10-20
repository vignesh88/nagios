import xml.parsers.expat,sys
from glob import glob
import os
import os.path
import sys

## Writing the output to a log file
Output_file = sys.argv[2]
sys.stdout = open(Output_file, 'w')

def parsefile(file):
    parser = xml.parsers.expat.ParserCreate()
    parser.ParseFile(open(file, "r"))

def xml_check():
    for arg in sys.argv[1:]:
        for filename in glob(arg):
            try:
                parsefile(filename)
                print "%s is well-formed" % filename
	        sys.exit(0)
            except Exception, e:
                print "%s is %s" % (filename, e)
		sys.exit(2)

LOG_FILE = sys.argv[1]
if os.path.isfile(LOG_FILE):
   xml_check()
else:
   print LOG_FILE ,"- does not exist"
   sys.exit(2)

