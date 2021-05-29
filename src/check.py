import sys, imp
import subprocess
import os
import xml.etree.ElementTree as ET

exec_map = {}
def check(s, label=None):
    if s in exec_map: 
        return exec_map[s]
    v =  _check(s)
    exec_map[s] = v
    return v

# This is the oracle. Here, we use a xml parser
# but you can replace it with any context free oracle. Return
# True if your oracle agrees with the input.
import re
def _check(s):
	try:
		ET.fromstring(s)
		return True

	except Exception as e:
		return False
