import java.io.*;
public class boj25191_2{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int chicken = Integer.parseInt(br.readLine());
        String[] s = br.readLine().split(" ");
        int coke = Integer.parseInt(s[0]);
        int beer = Integer.parseInt(s[1]);
        int drinks = coke/2+beer;
        if (drinks>=chicken){
            System.out.println(chicken);
        }
        else{
            System.out.println(drinks);
        }
    }
}