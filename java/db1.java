import java.io.*;
public class db1 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] str = br.readLine().split(" ");
        int n = Integer.parseInt(str[0]);
        int k = Integer.parseInt(str[1]);
        int count = 0;
        while(n>1){
            if(n%k==0){
                n = n/k;
                count += 1;
            }
            else{
                n-=1;
                count += 1;
            }
        }
        System.out.println(count);
    }
}
