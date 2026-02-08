#include <iostream>
#include <vector>
#include <algorithm>

int main(){

    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int n;
    std::cin >> n;

    std::vector<int> arr(n);
    std::vector<int> dp_inc(n);
    std::vector<int> dp_dec(n);

    fill(dp_inc.begin(), dp_inc.end(), 1);
    fill(dp_dec.begin(), dp_dec.end(), 1);

    for (int i = 0; i < n; i++){
        std::cin >> arr[i];
    }

    for (int i = 0; i < n; i++){
        for (int j = 0; j < i; j++){
            if ((arr[j] < arr[i]) && ((dp_inc[j] + 1) > dp_inc[i])){
                dp_inc[i] = dp_inc[j] + 1;
            }
        }
    }

    for (int i = n - 1; i >= 0; i--){
        for (int j = n - 1; j > i; j--){
            if ((arr[j] < arr[i]) && ((dp_dec[j] + 1) > dp_dec[i])){
                dp_dec[i] = dp_dec[j] + 1;
            }
        }
    }
    
    int res = 0;
    for (int i = 0; i < n; i++){
        res = std::max(res, dp_inc[i] + dp_dec[i] - 1);
    }

    std::cout << res;

    return 0;
}