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


def get_thermochem(logfile):
    with open(logfile, 'r') as f:
        pat = re.compile(r"""
                          TOTAL
                         \s+\d+.\d+
                         \s+\d+.\d+
                         \s+\D\d+.\d+
                         \s+\d+.\d+
                         \s+\d+.\d+
                         \s+\d+.\d+
                         """, re.VERBOSE)
        ss = re.findall(pat, f.read())
        s = ss[-1].split()
        H, G, S = s[2], s[3], s[-1]
    return eval(H), eval(G), eval(S)


def get_mo_energies(logfile):
    with open(logfile, 'r') as f:
        swa = False
        swb = False
        swc = False
        swd = False
        pat = re.compile(r"""
                        \s*
                        -?\d+\.\d+
                    """, re.VERBOSE)
        eigveca = []
        eigvecb = []
        mosalpha = []
        mosbeta = []
        for line in f:
            if (('          EIGENVECTORS') in line) and not swb:
                swa = True
                continue
            if swa:
                if pat.match(line):
                    for i in line.split():
                        eigveca.append(eval(i))
                if re.match(r'  ----- BETA SET ----- ', line):
                    swa = False
                    swb = True
            if swb:
                if pat.match(line):
                    for i in line.split():
                        eigvecb.append(eval(i))
            if re.match(r' ...... END OF (U|R)HF CALCULATION ......', line):
                swa = False
                swb = False
            if ('          MOLECULAR ORBITALS') in line:
                swc = True
                continue
            if swc:
                if pat.match(line):
                    for i in line.split():
                        mosalpha.append(eval(i))
                if ('          **** BETA SET ****') in line:
                    swc = False
                    swd = True
            if swd:
                if pat.match(line):
                    for i in line.split():
                        mosbeta.append(eval(i))
            if ('     PROPERTIES FOR THE') in line:
                swc = False
                swd = False
    return eigveca, eigvecb, mosalpha, mosbeta


def get_sol_free_energy(logfile):
    with open(logfile, 'r') as f:
        s = re.search(r' TOTAL FREE ENERGY IN SOLVENT\s+=\s+-\d+.\d+',
                          f.read())
        s = s.group(0).split()        
    return eval(s[6])

