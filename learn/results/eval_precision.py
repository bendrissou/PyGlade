import sys
import glob
import json
sys.path.append("../")
import sampler
import earley_parser as parser
import subprocess

def parse_antlr(g):

    program_path = '../../antlr4/' + g
    path_sinputs = '../samples/synthesized/' + g + '/*'   
    files = glob.glob(path_sinputs)   

    s_parsed = 0
    i = 0
    for name in files: # 'file' is a builtin type, 'name' is a less-ambiguous variable name.
        i += 1
        batcmd="python3 " + program_path + "/parse.py " + name
        result = subprocess.check_output(batcmd, shell=True, stderr=subprocess.STDOUT)
        out = result.decode('utf-8')

        if out == '': 
            s_parsed += 1


    precision = s_parsed/i
    print("precision: " + str(precision))

    precision_score = "Precision for " + g + " is: " + str(s_parsed) + " / " + str(i)

    results =  precision_score + "\n"

    file2 = open('eval_%s_precision.txt' % g, 'w')
    file2.write(results)
    file2.close()

def parse(g):
    # reading the grammar from the file
    with open('../handwritten/%s.json' % g) as f:
        data = f.read()
    h_grammar = json.loads(data)
    

    # reading sample inputs
    path = '../samples/synthesized/' + g + '/*'   
    files = glob.glob(path)   
    inputs = []
    for name in files:
        nfin = open(name, "rt")
        input = nfin.read().strip()
        inputs.append(input)
        
    s_parsed = 0
    i = 0
    for input in inputs:
        try:
            i += 1
            ee = parser.EarleyParser(h_grammar).recognize_on(input, parser.START)
            s_parsed += 1
        except SyntaxError:
            pass

    precision = s_parsed/i
    print("precision: " + str(precision))

    precision_score = "Precision for " + g + " is: " + str(s_parsed) + " / " + str(i)

    results =  precision_score + "\n"

    file2 = open('eval_%s_precision.txt' % g, 'w')
    file2.write(results)
    file2.close()


if __name__ == '__main__':
    import sys
    program = sys.argv[1]
    antlr_programs = ['xpath', 'lua', 'pascal', 'mysql', 'c', 'tinyc', 'tiny', 'basic']
    if program in antlr_programs:
        parse_antlr(program)
    else:
        parse(program)
