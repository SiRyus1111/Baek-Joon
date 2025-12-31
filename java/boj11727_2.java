import java.io.*;
public class boj11727_2 {
    static int[] dp; 
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        dp = new int[Math.max(3,n+1)];
        dp[1] = 1;
        dp[2] = 3;
        System.out.println(tile(n));
    }
    static int tile(int n){
        if(n==1){
            return 1;
        }
        if(n==2){
            return 3;
        }
        if(dp[n]!=0){
            return dp[n];
        }
        dp[n] = (tile(n-1) + tile(n-2)*2)%10007;
        return dp[n];
    }
}
