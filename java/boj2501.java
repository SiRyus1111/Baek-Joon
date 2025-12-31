import java.io.*;
public class boj2501{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        String[] str = br.readLine().split(" ");
        int n = Integer.parseInt(str[0]);
        int k = Integer.parseInt(str[1]);
        String[] yaksu = new String[n];
        for(int i=1;i<=n;i++){
            if(n%i==0){
                sb.append(i).append(" ");
            }
        }
        yaksu = sb.toString().split(" ");
        if(k<=yaksu.length){
            System.out.println(Integer.parseInt(yaksu[k-1]));
        }
        else{
            System.out.println(0);
        }
    }
}