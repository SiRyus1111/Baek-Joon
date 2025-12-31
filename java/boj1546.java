import java.util.Scanner;
public class boj1546 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        double[] mx = new double[n];
        double max = 0;
        double sum = 0;
        for(int i=0;i<n;i++){
            mx[i] = sc.nextDouble();//성적 값 입력
        }
        for(int i=0;i<n;i++){
            if(mx[i]>max){
                max = mx[i];
            }//최고 점수 구하기
        }
        for(int i=0;i<n;i++){
            mx[i] = (mx[i]/max)*100;//성적 고치기
        }
        for(double num:mx){
            sum+=num;
        }//고친 성적 전부 더하기
        double average = sum / mx.length;//평균내기
        System.out.println(average);//출력하기
    }
}
