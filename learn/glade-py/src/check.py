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
		parser.check(s, p)
		#print("Valid input: " + s)
		return True

	except Exception as e:
		#print("Invalid input. \n")
		#print("Invalid input: " + s)
		#print("Error: "+str(e))
		return False
