import java.util.Scanner;
public class boj2675 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        for(int i=0;i<t;i++){
            int r = sc.nextInt();
            String s = sc.next();
            String[] str = new String[s.length()];
            str = s.split("");
            for(int j=0;j<s.length();j++){
                str[j] = str[j].repeat(r);
            }
            for(int k=0;k<s.length();k++){
                System.out.print(str[k]);
            }
            System.out.println();
        }
    }
}
