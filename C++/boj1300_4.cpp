// 백준 1300번 - K번째 수
// 문제 유형 : 이분 탐색(값에 대한 이분 탐색, parametric search)

// 0. 단순히 배열을 직접 만들어 정렬하려하면 최대 100000 * 100000 = 10000000000번의 연산이 필요하므로
// 배열을 만들어서 정렬 후 K번째 수를 구하는 방법은 사실상 불가능하다.

// 그렇기 때문에 일단 각 행에서 mid보다 작은 수의 갯수를 구한다.

// 1. K번째로 큰 수 = K번째 수보다 작거나 같은 수의 갯수이므로
// 'mid보다 작거나 같은 수의 갯수'를 구한 후
// mid보다 작거나 같은 수의 갯수가 K개를 넘냐, 안 넘냐에 따라
// 계속 mid의 값을 이분 탐색으로 한 점으로 수렴하게
// start와 end의 값을 조정한다.

// mid보다 작거나 같은 수의 갯수가 K개를 넘으면 mid가 너무 큰 것이므로, end를 mid - 1로 조정한다.
// mid보다 작거나 같은 수의 갯수가 K개보다 적으면 mid가 너무 작은 것이므로, start를 mid + 1로 조정한다.

// 2. mid보다 작거나 같은 수의 갯수를 구하는게 이 문제의 핵심이다.
// 일단 각 행 별로 수는 i * 1 , i * 2 ... i * n까지 이어진다.
// 각 행 별로 mid보다 작거나 같은 수의 갯수를 구한 후 
// 그 값들을 전부 더하면 전체 배열에서 mid보다 작거나 같은 수의 갯수가 된다.

// 그리고 각 행별로 mid를 행의 번호인 i로 나눈다면 정확히 그 행의 mid보다 작거나 같은 수의 갯수가 나온다.

// 하지만 결국 각 행의 mid보다 작거나 같은 수의 갯수는 n개를 넘을 수 없으므로 
// n과 방금 계산한 값 중 작은 수가 그 행의 mid보다 작거나 같은 수의 갯수이다.

#include <iostream>
#include <algorithm>

int main(){

    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n, k; 

    std::cin >> n >> k;

    int start = 1;
    int end = k;

    int mid, res, sum, temp;
    
    while (start <= end){
        sum = 0;
        mid = (start + end) / 2;
        for (int i = 1; i <= n; i++){

            temp = mid / i;

            if (temp == 0) break;
            sum += std::min(n, temp);
        }

        if (sum >= k){
            res = mid;
            end = mid - 1;
        }

        else{
            start = mid + 1;
        }
    }

    std::cout << res;
}