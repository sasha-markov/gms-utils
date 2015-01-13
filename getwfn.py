#!/usr/bin/python

import os.path
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename")
(options, args) = parser.parse_args()

with open(options.filename, "r") as f:
    filename, fileext = os.path.splitext(options.filename)
    sw = False
    for line in f.readlines():
        if ("----- TOP OF INPUT FILE FOR BADER'S AIMPAC PROGRAM -----" in
            line):
                sw = True
                continue
        if ("----- END OF INPUT FILE FOR BADER'S AIMPAC PROGRAM -----" in
            line):
                break
        if sw:
            with open(filename + ".wfn", "w") as o:
                o.write(line)
    if not sw:
        print "There is no AIM data in " + filename
