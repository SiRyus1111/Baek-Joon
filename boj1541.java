import java.io.*;
public class boj1541 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] str = br.readLine().split("-");
        int sum = 0;
        //첫번째 항
        String[] first = str[0].split("\\+");
        for(String num:first){
            sum+=Integer.parseInt(num);
        }
        //두번째 이후 항
        for(int i=1;i<str.length;i++){
            String[] next = str[i].split("\\+");
            int temp = 0;
            for(String num:next){
                temp+=Integer.parseInt(num);
            }
            sum-=temp;
        }
        System.out.print(sum);
    }
}
