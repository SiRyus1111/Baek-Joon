import java.io.*;

public class boj1009 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        
        for (int i = 0; i < n; i++) {
            String[] arr = br.readLine().split(" ");
            int a = Integer.parseInt(arr[0]);
            int b = Integer.parseInt(arr[1]);
            
            b = b % 4 == 0 ? 4 : b % 4;
            int result = (int) Math.pow(a, b) % 10;
            
            sb.append(result == 0 ? 10 : result).append("\n");
        }
        System.out.print(sb);
    }
}

