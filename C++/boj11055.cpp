// 백준 11055번 - 가장 큰 증가하는 부분 수열
// 시간복잡도 분석 : N(array_size)가 최대 1000이므로 1초(1억번 연산) 안에는 O(N^2)까지 무난하게 통과. O(N^3)은 최대 1000000000(10억)번 연산해야해서 불가능..
// == 이중 반복문까지는 OK.

// 이거 그냥 LIS(Longest Increasing Subsequence) 문제에서 
// dp[i] = i번 인덱스까지의 가장 긴 부분 수열의 길이
// 이거를
// dp[i] = i번 인덱스까지의 가장 큰 부분 수열의 길이
// 이렇게 바꾸면 끝인 문제이다.

// 기존의 LIS 문제에서는 이전 인덱스 원소(array[j]) < 현재 인덱스 원소(array[i]) 일 때
// dp[i](지금까지 갱신된 가장 긴 증가하는 부분 수열 길이)와 dp[j] + 1(이전의 가장 긴 증가하는 부분 수열의 길이 + 현재 인덱스까지 포함)
// 이렇게 두 개를 비교해서 더 큰 값(더 긴 증가하는 부분 수열 길이)을 고르면 됐었는데

// 여기서는 이전 인덱스 원소(array[j]) < 현재 인덱스 원소(array[i]) 일 때인건 같지만
// dp[i](지금까지 갱신된 가장 큰 증가하는 부분 수열의 모든 원소를 더한 값)와 dp[j] + array[i](이전의 가장 큰 증가하는 부분 수열의 모든 원소를 더한 값 + 현재 인덱스 원소의 값)
// 이렇게 두 개를 비교해서 더 큰 값(더 큰 증가하는 부분 수열의 모든 원소를 더한 값)을 고르면 된다.

// 사실상 전체적인 매커니즘은 상당히 비슷하고, 그저 dp[i]가 의미하는게 달라짐에 따라
// 조금 코드를 수정하면 된다.

#include <iostream>
#include <algorithm>
#include <vector>

int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int array_size;

    std::cin >> array_size;
    std::vector<int> array(array_size);
    std::vector<int> dp(array_size);

    for (int i = 0; i < array_size; i++){
        std::cin >> array[i];
        dp[i] = array[i];
    }

    for (int i = 1; i < array_size; i++){
        for (int j = 0; j < i; j++){
            if (array[j] < array[i]){
                // 디버깅 포인트 
                // 이전 누적 값 + 현재 값 해야하는데 이전 누적 값 + 이전 값(이미 이전 누적 값에 포함)
                // dp[i] = std::max(dp[i], dp[j] + array[j]); / array[j]가 문제.
                dp[i] = std::max(dp[i], dp[j] + array[i]); 
            }
        }
    }

    int max_sum = 0;
    for (int i = 0; i < array_size; i++){
        max_sum = std::max(dp[i], max_sum);
    }

    std::cout << max_sum << '\n';
}

// 결과 : 메모리 = 2020KB, 시간 = 0ms