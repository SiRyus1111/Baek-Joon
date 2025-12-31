import java.io.*;
public class boj2566 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = "";
        int[][] str3 = new int[9][9];
        int max = Integer.MIN_VALUE;
        int maxi = 0;
        int maxj = 0;
        for(int i=0;i<9;i++){
            str = br.readLine();
            String[] str2 = str.split(" ");
            for(int j=0;j<9;j++){
                str3[i][j] = Integer.parseInt(str2[j]);
                if(str3[i][j]>max){
                    max = str3[i][j];
                    maxi = i+1;
                    maxj = j+1;
                }
            }
        }
        System.out.println(max);
        System.out.println(maxi+" "+maxj);
    }
}
