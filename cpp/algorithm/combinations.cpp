#include <iostream>
#include <vector>

using namespace std;

void dfs(const vector<int> &v, int start, int r, vector<int> &cur, vector<vector<int> > &result) {
  if (cur.size() == r) {
    result.push_back(cur);
    return;
  }

  for (int i = start; i < v.size(); i++) {
    cur.push_back(v[i]);
    dfs(v, i + 1, r, cur, result);
    cur.pop_back();
  }
}

vector<vector<int> > combinations(const vector<int> &v, int r) {
  vector<vector<int> > result;
  vector<int> cur;

  dfs(v, 0, r, cur, result);

  return result;
}

int main() {
  vector<int> nums = {1, 2, 3, 4, 5, 6};


  vector<vector<int> > combi = combinations(nums, 3);
  int cnt = 0;
  for (const auto &c: combi) {
    for (const int v: c) cout << v << " ";
    cout << endl;
    cnt++;
  }

  cout << cnt << endl;
}
