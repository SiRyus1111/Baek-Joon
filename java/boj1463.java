import java.io.*;
public class boj1463 {
    static int[] arr;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        arr = new int[n+1];
        arr[1] = 0;
        System.out.println(one(n));
    }
    static int one(int n){
        if(n==1){
            return 0;
        }
        if(arr[n]!=0){
            return arr[n];
        }
        arr[n] = one(n-1)+1;
        if(n%3==0){
            arr[n] = Math.min(arr[n],one(n/3)+1);
        }
        if(n%2==0){
            arr[n] = Math.min(arr[n],one(n/2)+1);
        }
        return arr[n];
    }
}
