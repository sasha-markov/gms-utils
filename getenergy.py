#!/usr/bin/python

import re


def get_total_energy(logfile):
    with open(logfile, 'r') as f:
        ss = re.findall(r'                       TOTAL ENERGY =\s+-\d+.\d+',
                        f.read())
        s = ss[-1].split()
    return eval(s[3])
