import java.io.*;
import java.util.*;

public class boj2217 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] ropes = new int[n];
        for (int i = 0; i < n; i++) {
            ropes[i] = Integer.parseInt(br.readLine());
        }

        Arrays.sort(ropes); // 오름차순 정렬

        int max = 0;
        for (int i = 0; i < n; i++) {
            int weight = ropes[i] * (n - i);
            if (weight > max){
                max = weight;
            }
        }
        System.out.println(max);
    }
}

