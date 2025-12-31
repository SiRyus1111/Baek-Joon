import java.io.*;
import java.util.Arrays;
public class boj11399 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String[] p = br.readLine().split(" ");
        int[] p2 = new int[n];
        for(int i=0;i<n;i++){
            p2[i] = Integer.parseInt(p[i]);
        }
        Arrays.sort(p2);
        int sum = 0;
        int temp = 0;
        for(int i=0;i<n;i++){
            temp += p2[i];
            sum+=temp;
        }
        System.out.println(sum);
    }
}
