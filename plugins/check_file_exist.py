import os
import os.path
import sys

LOG_FILE = sys.argv[1]
if os.path.isfile(LOG_FILE):
   print LOG_FILE , "- exist "
   sys.exit(0)
else:
   print LOG_FILE ,"- does not exist"
   sys.exit(2)

