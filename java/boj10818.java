import java.io.*;
public class boj10818 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String[] nums = br.readLine().split(" ");
        int max = Integer.MIN_VALUE;
        int min = Integer.MAX_VALUE;
        for(int i=0;i<n;i++){
            int num = Integer.parseInt(nums[i]);
            if(num>max){
                max = num;
            }
            if (num<min) {
                min = num;
            }
        }
        System.out.println(min+" "+max);
    }
}
