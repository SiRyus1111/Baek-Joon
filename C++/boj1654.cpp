#include <iostream>

int main(){
    int k, n;
    std::cin >> k >> n;
    std::cin.ignore();
    unsigned int* lan = new unsigned int[10000];
    int max = 0;

    for (int i = 0; i < k; i++){
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
        long long cnt = 0;
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