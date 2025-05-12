
#include <algorithm>
#include <iostream>
#include <vector>



using namespace std;

void topologicalSort(int node, vector<int>& visited, vector<int>& result, const vector<vector<int>>& graph) {
    visited[node] = 1; 

    for (int neighbor : graph[node]) {
        if (!visited[neighbor]) {
            topologicalSort(neighbor, visited, result, graph);
        }
    }
    result.push_back(node);
}

int main() {
    int n, m;
    cin >> n >> m; 
    vector<vector<int>> graph(n + 1); 
    vector<int> indegree(n + 1, 0);

    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        graph[u].push_back(v);
        indegree[v]++; 
    }

    vector<int> visited(n + 1, 0); 
    vector<int> result; 

    for (int i = 1; i <= n; ++i) {
        if (!visited[i]) {
            topologicalSort(i, visited, result, graph);
        }
    }

    reverse(result.begin(), result.end());

    for (int i = 0; i < n; ++i) {
        cout << result[i] << " "; 
    }
    cout << endl;

    return 0;
}