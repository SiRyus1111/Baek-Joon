import java.io.*;
public class boj10798 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        char[][] word = new char[5][15];
        for(int i=0;i<5;i++){
            String str = br.readLine();
            for(int j=0; j<str.length(); j++){
                word[i][j] = str.charAt(j);
            }
        }
        for(int i=0;i<15;i++){
            for(int j=0;j<5;j++){
                if(word[j][i] !='\0'){
                    System.out.print(word[j][i]);
                }
            }
        }
    }
}
