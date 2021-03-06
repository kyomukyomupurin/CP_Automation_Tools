#include <bits/stdc++.h>

using namespace std;
using int64 = long long;

#define ALL(v) std::begin(v), std::end(v)
#define RALL(v) std::rbegin(v), std::rend(v)

template <class T> inline bool minimize(T& x, T y) { if (x > y) { x = y; return 1; } return 0; }
template <class T> inline bool maximize(T& x, T y) { if (x < y) { x = y; return 1; } return 0; }
inline void Yes(bool cond) noexcept { std::cout << (cond ? "Yes" : "No") << '\n'; }

int main() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(nullptr);
  std::cout << std::fixed << std::setprecision(17);


  return 0;
}