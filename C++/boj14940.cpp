#include <iostream>
#include <vector>
#include <queue>

int main(){

    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n, m;
    std::cin >> n >> m;

    std::vector<std::vector<int>> graph(n, std::vector<int>(m));
    std::vector<std::vector<int>> visited(n, std::vector<int>(m, -1));
    int start_x;
    int start_y;

    std::vector<std::pair<int, int>> move(4);
    move[0] = {0, 1};
    move[1] = {1, 0};
    move[2] = {0, -1};
    move[3] = {-1, 0};


    for (int i = 0; i < n; i++){
        for (int j = 0; j < m; j++){
            std::cin >> graph[i][j];

            if (graph[i][j] == 2){
                start_y = i;
                start_x = j;
            } else if (graph[i][j] == 0){
                visited[i][j] = 0;
            }
            
        }
    }

    std::queue<std::pair<int, int>> q;

    q.push({start_y, start_x});
    visited[start_y][start_x] = 0;
    while (!q.empty()){
        std::pair<int, int> xy = q.front();
        int y = xy.first;
        int x = xy.second;
        q.pop();

        for (int i = 0; i < 4; i++){
            
            int dy = y + move[i].first;
            int dx = x + move[i].second;
            
            if ((0 <= dx && dx < m) && (0 <= dy && dy < n)){
                if (graph[dy][dx] == 0) continue;   
                if (visited[dy][dx] != -1) continue;

                visited[dy][dx] = visited[y][x] + 1;
                q.push({dy, dx}); 
            }
        }
    }

    for (int i = 0; i < n; i++){
        for (int j = 0; j < m; j++){
            std::cout << visited[i][j] << " ";
        }
        std::cout << '\n';
    }
}