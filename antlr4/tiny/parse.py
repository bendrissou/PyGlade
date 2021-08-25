import sys
from antlr4 import *
from tinyLexer import tinyLexer
from tinyParser import tinyParser
from MyErrorListener import MyErrorListener
import io

def main(argv):
    input = FileStream(argv[1], encoding = 'utf8')
    lexer = tinyLexer(input)
    lexer.removeErrorListeners()
    lexer.addErrorListener(MyErrorListener())  
    stream = CommonTokenStream(lexer)
    parser = tinyParser(stream)
    #error = io.StringIO()
    #print(error.read())
    #parser.removeErrorListeners()        
    #errorListener = ExprErrorListener(error)
    #parser.removeErrorListeners()
    #parser.addErrorListener(ExprErrorListener())  

    try:
        tree = parser.program()
        pass
    except SyntaxError:
        print("\n ++++++ Syntax Error ++++++ \n")
    except Exception as e:
        print("Error is: " + str(e))
        print("\n ++++++ Other Error ++++++ \n")

if __name__ == '__main__':
    main(sys.argv)
