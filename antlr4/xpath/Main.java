import org.antlr.v4.runtime.ANTLRFileStream;
import org.antlr.v4.runtime.CommonTokenStream;
import org.antlr.v4.runtime.tree.ParseTree;

public class Main {
    public static void main(String[] args) throws Exception {
        xpathLexer lexer = new xpathLexer(new ANTLRFileStream("input"));
        xpathParser parser = new xpathParser(new CommonTokenStream(lexer));
        ParseTree tree = parser.main();
    }
}
