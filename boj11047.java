import java.io.*;
public class boj11047 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] str = br.readLine().split(" ");
        int n = Integer.parseInt(str[0]);
        int k = Integer.parseInt(str[1]);
        int[] coin = new int[n];
        int sum = 0;
        for(int i=0;i<n;i++){
            coin[i] = Integer.parseInt(br.readLine());
        }
        for(int i=n-1;i>=0;i--){
            if(k>=coin[i]){
                sum += k/coin[i];
                k = k%coin[i];
            }
        }
        System.out.println(sum);
    }
}
