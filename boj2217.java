import java.io.*;
import java.util.Arrays;
public class boj2217 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] ropes = new int[n];
        for(int i=0;i<n;i++){
            ropes[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(ropes);
        System.out.println(ropes[0]*n);
    }
}
