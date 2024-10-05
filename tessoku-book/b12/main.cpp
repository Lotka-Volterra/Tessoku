#include <bits/stdc++.h>

using namespace std;
// using namespace atcoder;
using ll = long long;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
// usage:rep(i,3){ processing }  i starts at 0 and increments by 1 until it reaches n.
#define rep2(i, s, n) for (int i = (s); i < (int)(n); i++)
// usage:rep2(i,1,3){ processing }  i starts at s and increments by 1 until it reaches n.
#define Yes cout << "Yes" << endl
#define No cout << "No" << endl
#define YES cout << "YES" << endl
#define NO cout << "NO" << endl
const ll MOD = 1000000007LL;
// const ll MOD = 998244353LL;

const vector<pair<int, int>> dpos4 = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
// const vector<pair<int, int>> dpos8 = {{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};
vector<int> input(int N)
{
    vector<int> vec(N);
    for (int i = 0; i < N; i++)
    {
        cin >> vec.at(i);
    }
    return vec;
}
vector<int> A;
int N;

bool isOk(int num)
{
    return num * (num * num + 1) >= N;
}
int binarySearch()
{
    // 誤差0.001まで許容=>0.001ずつ二分探索
    ll left = 0;
    ll right = 100'000;
    while (abs(right - left) > 0.001)
    {
        int mid = (left + right) / 2;
        if (isOk(mid))
        {
            right = mid;
        }
        else
        {
            left = mid;
        }
    }
    return right;
}
int main()
{
    cin >> N;
    cout << binarySearch() << endl;
    return 0;
}
