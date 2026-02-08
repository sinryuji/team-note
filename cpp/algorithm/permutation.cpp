#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

void dfs(const vector<int> &v,
         vector<bool> &used,
         vector<int> &cur,
         vector<vector<int> > &result,
         const int r) {
  if (cur.size() == r) {
    result.push_back(cur);
    return;
  }

  for (int i = 0; i < v.size(); i++) {
    if (used[i]) continue;

    used[i] = true;
    cur.push_back(v[i]);
    dfs(v, used, cur, result, r);
    cur.pop_back();
    used[i] = false;
  }
}

vector<vector<int> > permutations(vector<int> &v, int r) {
  vector<vector<int> > result;
  vector<bool> used(v.size(), false);
  vector<int> cur;

  dfs(v, used, cur, result, r);

  return result;
}

int main() {
  vector<int> nums = {1, 2, 3, 4, 5, 6};

  vector<vector<int> > perm = permutations(nums, 3);
  int cnt = 0;
  for (const auto &p: perm) {
    for (int v: p) cout << v << " ";
    cout << endl;
    cnt++;
  }

  cout << cnt << endl;
}
