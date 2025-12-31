import java.io.*;
public class boj2748_4 {
    static long[] arr;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        arr = new long[n+1];
        for(int i=0;i<=n;i++){
            arr[i] = -1;
        }
        arr[0] = 0;
        arr[1] = 1;
        System.out.println(fibo(n));
    }
    static long fibo(int n){
        if(n==0){
            return 0;
        }
        if(n==1){
            return 1;
        }
        if(arr[n]!=-1){
            return arr[n];
        }
        arr[n] = fibo(n-1) + fibo(n-2);
        return arr[n];
    }
}
