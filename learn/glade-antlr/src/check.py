import sys, imp
import subprocess
import os
import sys
import xml.etree.ElementTree as ET

sys.path.append("../..")

import earley_parser as parser

exec_map = {}
def check(s, p, label=None):
    if s in exec_map: 
        # Input already tested.
        return exec_map[s]
    v =  _check(s, p)
    exec_map[s] = v
    return v

import re
def _check(s, p):
	try:
		file1 = open('input', 'w')
		file1.write(s)
		file1.close()
		result = subprocess.check_output(get_command(p), shell=True, stderr=subprocess.STDOUT, timeout=10)
		output = result.decode('utf-8')
		if output == '': 
			return True
		else:
			return False
	except Exception as e:
		print("Error: "+str(e))
		return False

def get_command(p):
    cmd = 'python3 ../../../antlr4/' + p + '/parse.py input'
    return cmd

