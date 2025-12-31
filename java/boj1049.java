import java.io.*;
public class boj1049 {
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] nm = br.readLine().split(" ");
        int n = Integer.parseInt(nm[0]);
        int m = Integer.parseInt(nm[1]);
        String[][] arr = new String[m][2];
        int min = Integer.MAX_VALUE;
        for(int i=0;i<m;i++){
            arr[i] = br.readLine().split(" ");
        }
        for(int i=0;i<m;i++){
            int a = Integer.parseInt(arr[i][0]);
            int b = Integer.parseInt(arr[i][1]);
            int pack = (n/6)+(n%6==0?0:1);
            int aa = a*pack;
            int minn = Math.min(aa,b*n);
            min = Math.min(minn,min);
        }
        System.out.println(min);
    }
}
