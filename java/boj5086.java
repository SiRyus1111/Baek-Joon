import java.io.*;
public class boj5086{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int a,b;
        String l;
        while (!(l = br.readLine()).equals("0 0")) { 
            String[] k = l.split(" ");
            a = Integer.parseInt(k[0]);
            b = Integer.parseInt(k[1]);
            if(a%b==0){
                sb.append("multiple\n");
            }
            else if(b%a==0){
                sb.append("factor\n");
            }
            else{
                sb.append("neither\n");
            }
        }
        System.out.print(sb);
    }
}