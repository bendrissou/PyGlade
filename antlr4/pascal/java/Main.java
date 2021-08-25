import org.antlr.v4.runtime.ANTLRFileStream;
import org.antlr.v4.runtime.CommonTokenStream;
import org.antlr.v4.runtime.tree.ParseTree;

public class Main {
    public static void main(String[] args) throws Exception {
        pascalLexer lexer = new pascalLexer(new ANTLRFileStream("input"));
        pascalParser parser = new pascalParser(new CommonTokenStream(lexer));
        ParseTree tree = parser.program();
    }
}
