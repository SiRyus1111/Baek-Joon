import java.io.*;
public class boj11726_2 {
    static int[] arr;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        arr = new int[Math.max(3,n+1)];
        arr[1]=1;
        arr[2]=2;
        System.out.println(shape(n));
    }
    static int shape(int n){
        if(n==1){
            return 1;
        }
        if(n==2){
            return 2;
        }
        if(arr[n]!=0){
            return arr[n];
        }
        arr[n] = (shape(n-1)+shape(n-2))%10007;
        return arr[n];
    }
}
