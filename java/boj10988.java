import java.io.*;
import java.util.Scanner;
public class boj10988 {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        String reverse = "";
        for(int i=str.length()-1;i>=0;i--){
            reverse = reverse+str.charAt(i);
        }
        if(str.equals(reverse)){
            System.out.println(1);
        }
        else{
            System.out.println(0);
        }
    }
}
