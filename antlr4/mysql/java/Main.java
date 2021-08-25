import org.antlr.v4.runtime.ANTLRFileStream;
import org.antlr.v4.runtime.CommonTokenStream;
import org.antlr.v4.runtime.tree.ParseTree;

public class Main {
    public static void main(String[] args) throws Exception {
        MySqlLexer lexer = new MySqlLexer(new ANTLRFileStream("input"));
        MySqlParser parser = new MySqlParser(new CommonTokenStream(lexer));
        ParseTree tree = parser.root();
    }
}
