import java.io.*;
public class boj2720 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        int[][] result = new int[t][4];
        for(int i=0;i<t;i++){
            int c = Integer.parseInt(br.readLine());
            result[i][0]=c/25;
            result[i][1]=c%25;
            int c2 = result[i][1];
            result[i][1]=c2/10;
            result[i][2]=c2%10;
            int c3 = result[i][2];
            result[i][2]=c3/5;
            result[i][3]=c3%5;
        }
        for(int i=0;i<t;i++){
            System.out.println(result[i][0]+" "+result[i][1]+" "+result[i][2]+" "+result[i][3]);
            
        }     
    }
}
