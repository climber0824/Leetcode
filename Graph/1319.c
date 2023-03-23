/*
//use dfs
//adjacency_list
//to connect n nodes you need to have n-1 edges
// if you have number of edges > number of connected components
// if yes then no of connected components is the answer
struct adj_list {
    int key;
    struct adj_list *next;
};

struct adj_list *new_node(struct adj_list *node, int key) {
    struct adj_list *temp = malloc(sizeof(struct adj_list));
    temp->key = key;
    temp->next = node;
    return temp;
}

void make_adj_list(struct adj_list *adj_list[], int n, int **connections, int connectionSize) {
    for (int i = 0; i < n; i++) {
        adj_list[i] = NULL;
    }
    for (int i = 0; i < connectionSize; i++) {
        adj_list[connections[i][0]] = new_node(adj_list[connections[i][0]], connections[i][1]);
        adj_list[connections[i][1]] = new_node(adj_list[connections[i][1]], connections[i][0]);
    }
}

//number of nodes is n
//this implies that minimum number of edges to connect every node will be n-1
//counted the number of edges using dfs
// edges_count is incremented every time a new node is pushed into the stack
//stack is implicit in this case because I am using recursive DFS is used instead of iterative where actual stack is used
void dfs(int i, struct adj_list *adj_list[], int n, bool visited[]) {
    if (visited[i]) return;
    visited[i] = true;
    struct adj_list *temp;
    temp = adj_list[i];
    while (temp) {
        if (!visited[temp->key]) {
            dfs(temp->key, adj_list, n, visited);
        }
        temp = temp->next;
    }
}

int makeConnected(int n, int **connections, int connectionsSize, int *connectionsColSize)
{   
    struct adj_list *adj_list[n];
    make_adj_list(adj_list, n, connections, connectionsSize);
    
    bool visited[n];
    for (int i = 0; i < n; i++) {
        visited[i] = false;
    }
    
    //each DFS will visit all the nodes connected to the source vertex hence number of dfs calls is the number of connected components
    int comps = 0;
    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            comps++;
            dfs(i, adj_list, n, visited);
        }
    }
    //no of edges is less than minimum no of edges required implies connecting every node is impossible
    // the number of elements in connections is the number of edges in the graph 
    if (connectionsSize < n - 1)
        return -1;
    
    //if connectionSize is > n-1 then it means there are enough edges
    //if there are 'n' connected components then we have to shift n-1 connected components to connect them all
    return comps - 1;
}
*/
// DSU
typedef struct DSU{
    int* rank;
    int* root;
}DSU;
//create disjoint-set object
DSU* createDSU(int size){
    DSU* dsu = malloc(sizeof(DSU));
    dsu->rank = calloc(size, sizeof(int));
    dsu->root = malloc(size * sizeof(int));
    for(int i = 0; i < size; i++)
        dsu->root[i] = i;
    return dsu;
}
//find root of element
int find(int* root, int x){
    if(x == root[x])
        return x;
    return root[x] = find(root, root[x]);
}
//unite the roots of two sets
void setUnion(int* root, int* rank, int x, int y){
    int rootX = find(root, x);
    int rootY = find(root, y);
    if(rootX != rootY){
        if(rank[rootX] > rank[rootY])
            root[rootY] = rootX;
        else if(rank[rootY] > rank[rootX])
            root[rootX] = rootY;
        else{
            root[rootX] = rootY;
            rank[rootY]++;
        }
    }
}
//free dsu object
void freeDSU(DSU* dsu, int size){
    free(dsu->root);
    free(dsu->rank);
    free(dsu);
}

int makeConnected(int n, int** connections, int connectionsSize, int* connectionsColSize){
    if(connectionsSize < n - 1)//edge case: not enough connections to connect all devices
        return -1;

    int networks = n;//network count starts with amount of total devices
    DSU* dsu = createDSU(n);//create our disjoint set object
    int* root = dsu->root;
    int* rank = dsu->rank;

    for(int i = 0; i < connectionsSize; i++){
        int computer1 = connections[i][0];
        int computer2 = connections[i][1];
        //if computers are on different networks
        if(find(root, computer1) != find(root, computer2)){
            setUnion(root, rank, computer1, computer2);//connect computers
            networks--;//we've connected two computers, there is now one less network
        }
    }
    freeDSU(dsu, n);//free our dsu object to avoid memory leaks
    return networks - 1;//number of connections left to make will be number of networks > 1.
}
