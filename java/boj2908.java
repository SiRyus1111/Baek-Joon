import java.util.Scanner;
public class boj2908 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int a1 = a/100;
        int a2 = (a/10)%10;
        int a3 = a%10;
        int a_reversed = a3*100+a2*10+a1;
        int b1 = b/100;
        int b2 = (b/10)%10;
        int b3 = b%10;
        int b_reversed = b3*100+b2*10+b1;
        if(a3<b3){
            System.out.println(b_reversed);
        }
        else if(a3>b3){
            System.out.println(a_reversed);
        }
        else if(a2<b2){
            System.out.println(b_reversed);
        }
        else if(a2>b2){
            System.out.println(a_reversed);
        }
        else if(a1<b1){
            System.out.println(b_reversed);
        }
        else{
            System.out.println(a_reversed);
        }
        
    }
}
