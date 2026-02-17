#include <iostream>
#include <algorithm>
#include <vector>

int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    unsigned short n;
    std::cin >> n;

    unsigned house_a, house_b, house_c;


    std::cin >> house_a;
    std::cin >> house_b;
    std::cin >> house_c;

    int a_min, b_min, c_min;
    
    a_min = house_a;
    b_min = house_b;
    c_min = house_c;

    int a_temp, b_temp, c_temp;

    for (unsigned short i = 1; i < n; i++){

        std::cin >> house_a;
        std::cin >> house_b;
        std::cin >> house_c;

        a_temp = a_min;
        b_temp = b_min;
        c_temp = c_min;

        a_min = std::min(b_temp, c_temp) + house_a;
        b_min = std::min(a_temp, c_temp) + house_b;
        c_min = std::min(a_temp, b_temp) + house_c;

    }

    int result1 = std::min(a_min, b_min);

    int result2 = std::min(result1, c_min);

    std::cout << result2;
}