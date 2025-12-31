import java.util.Scanner;
public class boj3003 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int king = sc.nextInt();
        int queen = sc.nextInt();
        int rook = sc.nextInt();
        int bishop = sc.nextInt();
        int knight = sc.nextInt();
        int phon = sc.nextInt();
        king = -(king)+1;
        queen = -(queen)+1;
        rook = -(rook)+2;
        bishop = -(bishop)+2;
        knight = -(knight)+2;
        phon = -(phon)+8;
        System.out.println(king+" "+queen+" "+rook+" "+bishop+" "+knight+" "+phon);
    }
}
