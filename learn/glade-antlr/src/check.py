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
        #print("Input already tested.")
        return exec_map[s]
    v =  _check(s, p)
    #print("\t\t", repr(s), v, ' from: %s' % str(label))
    exec_map[s] = v
    return v

# This is the oracle. For now, we simply use a regex matcher
# but you can replace it with any context free oracle. Return
# True if your oracle agrees with the input.
import re
def _check(s, p):
	try:
		# writing to file
		file1 = open('input', 'w')
		#file1 = open('../../../antlr4/' + p + '/java/input', 'w')
		file1.write(s)
		file1.close()
		#result = subprocess.call(get_command(p), timeout=3, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
		result = subprocess.check_output(get_command(p), shell=True, stderr=subprocess.STDOUT, timeout=10)
		output = result.decode('utf-8')
		#print("output: " + output)
		if output == '': 
			#print("Valid Input")
			return True
		else:
			#print("Invalid Input")
			return False
	except Exception as e:
		print("Error: "+str(e))
		return False

def get_command(p):
    #cmd = ['python3', '../../../antlr4/' + p + '/parse.py', 'input']
    cmd = 'python3 ../../../antlr4/' + p + '/parse.py input'
    #cmd = 'cd ../../../antlr4/' + p + '/java && java -cp .:/usr/local/lib/antlr-4.9.2-complete.jar Main'
    #cmd = 'java -cp .:/usr/local/lib/antlr-4.9.2-complete.jar ../../../antlr4/' + p + '/java/Main'
    return cmd

