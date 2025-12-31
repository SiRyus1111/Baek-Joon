import java.io.*;
public class boj1912 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String[] arr1 = br.readLine().split(" ");
        int[] arr = new int[n+1];
        int[] dp = new int[n+1];
        for(int i=0;i<n;i++){
            arr[i+1] = Integer.parseInt(arr1[i]);
        }
        dp[1] = arr[1];
        int max = dp[1];
        for(int i=2;i<=n;i++){
            dp[i] = Math.max(arr[i],dp[i-1]+arr[i]);
            max = Math.max(max,dp[i]);
        }
        System.out.println(max);
    }
}
