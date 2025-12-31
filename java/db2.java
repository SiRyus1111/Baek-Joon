import java.io.*;
public class db2 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] str = br.readLine().split("");
        int sum=0;
        for(int i=0;i<str.length;i++){
            int num = Integer.parseInt(str[i]);
            sum = (num<=1 || sum<=1)?sum+num:sum*num;
        }
        System.out.println(sum);
    }
}
