package parser;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;
import java.io.FileWriter; 
/**
 * Earley Parser
 *
 */
public class App {
    public static void main(String[] args) {
        ParserLib pl;
        try {
            long startTime = System.currentTimeMillis();
            String program = args[0];
            int part = Integer.parseInt(args[1]);
            String grammar = "../synthesized/" + program + ".json";
            pl = new ParserLib(grammar);
            //ParseTree result = pl.parse_text(args[1], pl.start_symbol);
            System.out.println("Grammar read");
            String samples_path = "../samples/handwritten/" + program;
            //String path = "EarleyParser/myfile.json";
            int start = part * 100 - 99;
            int end = part * 100;
            int total = 100;
            int valid = 0;
            for (int i = start; i <= end; i++) {

              String filePath = samples_path + "/input_" + i + ".in";
              String content = new String (Files.readAllBytes(Paths.get(filePath)));
              System.out.println(filePath);
              System.out.println(content);
              try {
                  pl.parse_text(filePath, pl.start_symbol);
                  System.out.println("Valid input");
                  valid += 1;
              } catch (ParseException e) {
                  System.out.println("SyntaxError: " + e);
              } catch (NullPointerException e) {
                  System.out.println("NullPointerException here!.");
              }

            }

            long estimatedTime = System.currentTimeMillis() - startTime;
            System.out.println("Elapsed time: " + estimatedTime/1000);
            String recall = valid + " / " + total;
            String result = "Recall of part " + part + ": " + recall + "\n";
            System.out.println(result);
            FileWriter myWriter = new FileWriter("../results/eval_" + program + "_recall.txt" , true);
            myWriter.write(result);
            myWriter.close();

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
