//////////////////// Graph implementation ////////////////////
typedef struct node {
    int v;
    int dist;
    struct node* next;
} Node;

typedef struct adjList {
    Node *head;
} AdjList;

typedef struct graph {
    int numV;
    AdjList* list;
} Graph;

Node* newAdjListNode(int v, int dist) {
    Node* newNode = calloc(sizeof(Node), 1);
    newNode->v = v; newNode->dist = dist;
    return newNode;
}

Graph* createGraph(int v) {
    Graph* graph = calloc(sizeof(Graph), 1);
    graph->list = calloc(sizeof(AdjList), v);
    graph->numV = v;
    return graph;
}

void addEdge(Graph* graph, int src, int dest, int dist) {
    Node* newNode = newAdjListNode(dest, dist);
    newNode->next = graph->list[src].head;
    graph->list[src].head = newNode;

    newNode = newAdjListNode(src, dist);
    newNode->next = graph->list[dest].head;
    graph->list[dest].head = newNode;
}
//////////////////// End Graph /////////////////////////
void dfs(int node, Graph *graph, int *result, bool *visited) {
    visited[node] = true;
    Node* nei = graph->list[node].head;
    while (nei) {
        *result = fmin(*result, nei->dist);
        if (!visited[nei->v])
            dfs(nei->v, graph, result, visited);
        nei = nei->next;
    }
}

int minScore(int n, int** roads, int roadsSize, int* roadsColSize){
    Graph *graph = createGraph(n+1);
    int result = INT_MAX;
    bool *visited = calloc(sizeof(bool), n+1);
    
    for (int i = 0; i < roadsSize; i++)
        addEdge(graph, roads[i][0], roads[i][1], roads[i][2]);
    dfs(1, graph, &result, visited);

    return result;
}
