import re
import glob
import os

def main():

    path = 'generate/random/*.ex'   
    files = glob.glob(path)   
    seen = set()
    i = 0
    for name in files: # 'file' is a builtin type, 'name' is a less-ambiguous variable name.
        i += 1
        new_file = 'generate/random/input_' + str(i) + '.cm'
        fin = open(name, "rt")
        fout = open(new_file, "wt")

        for line in fin:
            fout.write(re.sub('\s+',' ',line))
            #fout.write(re.sub('[\s]{2,}','  ',line))

        fin.close()
        fout.close()

        os.remove(name)



if __name__ == '__main__':
    main()
