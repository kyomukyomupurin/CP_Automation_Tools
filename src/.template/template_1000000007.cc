#include <bits/stdc++.h>

using namespace std;
using int64 = long long;

#define ALL(v) std::begin(v), std::end(v)
#define RALL(v) std::rbegin(v), std::rend(v)

template <class T> inline bool minimize(T& x, T y) { if (x > y) { x = y; return 1; } return 0; }
template <class T> inline bool maximize(T& x, T y) { if (x < y) { x = y; return 1; } return 0; }

template <class T>
T inverse(T a, T m) {
  T u = 0, v = 1;
  while (a != 0) {
    T t = m / a;
    m -= t * a;
    std::swap(a, m);
    u -= t * v;
    std::swap(u, v);
  }
  assert(m == 1);
  return u;
}

template <int Mod>
class Modular {
 public:
  constexpr Modular(int64 val = 0) : val_(val % mod()) {
    if (val_ < 0) val_ += mod();
  }

  const int64& operator()() const noexcept { return val_; }

  constexpr int mod() const noexcept { return Mod; }

  constexpr Modular& operator+=(const Modular& other) noexcept {
    if ((val_ += other.val_) >= mod()) val_ -= mod();
    return *this;
  }

  constexpr Modular& operator-=(const Modular& other) noexcept {
    if ((val_ -= other.val_) < 0) val_ += mod();
    return *this;
  }

  constexpr Modular& operator*=(const Modular& other) noexcept {
    (val_ *= other.val_) %= mod();
    if (val_ < 0) val_ += mod();
    return *this;
  }

  constexpr Modular& operator/=(const Modular& other) noexcept {
    return *this *= Modular(inverse(other.val_, static_cast<int64>(mod())));
  }

  constexpr Modular& operator++() noexcept { return *this += 1; }

  constexpr Modular& operator--() noexcept { return *this -= 1; }

  constexpr Modular operator-() const noexcept { return Modular(-val_); }

  friend std::istream& operator>>(std::istream& is, Modular& num) {
    int64 x;
    is >> x;
    num = Modular(x);
    return is;
  }

  friend std::ostream& operator<<(std::ostream& os, const Modular& num) {
    return os << num();
  }

 private:
  int64 val_;
};

constexpr int mod = int(1e9) + 7;
using Mint = Modular<mod>;

Mint operator+(const Mint& lhs, const Mint& rhs) noexcept {
  return Mint(lhs) += rhs;
}

Mint operator-(const Mint& lhs, const Mint& rhs) noexcept {
  return Mint(lhs) -= rhs;
}

Mint operator*(const Mint& lhs, const Mint& rhs) noexcept {
  return Mint(lhs) *= rhs;
}

Mint operator/(const Mint& lhs, const Mint& rhs) noexcept {
  return Mint(lhs) /= rhs;
}

bool operator==(const Mint& lhs, const Mint& rhs) noexcept {
  return lhs() == rhs();
}

bool operator!=(const Mint& lhs, const Mint& rhs) noexcept {
  return !(lhs() == rhs());
}

template <class T>
Mint power(const Mint& a, T b) {
  assert(b >= 0);
  Mint x = a, res = 1;
  while (b) {
    if (b & 1) res *= x;
    x *= x;
    b >>= 1;
  }
  return res;
}

// 二項係数テーブルを必要なところまで作る
// inv だけ前計算したいときは choose(200000, 1) とかで適当に空呼び出しすればいい
// std::vector<Mint> fact{1, 1};
// std::vector<Mint> inv{0, 1};
// std::vector<Mint> inv_fact{1, 1};

// Mint choose(int n, int k) noexcept {
//   if (n < k || n < 0 || k < 0) return 0;
//   while (int(fact.size()) < n + 1) {
//     int sz = fact.size();
//     fact.emplace_back(fact.back() * sz);
//     inv.emplace_back(mod - inv[mod % sz] * (mod / sz));
//     inv_fact.emplace_back(inv_fact.back() * inv.back());
//   }
//   return fact[n] * inv_fact[k] * inv_fact[n - k];
// }

int main() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(nullptr);
  std::cout << std::fixed << std::setprecision(17);


  return 0;
}