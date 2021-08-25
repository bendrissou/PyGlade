import re
import glob
import subprocess
import os
def main():

    path = 'generate/random/*'   
    files = glob.glob(path)   
    for name in files: # 'file' is a builtin type, 'name' is a less-ambiguous variable name.
        #fin = open("test_13.ex.s", "rt")

        batcmd="python3 parse.py " + name
        result = subprocess.check_output(batcmd, shell=True, stderr=subprocess.STDOUT)
        out = result.decode('utf-8')

        if out != '': 
            #print("\nError: " + out)
            print("File: " + name)
            os.remove(name)
        #print("Result: " + out)
        #fin.close()


if __name__ == '__main__':
    main()
