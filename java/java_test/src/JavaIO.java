/**
 * Created by Taikor on 6/24/2015.
 */
import java.io.*;

public class JavaIO {
    public static void main(String args[]) throws IOException
    {

        String file = "C:\\workspace\\Github_MasterRepository\\miscellaneous\\java\\java_test\\src\\input.txt";
        BufferedReader br = new BufferedReader(new FileReader(file));

        String text = "";
        String text_buffer;
        while ((text_buffer = br.readLine()) != null)
        {
            text = text + text_buffer;
            text = text + "\n";
        }
        System.out.println(text);

    }
}