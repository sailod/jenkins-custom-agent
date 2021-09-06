
from pathlib import Path
import os, subprocess, sys

files = ["a", "b", "c", "d"]

for x in files:
    f = open("{}.txt".format(x), "a")
    f.write("Now the file has more content!")
    f.close()
    try:
        file = open("{}.txt".format(x), 'r')
    except IOError:
        print('There was an error opening the file!')
        sys.exit(1)

for x in files:
    subprocess.call("zip {}_{}.zip {}.txt".format(x,os.environ['VERSION'],x), shell=True)  # returns the exit code in unix
    my_file = Path("./{}_{}.zip".format(x,os.environ['VERSION']))
    if not my_file.is_file():
        sys.exit(1)
