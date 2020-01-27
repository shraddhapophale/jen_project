#!/usr/bin/python

import subprocess
list_files = subprocess.run(["ansible-playbook", "abc.yml", "-K"])
print("The exit code was: %d" % list_files.returncode)
if list_files.returncode==0:
	print("Successful...")
else:
	print("Something goes Wrong....")
