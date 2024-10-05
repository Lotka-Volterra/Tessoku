#include <bits/stdc++.h>
#include <atcoder/all>

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

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N, Q;
    map<int, int> dict;
    // 符号で、逆順になっているかどうかを管理
    int sign = 1;
    rep(i, Q)
    {
        int q;
        cin >> q;
        if (q == 1)
        {
            int x, y;
            cin >> x >> y;
            if (sign > 0)
            {
                dict[x] = y;
            }
            else
            {
                dict[N + 1 - x] = y;
            }
        }
        else if (q == 2)
        {
            sign *= -1;
        }
        else
        {
            int x;
            cin >> x;
            bool exist = dict.find(x) != dict.end();
            bool exist_reverse = dict.find(N + 1 - x) != dict.end();
            if (sign > 0)
            {
                if (exist)
                {
                    cout << dict[x] << endl;
                }
                else
                {
                    cout << x << endl;
                }
            }
            else
            {
                if (exist_reverse)
                {
                    cout << dict[N + 1 - x] << endl;
                }
                else
                {
                    cout << N + 1 - x << endl;
                }
            }
        }
    }
    return 0;
}