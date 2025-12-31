import java.io.*;
public class boj2869 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] num = br.readLine().split(" ");
        int a = Integer.parseInt(num[0]);
        int b = Integer.parseInt(num[1]);
        int v = Integer.parseInt(num[2]);
        int days = (v-a)/(a-b);
        if((v-a)%(a-b)!=0){
            days++;
        }
        days++;
        System.out.println(days);
    }
}
