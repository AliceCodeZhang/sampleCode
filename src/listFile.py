import os
from string import atoi
from itertools import islice
import sys, getopt, time
import psutil
import commands
import re
import os
'''
this python script is used for read result folder
'''
folder = 'report'
try:
   opts, args = getopt.getopt(sys.argv[1:],"h:f:",["help", "folder="])
except getopt.GetoptError:
   print 'error : listFile.py -f <folder>'
   sys.exit(2)
for opt, arg in opts:
   if opt in ("-h", "--help"):
      print 'listFile.py -f <folder> \n'
   elif opt == '-f':
      folder = arg
   else:
      assert False, "unhandled option"

for dirname, dirnames, filenames in os.walk(folder):
     for subdirname in dirnames:
           print(os.path.join(dirname, subdirname))

