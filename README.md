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
Contains functions that (1) returns the last value of the total energy and
(2) returns the value of the zero-point energy in a given GAMESS logfile.
### Usage

```
import getenergy
getenergy.get_total_energy('/path/to/file.log')
getenergy.getzpe('/path/to/file.log')
```
