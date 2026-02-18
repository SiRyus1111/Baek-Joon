// 시간 복잡도 = O(N) / 공간 복잡도 = O(1)
// 배열을 쓰지 않고 변수만 쓴 dp
// rgb 중 현재 색깔의 시점에서 바로 이전의 집의 색깔이 될 수 있는 두 집 중 누적 비용이 더 작은 집에 현재 색깔의 비용을 더한다.

#include <iostream>
#include <algorithm>
#include <vector>

int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    unsigned short n;
    std::cin >> n;

    unsigned house_r, house_g, house_b;


    std::cin >> house_r >> house_g >> house_b;

    int r_min, g_min, b_min;
    
    r_min = house_r;
    g_min = house_g;
    b_min = house_b;

    int r_temp, g_temp, b_temp;

    for (unsigned short i = 1; i < n; i++){

        std::cin >> house_r >> house_g >> house_b;

        r_temp = r_min;
        g_temp = g_min;
        b_temp = b_min;

        r_min = std::min(g_temp, b_temp) + house_r;
        g_min = std::min(r_temp, b_temp) + house_g;
        b_min = std::min(r_temp, g_temp) + house_b;

    }

    int result1 = std::min(r_min, g_min);

    int result2 = std::min(result1, b_min);

    std::cout << result2;
}