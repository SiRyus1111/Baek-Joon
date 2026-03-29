// 백준 13458 - 시험 감독
// 시간복잡도 분석 : 입력값이 n = 최대 1,000,000, A[i] 각각 최대 1,000,000이고..
// O(n * A[i])이고, b, c 모두 1일 경우에 최대 1000000 * 1000000.. 이건 안됨.
// O(n log A[i])? 이거는.. 모르겠다..
// O(n)은 무조건 됨. 
// 이산수학 공부해야겠다.. 시간복잡도 좀 더 잘 알고싶어..

// 일단 이거 총감독관은 무조건 1명만 있어야하니까 일단 이걸 먼저 고려를 해버려서
// 모든 감독관 수에 시험장 수(총감독관 수)를 먼저 더해버림.
// 이제 여기서 두 가지로 분기되는데,

// 1. 이미 총감독관으로 커버가 되면 그냥 다음 시험장으로 넘어가기.

// 2. 총감독관을 넘어 부감독관으로 넘어가야하면 총감독관으로 커버되는 인원수를 제외한 나머지 인원을 가지고
// 나머지 인원 / 부감독관 1명당 커버 가능 인원
// 이렇게 한 후 올림해서(어쨌든 모든 인원을 커버해야하니까?)
// 모든 감독관 수에 더하면 됨.

// 이걸 모든 시험장마다 반복.

#include <iostream>
#include <math.h>

int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n, b, c;
    std::cin >> n;

    int *array = new int[n];

    for (int i = 0; i < n; i++){
        std::cin >> *(array + i);
    }

    std::cin >> b >> c;
    
    // 디버깅 포인트
    long long sum = n;

    for (int i = 0; i < n; i++){
        array[i] -= b;
        if (array[i] <= 0) {
            continue;
        }

        // 최적화 포인트
        sum += (array[i] + c - 1) / c;
    }

    std::cout << sum;

    delete[] array;

    return 0;
}

// 메모리 : 5928KB / 시간 : 108ms