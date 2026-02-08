#include <iostream>
#include <vector>

using namespace std;

vector<int> arr;
vector<int> tree;

int init(int start, int end, int index) {
    if (start == end) {
        return tree[index] = arr[start];
    }
    int mid = (start + end) / 2;
    tree[index] = init(start, mid, index * 2) + init(mid + 1, end, index * 2 + 1);
    return tree[index];
}

int interval_sum(int start, int end, int index, int left, int right) {
    if (left > end || right < start) {
        return 0;
    }
    if (left <= start && right >= end) {
        return tree[index];
    }
    int mid = (start + end) / 2;
    return interval_sum(start, mid, index * 2, left, right) + interval_sum(mid + 1, end, index * 2 + 1, left, right);
}

void update_tree_top_down(int start, int end, int index, int target, int diff) {
    if (target < start || target > end) {
        return;
    }
    tree[index] += diff;
    if (start == end) {
        return;
    }
    int mid = (start + end) / 2;
    update_tree_top_down(start, mid, index * 2, target, diff);
    update_tree_top_down(mid + 1, end, index * 2 + 1, target, diff);
}

void update_top_down(int n, int target, int value) {
    int diff = value - arr[target];
    arr[target] = value;
    update_tree_top_down(0, n - 1, 1, target, diff);
}

void update_bottom_up(int start, int end, int index, int target, int value) {
    if (target < start || target > end) {
        return;
    }
    if (start == end) {
        arr[target] = value;
        tree[index] = value;
        return;
    }
    int mid = (start + end) / 2;
    update_bottom_up(start, mid, index * 2, target, value);
    update_bottom_up(mid + 1, end, index * 2 + 1, target, value);
    tree[index] = tree[index * 2] + tree[index * 2 + 1];
}

int main() {
    int n = 10;
    arr = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    tree.resize(n * 4, 0);

    init(0, n - 1, 1);

    for (int val : tree) {
        cout << val << " ";
    }
    cout << endl;

    cout << interval_sum(0, n - 1, 1, 0, 9) << endl;  // 1 + 2 + ... + 10 = 55
    cout << interval_sum(0, n - 1, 1, 0, 2) << endl;  // 1 + 2 + 3 = 6
    cout << interval_sum(0, n - 1, 1, 6, 7) << endl;  // 7 + 8 = 15

    // arr[0]을 5로 수정 (Top down)
    update_top_down(n, 0, 5);
    cout << interval_sum(0, n - 1, 1, 0, 2) << endl;  // 5 + 2 + 3 = 10

    // arr[9]을 -1로 수정 (Bottom up)
    update_bottom_up(0, n - 1, 1, 9, -1);
    cout << interval_sum(0, n - 1, 1, 8, 9) << endl;  // 9 + (-1) = 8

    return 0;
}