__author__ = 'davidhalldor'

import os
for dirpath, dirnames, filenames in os.walk("Snidagerd"):
  print dirpath
  for fn in filenames:
      print "   ", fn
      os.remove(os.path.abspath(dirpath + os.sep + fn))