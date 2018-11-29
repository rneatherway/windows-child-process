#!/usr/bin/python

import subprocess
import sys

print("Launching child")
proc = subprocess.Popen(["python", "loop.py"], stdout=sys.stdout, stderr=sys.stderr)
return_code = proc.wait()
