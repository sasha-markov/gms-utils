## getwfn.py
The script for exporting [AIM](http://www.chemistry.mcmaster.ca/aim/)
data from [GAMESS-US](http://www.msg.ameslab.gov/gamess/) `dat` file.
### Usage
In order to generate AIM data in GAMESS calculations you must use
`AIMPAC=.TRUE.` flag in $contrl group.
Then in command line:

```
getwfn.py -f somefile.dat
```
If successful, `somefile.wfn` will appear in the same folder as `somefile.dat` file.

## getenergy.py
Contains following functions with path to GAMESS logfile as an argument:
+ `get_total_energy` returns a last value of total energy (in
   hartree) in a given logfile
+ `getzpe` returns value of the zero-point energy (in kcal/mol)
+ `get_thermochem` returns list (Hc, Gc, Sc) where Hc, Gc, Sc are
thermal corrections to thermodynamical functions H, G, S
+ `get_mo_energies` returns one list of molecular orbitals energies
  (in hartree) for RHF calculation or two lists, alpha and beta, for
  UHF calculation
+ `get_sol_free_energy` returns value of total free energy (in
  hartree) in solvent for PCM calculatio.
### Usage

```
import getenergy
getenergy.get_total_energy('/path/to/file.log')
getenergy.getzpe('/path/to/file.log')
```
