__author__ = 'davidhalldor'
# Setting up the libs
# http://stackoverflow.com/questions/13984357/pythonmagick-cant-find-my-pdf-files

from PythonMagick import Image
im = Image()

import os
for dirpath, dirnames, filenames in os.walk("Snidagerd"):
  print dirpath
  for fn in filenames:
    print "   ", fn
    new_fn = fn.replace(".pdf", ".jpg")
    print "New file name: ", new_fn
    if fn.find(".jpg") is -1:
        im.read(os.path.abspath(dirpath + os.sep + fn))
        im.write(os.path.abspath(dirpath + os.sep + new_fn))
        os.remove(os.path.abspath(dirpath + os.sep + fn))

