#!/usr/bin/python3

import subprocess

list_files = subprocess.run(["ansible-playbook", "/etc/ansible/abc.yml", "-K"])
print("The exit code was: %d" % list_files.returncode)
if list_files.returncode==0:
	print("Successful...")
else:
	print("Something goes Wrong....")
