import java.io.*;
public class boj1003 {
    static int[] sum = new int[2];
    static int[][] dp = new int[41][2];
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int t = Integer.parseInt(br.readLine());
        int n;
        dp[0][0] = 1;
        dp[0][1] = 0;
        dp[1][0] = 0;
        dp[1][1] = 1;
        fibo(40);
        for(int i=0;i<t;i++){
            n = Integer.parseInt(br.readLine());
            sb.append(dp[n][0]).append(" ").append(dp[n][1]).append('\n');
        }
        System.out.print(sb);
    }
    static int[] fibo(int n){
        if(dp[n][0]!=0||dp[n][1]!=0||n==0||n==1){
            return dp[n];
        }
        int[] a = fibo(n-1);
        int[] b = fibo(n-2);
        dp[n][0] = a[0] + b[0];
        dp[n][1] = a[1] + b[1];
        return dp[n];
    }
}
