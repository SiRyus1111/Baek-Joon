import java.io.*;
public class boj2446{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        for(int k=0;k<n;k++){
            for(int j=0;j<k;j++){
                System.out.print(" ");
            }
            for(int i=0;i<(2*n-1)-(k*2);i++){
                System.out.print("*");
            }
            System.out.println();
        }
        for(int k=0;k<n-1;k++){
            for(int j=1;j<(n-1)-k;j++){
                System.out.print(" ");
            }
            for(int i=0;i<3+(2*k);i++){
                System.out.print("*");
            }
            System.out.println();
        }
    }
}