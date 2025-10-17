import java.io.*;
public class boj9095_2 {
    static int[] arr = new int[11];
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int t = Integer.parseInt(br.readLine());
        int[] num = new int[t];
        for(int i=0;i<t;i++){
            num[i] = Integer.parseInt(br.readLine());
        }
        arr[1] = 1;
        arr[2] = 2;
        arr[3] = 4;
        ott(10);
        for(int i=0;i<t;i++){
            sb.append(arr[num[i]]).append('\n');
        }
        System.out.print(sb);
    }
    static int ott(int n){
        if(n==1){
            return 1;
        }
        if(n==2){
            return 2;
        }
        if(n==3){
            return 4;
        }
        if(arr[n]!=0){
            return arr[n];
        }
        arr[n] = ott(n-1) + ott(n-2) + ott(n-3);
        return arr[n];
    }
}
