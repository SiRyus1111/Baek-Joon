// 백준 2565번 - 전깃줄
// 문제 유형 : 다이나믹 프로그래밍

// 권장 시간 복잡도 : 전깃줄 개수 = 100이하의 자연수, 전봇대 위치의 번호 = 500이하의 자연수. 
// 제한시간 = 1초
// 일일히 전깃줄 하나하나, 전봇대 번호 하나하나 탐색할 때 100 * 500 = 50000번의 연산 필요함.
// = 1초에 1억번 연산이라고 가정하면 O(N^3)까지도 가능.

#include <iostream>
#include <vector>
#include <algorithm>

struct pole{
    int A_pole = 0;
    int B_pole = 0;
};

bool compare(pole A, pole B){
    return A.A_pole < B.A_pole;
}

int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n;
    std::cin >> n;

    std::vector<pole> poles(n);

    std::vector<int> dp(n, 1);

    for (int i = 0; i < n; i++){
        int a, b;

        std::cin >> a >> b;

        poles[i].A_pole = a;
        poles[i].B_pole = b;
    }

    // 디버깅 포인트
    // 밑의 dp vector 갱신 문제를 고쳤는데도 그저 dp vector가 갱신만 될 뿐 아예 이상한 값이 나왔다.
    // 애초에 이 로직이 poles vector가 A_pole을 기준으로 오름차순 정렬되어있다는 가정 하에 만들어진 로직이라서,
    // 이렇게 정렬을 해줘야했다.
    std::sort(poles.begin(), poles.end(), compare);

    for (int i = 1; i < n; i++){
        for (int j = 0; j < i; j++){

            // 최적화 포인트
            // 원래는 이 if문의 조건이 이랬다. 두 전선이 교차하는지 아닌지 판별하기 위해서 만든 조건식이다.
            // !(poles[i].A_pole > poles[j].A_pole && poles[i].B_pole < poles[j].B_pole) || (poles[i].A_pole < poles[j].A_pole && poles[i].B_pole > poles[j].B_pole)
            // 하지만 이미 A_pole에 대해 오름차순 정렬 되어있으므로, 그저 B_pole이 교차하는지만 보면 된다. 이렇게 복잡한 조건식을 쓸 필요가 없다.
            if (poles[i].B_pole > poles[j].B_pole){
                // 디버깅 포인트
                // 처음에 dp vector가 갱신이 안되어서 여기서 cout로 출력을 해봄으로써 위의 if문이 정상적이라는 것을 확인했다.
                // 하지만 dp vector가 갱신이 안 되었기 때문에 아래의 if문이 비정상적이었다고 생각해서, 결국 문제를 찾아냈다.
                // dp[i] = std::max(dp[i], dp[j]);
                // 이렇게 dp[i] = 현재의 전선 수와 이전의 전선 수 중에 더 큰 것
                // 으로 하고있었다.. 실제로는 dp[i]는 dp[j]의 다음 단계가 되므로 dp[i]와 dp[j] + 1을 비교해야한다.
                // 역시 밤에 집중력 딸리는 상태로 알고리즘 문제를 푸는 것은 위험하다. 이런 초보적인 실수를 하게 된다.
                dp[i] = std::max(dp[i], dp[j] + 1);
            }
        }
    }

    int max_amount = 0;
    // 디버깅 포인트
    // 원래는 반복문이 
    // for (int i = 1; i < n; i++)
    // 이었는데 n == 1인 경우를 처리하지 못했다.
    // 사실 원래는 dp[i]랑 dp[i-1]을 비교하게 하려고 했는데,
    // 그 때 잘못된 인덱스에 접근하는걸 막기 위해 i = 1번부터 시작했었다.
    // 하지만 max를 사용하는 방식으로 바꿨는데 그걸 수정하지 않은 탓에
    // n == 1인 경우를 처리하지 못했다.
    // 코드를 다 짠 후 수정이 필요한 곳이 있는지 꼼꼼히 확인해야겠다..
    for (int i = 0; i < n; i++){
        max_amount = std::max(dp[i], max_amount);
    }

    std::cout << (n - max_amount);
}

// 결과 : 메모리 = 2024KB, 시간 = 0ms