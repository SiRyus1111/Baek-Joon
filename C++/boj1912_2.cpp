#include <iostream>
#include <algorithm>

int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n;
    std::cin >> n;
    int x;
    std::cin >> x;
    int cur, max_value;
    cur = x;
    max_value = x;
    
    for (int i = 1; i < n; i++){
        std::cin >> x;
        cur = std::max(x, cur + x);
        max_value = std::max(max_value, cur);
    }
    
    std::cout << max_value;
}