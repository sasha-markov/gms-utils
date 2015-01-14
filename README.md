## getwfn.py
The script for exporting [AIM](http://www.chemistry.mcmaster.ca/aim/) data from [GAMESS-US](http://www.msg.ameslab.gov/gamess/) `dat` file.
### Usage
In order to generate AIM data in GAMESS calculations you must use `AIMPAC=.TRUE.` flag in $contrl group.
Then in command line:

```
getwfn.py -f _filename.dat_

```
If successful `filename.wfn` will appear in the same folder as `filename.dat` file.