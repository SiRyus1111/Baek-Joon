import java.io.*;
public class boj2193_2 {
    static long[][] dp;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        dp[1][0] = 0;
        dp[1][1] = 1;
        System.out.println(kkk(n,0)+kkk(n,1));
    }
    static long kkk(int n,int k){
        if(n==1){
            if(k==0){
                return 0;
            }
            return 1;
        }
        if(dp[n][k]!=0){
            return dp[n][k];
        }
        if(k==0){
            dp[n][0] = kkk(n-1,0) + kkk(n-1,1);
            return dp[n][0];
        }
        else{
            dp[n][1] = kkk(n-1,0);
            return dp[n][1];
        }
    }
}
