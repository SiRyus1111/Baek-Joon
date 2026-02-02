#include <iostream>

int main(){
    int k, n;
    std::cin >> k >> n;
    std::cin.ignore();
    unsigned int* lan = new unsigned int[10000]; // k가 최대 10000이므로 10000칸짜리 동적 배열 선언(최대 40000바이트)
    int max = 0; // 랜선의 길이가 자연수이므로 최솟값은 1, 그러므로 max 변수를 0으로 초기화.

    for (int i = 0; i < k; i++){ // 랜선들의 길이 입력받기
        int num;
        std::cin >> num;
        lan[i] = num;
        if (max < num) max = num; // 이 if 문을 비트 연산으로 해보고 싶었는데 아쉽다
    }

    unsigned int start = 1;
    unsigned int end = max;
    unsigned int ans = 0;

    while (start <= end){
        unsigned int mid = (start + end) >> 1; // 비트 시프트로 나누기 2
        long long cnt = 0; // cnt는 whlie문 반복마다 초기화해야함. 안그러면 while문 반복마다 계속 값이 누적됨.
        for (int i = 0; i < k; i++){
            cnt += lan[i] / mid; // 동적 배열은 for each문 못쓰나? 일단 이렇게 해봄
        }
        if (cnt >= n){
            ans = mid;
            start = mid + 1;
        }
        else end = mid - 1;
    }
    std::cout << ans << std::endl;
    delete lan;
    // 시간복잡도는 O(n log n)? - 이분탐색 + 반복문
}