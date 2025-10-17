import java.io.*;
public class boj2579 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int scores[] = new int[n+1];
        int arr[] = new int[n+1];
        for(int i=1;i<=n;i++){
            scores[i] = Integer.parseInt(br.readLine());
        }
        arr[1] = scores[1];
        if(n>=2){
            arr[2] = scores[1] + scores[2];
        }
        if(n>=3){
            arr[3] = Math.max(scores[1],scores[2])+scores[3];
        }
        for(int i=4;i<=n;i++){
            arr[i] = Math.max(arr[n-2],arr[n-3]+scores[n-1]) + scores[i];
        }
        System.out.println(arr[n]);
    }
}
