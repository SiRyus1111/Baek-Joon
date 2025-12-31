import java.util.Scanner;
public class boj25191 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int a = sc.nextInt();
        int b = sc.nextInt();
        a=a/2;
        int c = a+b;
        if(n>=c){
            System.out.println(c);
        }
        else if(n<c){
            System.out.println(n);
        }
    }
}
