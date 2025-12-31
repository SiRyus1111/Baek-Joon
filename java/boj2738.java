import java.io.*;
public class boj2738 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        String s2[] = s.split(" ");
        int n = Integer.parseInt(s2[0]);
        int m = Integer.parseInt(s2[1]);
        int[][] a = new int[n][m];
        int[][] b = new int[n][m];
        for(int i=0;i<n;i++){
            String s3 = br.readLine();
            String[] s4 = s3.split(" ");
            for(int j=0;j<m;j++){
                a[i][j] = Integer.parseInt(s4[j]);
            }
        }
        for(int i=0;i<n;i++){
            String s3 = br.readLine();
            String[] s4 = s3.split(" ");
            for(int j=0;j<m;j++){
                b[i][j] = Integer.parseInt(s4[j]);
            }
        }
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                a[i][j] = a[i][j] + b[i][j];
            }
            for(int j=0;j<m;j++){
                System.out.print(a[i][j]+" ");
            }
            System.out.println();
        }
    }
}
