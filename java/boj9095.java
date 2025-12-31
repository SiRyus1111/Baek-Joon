import java.io.*;
public class boj9095 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        int[] num  = new int[t];
        int[] arr = new int[11];
        for(int i=0;i<t;i++){
            num[i] = Integer.parseInt(br.readLine());
        }
        arr[1] = 1;
        arr[2] = 2;
        arr[3] = 4;
        for(int i=4;i<=10;i++){
            arr[i] = arr[i-1] + arr[i-2] + arr[i-3];
        }
        for(int i=0;i<t;i++){
            System.out.println(arr[num[i]]);
        }
    }
}