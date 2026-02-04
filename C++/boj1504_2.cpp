#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <functional>
#include <utility>

const long long INF = (1LL << 60);

std::vector<long long> dist(int start, const std::vector<std::vector<std::pair<int, int>>>& graph){
    int n = (int)graph.size() - 1;
    std::vector<long long> dp(n + 1, INF);

    // (거리, 노드 번호) / 작은 거리 우선
    std::priority_queue< // C++로 처음 우선순위 큐 써봤는데 왤케 복잡하냐 진짜..
        std::pair<long long, int>, // 저장할 값의 타입
        std::vector<std::pair<long long, int>>, // 실제로 값을 담을 컨테이너
        std::greater<std::pair<long long, int>> // 우선 순위 비교 기준
    > pq;

    dp[start] = 0;
    pq.push({0, start});

    while (!pq.empty()){
        auto [cur_wei, cur_node] = pq.top();
        pq.pop();

        if (cur_wei > dp[cur_node]) continue;

        for (auto [next_wei, next_node] : graph[cur_node]){
            long long w = (long long)next_wei + cur_wei;
            if (w < dp[next_node]){
                dp[next_node] = w;
                pq.push({w, next_node});
            }
        }
    }
    return dp;
}

int main(){
    int n, e;
    std::cin >> n >> e;
    
    std::vector<std::vector<std::pair<int, int>>> graph(n + 1); // 그래프. C++이 이래서 어럽구나.
    // 자유도가 높다 = 일일히 내가 다 설정해야한다..
    // C++의 장점이자 단잠..

    for (int i = 0; i < e; i++){
        int a, b, c;
        std::cin >> a >> b >> c;
        graph[a].push_back({c, b});
        graph[b].push_back({c, a});
    }
    
    int v1, v2;
    std::cin >> v1 >> v2;

    std::vector<long long> dist1 = dist(1, graph);
    std::vector<long long> distv1 = dist(v1, graph);
    std::vector<long long> distv2 = dist(v2, graph);

    long long path1 = dist1[v1] + distv1[v2] + distv2[n];
    long long path2 = dist1[v2] + distv2[v1] + distv1[n];
    
    long long shortest_path = (path1 < path2) ? path1 : path2;

    if (shortest_path >= INF){
        std::cout << -1 << std::endl;
    }
    else {
        std::cout << shortest_path << std::endl;
    }

    return 0;
}