import java.io.*;
import java.util.*;
public class boj1026 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String[] a = new String[n];
        String[] b = new String[n];
        int[] a1 = new int[n];
        int[] b1 = new int[n];
        a = br.readLine().split(" ");
        b = br.readLine().split(" ");
        for(int i=0;i<n;i++){
            a1[i] = Integer.parseInt(a[i]);
            b1[i] = Integer.parseInt(b[i]);
        }
        Arrays.sort(a1);
        Arrays.sort(b1);
        int total = 0;
        for(int i=0;i<n;i++){
            total+=(a1[i]*b1[n-(i+1)]);
        }
        System.out.println(total);
    }
}
