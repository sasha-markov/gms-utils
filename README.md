# Simple functions for working with GANESS-US output files

## getenergy.py
Contains following functions with the path to [GAMESS-US](http://www.msg.ameslab.gov/gamess/)
logfile as an argument:
+ `get_total_energy` returns the last value of total energy (in
hartree) in a given logfile
+ `get_total_energies` returns a list of total energies (in hartree)
  computed in the course of optimization procedure or PES scan from a
  given logfile
+ `get_zpe` returns a value of zero-point energy (in kcal/mol)
+ `get_thermochem` returns a list [Hc, Gc, Sc] where Hc, Gc, Sc are
thermal corrections to thermodynamical functions H, G, S (in kcal/mol)
+ `get_mo_energies` returns a list of molecular orbitals energies
  (in hartree) for RHF calculation or two lists, alpha and beta, for
  UHF calculation
+ `get_sol_free_energy` returns a value of total free energy in solvent (in
hartree) for PCM calculation.

### Usage

```
import getenergy
getenergy.get_total_energy('/path/to/file.log')
```

## get_irc.py
Contains following functions:
+ `get_irc_energy(logfile)` returns two lists, the IRC path coordinates, and
corresponding total energies from a given logfile
+ `ircjoin(l, r, ts)` returns two numpy arrays, x (IRC path
  coordinate) and y (energy), combined left and right parts of the IRC
  bell-like curve ready to plotting in matplotlib. As arguments the
  function takes three logfiles -- transition state, left and right
  parts of IRC curve

### Usage

```
%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np

import get_irc


l = '/path/to/left.log'
r = '/path/to/right.log'
ts = '/path/to/ts.log'
x, y = get_irc.ircjoin(l, r, ts)
plt.plot(x, y, 'k.')
```

## getwfn.py
The script for exporting [AIM](http://www.chemistry.mcmaster.ca/aim/)
data from [GAMESS-US](http://www.msg.ameslab.gov/gamess/) `dat` file.
### Usage
For generating AIM data in GAMESS calculation add
`AIMPAC=.TRUE.` flag to $contrl group.
Then in command line:

```
getwfn.py -f somefile.dat
```
If successful, `somefile.wfn` will appear in the same folder as `somefile.dat` file.

