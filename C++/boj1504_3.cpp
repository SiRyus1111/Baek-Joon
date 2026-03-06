// 백준 1504번 - 특정한 최단 경로
// 문제 유형 : 다익스트라
// 권장 시간 복잡도 : 노드(V) = 최대 800개, 간선(E) = 최대 200000개
// 다익스트라 알고리즘의 시간복잡도 = O(E log V)로는 200000 log 800이고,
// 시간 제한이 1초 = 약 1억번의 계산 가능 이므로, 다익스트라로 충분히 풀 수 있다.
// 가중치는 최대 1000, 간선 = 최대 200000개이므로 1000 * 200000 200000000 = 2억이므로 int형을 써도 된다. int형은 최대 21억.

// 발상 :
// 그냥 시작 지점이랑 두 정점(v1, v2)에서 다익스트라를 돌려서
// 시작 지점 -> v1 -> v2 -> 도착 지점
// 시작 지점 -> V2 -> V1 -> 도착 지점
// 중에 더 최단경로가 짧은 것을 고르면 된다.
// 그리고 이 두 개의 최단 경로를 구하려면
// 시작지점에서 시작 -> V1,V2
// V1에서 시작 -> V2,도착지점
// V2에서 시작 -> V1,도착지점
// 딱 이렇게 세 정점으로부터 시작하는 다익스트라만으로도 가능하다.

#include <iostream> // 표준 입출력
#include <vector> // vector
#include <queue> // priority_queue
#include <functional> // greater
#include <algorithm> // min()

const int MAX_VALUE = 1 << 30; // INF라고 쓰는게 편했는데 깜빡하고 MAX_VALUE 써버림.. 자바가 어렴풋이 기억이 났나봐.

std::vector<int> dist(int node_num, std::vector<std::vector<std::pair<int, int>>>& graph){
    
    // 전체 노드 갯수. 나중에 +1할텐데 왜 -1을 했냐면, 전체 노드 갯수라는 것을 의미한다는걸 확실히 할려고 했다.
    // -1을 안하면 값이 전체 노드 갯수 +1이 되므로..
    int n = (int)graph.size() - 1; 

    // 우선순위 큐
    std::priority_queue<
    std::pair<int, int>, // 우선순위 큐에 저장할 값의타입 
    std::vector<std::pair<int, int>>, // 실제로 우선순위 큐 역할을 할, 실제로 값을 담을 컨테이너
    // 처음에는 단순히 std::greater<int>를 사용했지만, 실제로 우선순위 큐에 들어가는 값의 타입은 pair<int, int>이므로 정상적으로 greater<>를 사용하기 위해서는 우선순위 큐에 들어가는 값에 타입에 맞춰야한다.
    // greater<>를 사용하면, compare(A, B)로 값들을 비교하는 식으로 동작하는데, 
    // 여기서는 단순히 std::greater<int>를 사용하면 실제로 비교해야하는 std::pair<int, int>가 아니라 그저 int만 비교하므로 에러가 발생한다.
    std::greater<std::pair<int, int>> // 우선순위 비교 기준 (여기서는 최소 우선) / 왜 최소 우선이 greater이냐고 할 수 있지만, 
    > pq;

    // 시작할 때는 시작 노드로부터 모든 노드로의 최단 경로가 기록되지 않았으므로 
    // 가능할리가 없는 아주 큰 값으로 최단 경로를 저장하는 dist(distance)를 저장하는 vector를 초기화해놓는다.
    // 길이는 각각의 노드의 최단 경로이므로 전체 노드의 갯수 + 1(1 ~ n번 인덱스까지 있어야함)
    // 그냥 그래프의 인덱스 수만큼 만들어주면 된다.
    std::vector<int> dist (n + 1, MAX_VALUE);
    
    // 시작 노드의 거리(시작 지점이므로 0)를 기록하고 우선순위 큐에 시작 노드를 넣는다.
    dist[node_num] = 0;
    pq.push({0, node_num});

    // 본격적인 다익스트라
    while (!pq.empty()){ // 종료 조건 = 우선순위 큐가 빌 때

        // 우선순위 큐의 가장 우선순위 높은 원소(top)를 꺼낸다.
        // {현재 시점까지의 누적 가중치, 현재 시점 노드} 로 저장했으므로,
        // 그렇게 변수명을 지어준다.
        // 물론 top()으로 가장 우선순위가 높은 원소를 복사한 후
        // pop()으로 꺼내주는 식이다.        
        auto [cur_wei, cur_node] = pq.top(); 
        pq.pop();

        // 만약 이미 기록되어있는 그 노드의 최단경로가 우선순위 큐에서 꺼낸 최단 경로보다 짧다면
        // 우선순위 큐에서 꺼낸 최단 경로는 쓸모가 없다. 이미 더 짧은 경로로 이 노드에 도달할 수 있으니까.
        // 그래서 다시 while문 처음으로 돌아간다.
        if (dist[cur_node] < cur_wei) continue;

        // 본격적인 현재 노드와 연결되어있는 노드 탐색
        // graph는 vector라서 for-each문을 돌릴 수 없을 것 같지만,
        // 모던 C++에서는 충분히 가능하다.
        // 컴파일러가 vector라이브러리의 begin()과 end() 함수를 이용해서
        // 시작인덱스부터 끝인덱스까지 순회할 수 있다.
        // 그리고 값은 auto로 받는다. auto는 vector에 저장된 값의 타입을 자동으로 추론해서 저장해준다.
        for (auto [next_wei, next_node] : graph[cur_node]){ 
            
            int w = cur_wei + next_wei; // 현재 노드에서 현재 노드와 연결되어있는 다음 노드로 가는 누적 가중치 계산
            if (w < dist[next_node]){ // 만약 그 값이 지금까지 계산된 그 노드(다음 노드)로 가는 누적 가중치보다 작다면
                dist[next_node] = w; // 갱신 후
                pq.push({w, next_node}); // 우선순위 큐에 push하기
            }
        }
    }

    return dist;
}

int main(){
    // 입력받는 속도를 위해 사용
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    
    int v, e;
    std::cin >> v >> e;

    // 디버깅 포인트 = 애초에 간선이 0개인 경우도 입력으로 들어올 수도 있으므로 
    // 이 코드를 그대로 실행하면 아예 graph에 아무런 노드의 간선 정보도 들어가지 않는다.
    // 그래서 간선이 0개인 경우에 대한 예외처리를 추가로 했다.
    if (e == 0){
        std::cout << -1;
        return 0;
    }

    // 이 vector는 
    // 맨 바깥의 vector의 인덱스 = 노드 번호
    // 안에 있는 vector = 그 노드와 연결되어있는 노드들
    // pair = {가중치, 노드 번호} 쌍
    // 이다.
    std::vector<std::vector<std::pair<int, int>>> graph(v + 1);

    // 간선들 입력받기
    for (int i = 1; i <= e; i++){
        
        int vertex1, vertex2, wei;
        std::cin >> vertex1 >> vertex2 >> wei;

        // 문제에서 양방향 간선이라고 했으므로 vertex1 -> vertex2, vertex2 -> vertex1의 경우 모두 저장한다.
        // 그리고 우선순위 큐에서 가중치를 먼저 고려해서 가중치가 작은 순서대로 pop해야하니 {가중치, 노드 번호}로 저장한다.
        graph[vertex1].push_back({wei, vertex2});
        graph[vertex2].push_back({wei, vertex1});
    }
    
    // 꼭 자나가야하는 노드 입력받기
    int v1, v2;
    std::cin >> v1 >> v2;

    // 시작 노드(1), 꼭 지나가야하는 노드 1, 2(v1, v2)에서 각각 다익스트라를 시행
    std::vector<int> start_dist = dist(1, graph);
    std::vector<int> v1_dist = dist(v1, graph);
    std::vector<int> v2_dist = dist(v2, graph);

    // 두 지점을 지나는 최단 경로 구하기
    int path1 = start_dist[v1] + v1_dist[v2] + v2_dist[v];
    int path2 = start_dist[v2] + v2_dist[v1] + v1_dist[v];

    // 그중 최단 경로 구하기
    int shortest_path = std::min(path1, path2);

    // 만약 도착 지점에 도달할 수 없다면 -1 출력
    // 노드 두 개일 때 두 노드가 연결이 안되어 MAX_VALUE가 나오는 경우까지 고려
    if (shortest_path >= MAX_VALUE){
        std::cout << -1;
        
    }
    // 도달할 수 있다면 최단 경로 출력
    else{
        std::cout << shortest_path;
    }
    
    // 종료
    return 0;
}

// 결과 : 메모리 = 5728KB 시간 = 36ms

// 이전의 결과 : 메모리 = 5776KB 시간 = 112ms와 약간의 적은 메모리 사용량과 상당히 줄어든 실행 시간.
// 아마 요인은, 처음에 적었던 이 두 줄 = 
// std::ios::sync_with_stdio(false); 
// std::cin.tie(nullptr);
// 이 입력받는 시간을 단축시킨 것과,

// long long 자료형을 int 자료형으로 바꿔서 64비트(8바이트) -> 32비트(4바이트)로 변수의 크기가 줄어든게 영향이 있어보임.

// 그리고 츨력할 때 std::endl을 하지 않아 출력 버퍼 비우는 시간이 없어서 조금이나마 단축되지 않았나 싶음.