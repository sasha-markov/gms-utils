#!/usr/bin/python

import re


def get_total_energy(logfile):
    with open(logfile, 'r') as f:
        ss = re.findall(r'                       TOTAL ENERGY =\s+-\d+.\d+',
                        f.read())
        s = ss[-1].split()
    return eval(s[3])


def getzpe(logfile):
    with open(logfile, 'r') as f:
        sw = False
        i = 0
        for line in f:
            if (" THE HARMONIC ZERO POINT ENERGY IS") in line:
                sw = True
                continue
            if (i == 2):
                break
            if sw:
                s = line
                i = i + 1
                s = s.split()
        if not sw:
            print "There is no ZPE data in the file!"
    return eval(s[0])
