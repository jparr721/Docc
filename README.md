# Docc
```
Dem doccs doe
  - Said no one ever, python docs suck
```

Use this, it is better than other garbage, why? Because it's simple, and it WORKS out of the box.

## Usage:
```
usage: docc.py [-h] [--dir DIR] [--excludes EXCLUDES] {fuckyou,fu} ...

Doc generators are shit, use this, it isn't.

positional arguments:
  {fuckyou,fu}
    fuckyou (fu)       No

optional arguments:
  -h, --help           show this help message and exit
  --dir DIR            If you need to specify a spicy dir
  --excludes EXCLUDES  do,it,like,this,it,can,be,a,dir,or,a,file
```

I'll add a setup.py file eventually, for now, here's an example:

```
python3 docc.py --dir Cuttlefish/ --excludes .git,venv,updater.py,dist,cuttlefish_lib.egg-info,test
```
