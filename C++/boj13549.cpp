// 백준 13549번 - 숨바꼭질 3
// 두 번째로 풀었는데, 이번에는 딱히 외부 도움 없이 해결하는 것과, 지난번에는 파이썬으로 풀었다면 이번에는 C++로 구현해보는 것을 목표로 삼았습니다.
// 시간복잡도 분석 : N = 0 ~ 100000 / K = 0 ~ 100000 / 제한시간 2초
// 그래서 계속 +1만 하는 연산으로도 100000번이면 결과가 나오게됩니다. 그래서 O(n log n)까지는 될 가능성이 매우 높습니다.

// 이 문제는 뭔가 절대 그래프로 나타낼 수 없을 것 같지만,
// 그래프가 아닌 
// "목적지까지의 최단 경로를 구한다."
// 라는 생각으로 접근한다면, 굳이 그래프로 나타내지 않아도 발상이 그리 어렵지 않게 떠오릅니다.
// 뭔가 이런 최단 경로를 구하는 알고리즘들은 일반적으로 그래프로 생각할 수 있는 것에서만 동작한다는 편견을 깨야 하는 것 같습니다.
// 이 문제에서도 명시적으로 그래프로 주어지지만 않았지 사실상 그래프나 다름 없습니다.

// 현재 노드(위치)에서 이동할 수 있는 경우의 수는 1초 걸려서 +1 / 1초 걸려서 -1 / 0초 걸려서 *2이므로,
// 다익스트라를 가중치 1, 현재 위치 + 1 / 가중치 1, 현재 위치 - 1 / 가중치 0, 현재 위치 * 2의 지점의 
// 현재까지의 최단경로(dist)를 계속 갱신해주는 식으로 돌리면 됩니다.

// 그리고 현재 노드가 목적지(k)라면, 현재까지의 이동 시간(dist[k] / cur_wei)를 반환하는 식으로..

// 파이썬과 달랐던 점 : 

// 우선순위 큐를 선언하는 방식. 파이썬은 그냥 heapq 딸깍 느낌인데,
// C++에서는 다뤄야 할 자료형, 실제로 우선순위 큐를 담당할 객체(?), 우선순위 판별 방식까지 다 신경을 써줘야 했다.

// for-each문이 좀 다름. 파이썬은 그냥 튜플 넣고 딱히 자료형 지정할 필요가 없으니 상시 auto나 마찬가지.
// C++에서는 그냥 {가중치, 다음 노드} 이렇게 바로 못 때려넣고, 외부에서 따로 배열 만들어놓은 후에 for-each문에 넣어야함. 그리고 auto도 써야함..

// 실행 시간과 사용 메모리. 앞에서 말한 것들은 전부 C++이 더 안좋은데, 이거 하나만큼은 C++이 극단적으로 좋음.
// 이건 실행 결과에서 비교해보겠습니다.
#include <iostream>
#include <queue>
#include <vector>
#include <functional>

const int INF = 1 << 30;
const int MAX_LEN = 100001;

// 다익스트라
int dijkstra(const int start_node, const int end_node){
    // 우선순위 큐
    std::priority_queue<
    std::pair<int, int>,
    std::vector<std::pair<int, int>>,
    std::greater<std::pair<int, int>>
    > pq;

    // 거리(distance)를 기록할 vector
    std::vector<int> dist(MAX_LEN, INF);

    // 시작 노드 처리
    dist[start_node] = 0;
    pq.push({0, start_node});

    while (!pq.empty()){
        auto [cur_wei, cur_node] = pq.top();
        pq.pop();

        int moves[3][2] = {{1, cur_node + 1}, {1, cur_node - 1}, {0, cur_node * 2}};

        if (cur_node == end_node) {
            return cur_wei;
        }
        if (dist[cur_node] < cur_wei) continue;

        for (auto [next_wei, next_node] : moves){

            if (next_node < 0 || next_node >= MAX_LEN ) {
                continue;
            }
            int w = next_wei + cur_wei;
            if (dist[next_node] > w){
                dist[next_node] = w;
                pq.push({w, next_node});
            }
        }
    }

    return dist[end_node];
}

int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n, k;
    std::cin >> n >> k;

    if (n >= k){
        std::cout << n - k << '\n';
        return 0;
    }

    int res = dijkstra(n, k);

    std::cout << res << '\n';

    return 0;
}

// 실행 결과 : 메모리 = 2924KB, 시간 = 4ms
// 이전의 파이썬 실행 결과 : 메모리 = 37316KB, 시간 = 100ms

// 메모리 사용량 약 12배, 실행 시간 약 25배 차이..