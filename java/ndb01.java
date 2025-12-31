import java.io.*;
public class ndb01 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] str = br.readLine().split(" ");
        int n = Integer.parseInt(str[0]);
        int k = Integer.parseInt(str[1]);
        int count = 0;
        while (true){
            int target = (n/k)*k;
            count += (n-target);
            n = target;
            if(n<k){
                break;
            }
            count+=1;
            n/=k;
        }
        count-=1;
        System.out.println(count);
    }
}
