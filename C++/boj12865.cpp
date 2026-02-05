#include <iostream>
#include <vector>
#include <algorithm>

int main(){
    int n, k;
    std::cin >> n >> k;

    std::vector<std::pair<int, int>> item(n);

    int* dp = new int[k + 1];

    for (int i = 0; i < n; i++){
        int w, v;
        std::cin >> w >> v;
        item[i] = {w, v};
    }

    for (int i = 0; i <= k; i++){
        dp[i] = 0;
    }

    for (int i = 0; i < n; i++){
        auto [wei, val] = item[i];

        for (int j = k; j >= wei; j--){
            dp[j] = std::max(dp[j], dp[j - wei] + val);
        }
    }

    std::cout << dp[k] << std::endl;

    delete[] dp;
}