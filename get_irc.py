#!/usr/bin/python

import re
import numpy as np
import getenergy


def get_irc_energy(logfile):
    with open(logfile, 'r') as f:
        a = []
        b = []
        x = re.findall(r'          AT PATH DISTANCE STOTAL = \s+\d+.\d+',
                       f.read())
        f.seek(0)
        e = re.findall(r'          TOTAL ENERGY            =\s*-\d+.\d+',
                       f.read())
        for item in x:
            m = item.split()
            a.append(m[5])
        for item in e:
            n = item.split('=')
            b.append(n[1])
    return a, b


def ircjoin(l, r, ts):
    xl, el = get_irc_energy(l)
    xr, er = get_irc_energy(r)
    xl.reverse()
    el.reverse()
    xr.insert(0, 0)
    er.insert(0, getenergy.get_total_energy(ts))

    def invert(a):
        return float(a) * (-1)

    xl = map(invert, xl)

    def cfloat(a):
        return float(a)

    xr = map(cfloat, xr)

    xl.extend(xr)
    el.extend(er)
    el = np.array(el, dtype=np.float)
    xl = np.array(xl, dtype=np.float)
    return xl, el


def get_irc_geom(logfile, atoms):
    with open(logfile, 'r') as f:
        sw = False
        geom = []
        if len(atoms) == 2:
            pat2 = re.compile(r"""
                             \s*\d{1,2}\s*STRETCH\s*\d{1,2}\s*\d{1,2}
                             \s*\d+.\d+\s*\d+.\d+
                             """, re.VERBOSE)
        if len(atoms) == 3:
            pat3 = re.compile(r"""
                             \s*\d{1,2}\s*BEND\s*\d{1,2}\s*\d{1,2}\s*\d{1,2}
                             \s*\d+.\d+\s*\d+.\d+
                             """, re.VERBOSE)
        if len(atoms) == 4:
            pat4 = re.compile(r"""
                             \s*\d{1,2,3}\s*TORSION
                             \s*\d{1,2}\s*\d{1,2}\s*\d{1,2}\s*\d{1,2}
                             \s*-?\d+.\d+\s*-?\d+.\d+
                             """, re.VERBOSE)
        for line in f:
            if ('                     INTERNAL COORDINATES') in line:
                sw = True
                continue
            if sw:
                if (len(atoms) == 2) and (pat2.match(line)):
                        (no, string, a1, a2, v1, v2) = line.split()
                        if (a1 == str(atoms[0])) and (a2 == str(atoms[1])):
                            geom.append(eval(v2))
                            sw = False
                if (len(atoms) == 3) and (pat3.match(line)):
                        (no, string, a1, a2, a3, v1, v2) = line.split()
                        if (a1 == str(atoms[0])) and (a2 == str(atoms[1])) and \
                           (a3 == str(atoms[2])):
                            geom.append(eval(v2))
                            sw = False
                if (len(atoms) == 4) and (pat4.match(line)):
                        (no, string, a1, a2, a3, a4, v1, v2) = line.split()
                        if (a1 == str(atoms[0])) and (a2 == str(atoms[1])) and \
                           (a3 == str(atoms[2])) and (a4 == str(atoms[3])):
                            geom.append(eval(v2))
                            sw = False

            if ('     ------------------------------------------') in line:
                sw = False
    return geom
