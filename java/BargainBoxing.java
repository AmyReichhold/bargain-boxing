/*
import java.io.BufferedReader;
import java.io.FileReader;

import java.io.File;  // Import the File class
import java.io.FileNotFoundException;  // Import this class to handle errors
import java.util.Scanner; // Import the Scanner class to read text files
*/

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class BargainBoxing {
    public static void main(String[] args) {

        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

        //InputStreamReader cin = new InputStreamReader(System.in);

        try {
            String line = in.readLine();
            while (line != null) {
                System.out.println(line);
                line = in.readLine();
            }
        } catch (IOException e) {
          System.out.println("An error occurred.");
          e.printStackTrace();
        }
        
        /* How to open and read a file from the command line.
        try {
            if (args.length > 0) {
                File myObj = new File(args[0]);
                System.out.println(myObj); 
            }
            
            File myObj = new File(args[0]);
            Scanner myReader = new Scanner(myObj);
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                System.out.println(data);
            }
            myReader.close();
        } catch (FileNotFoundException e) {
          System.out.println("An error occurred.");
          e.printStackTrace();
        }
        */
    }
}
