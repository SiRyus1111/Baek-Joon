import java.io.*;
public class boj14648 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        String[] k = br.readLine().split(" ");
        int n = Integer.parseInt(k[0]);
        int q = Integer.parseInt(k[1]);
        String[] w = br.readLine().split(" ");
        int[] arr = new int[n];
        for(int i=0;i<n;i++){
            arr[i] = Integer.parseInt(w[0]);
        }
        for(int i=0;i<q;i++){
            String[] query1 = new String[5];
            query1 = br.readLine().split(" ");
            int[] query2 = new int[5];
            for(int nn=0;nn<5;nn++){
                query2[nn] = Integer.parseInt(query1[nn]);
            }
            if(query2[0]==1){
                int a = query2[1];
                int b = query2[2];
                int temp;
                for(int start=)
                temp = arr[b-1];
                arr[b-1] = arr[a-1];
                arr[a-1] = temp;
            }
            else if(query2[0]==2){
                
            }
        }
    }
}
