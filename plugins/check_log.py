import sys

Log_file = sys.argv[1]

for line in open(Log_file):
    if "well-formed" in line:
       print line
       sys.exit(0)
    elif "does not exist" in line:
       print line
       sys.exit(2)
