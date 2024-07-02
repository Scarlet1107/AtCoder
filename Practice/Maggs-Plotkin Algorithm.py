import os

def read_matrix(filename):
    with open(filename, 'r') as f:
        n = int(f.readline().strip())
        matrix = []
        for _ in range(n):
            row = list(map(int, f.readline().strip().split()))
            matrix.append(row)
    return n, matrix

def prim_algorithm(n, graph):
    key = [float('inf')] * n
    parent = [None] * n
    key[0] = 0
    mst_set = [False] * n
    
    for _ in range(n):
        min_key = float('inf')
        u = -1
        
        for v in range(n):
            if not mst_set[v] and key[v] < min_key:
                min_key = key[v]
                u = v
        
        mst_set[u] = True
        
        for v in range(n):
            if graph[u][v] != 99999 and not mst_set[v] and graph[u][v] < key[v]:
                key[v] = graph[u][v]
                parent[v] = u
    
    mst_weight = 0
    for i in range(1, n):
        if parent[i] is not None:
            mst_weight += graph[i][parent[i]]
    
    return mst_weight

# Main function
def main():
    input_file = os.path.join(os.getcwd(), 'Ex06input_dis2.txt')
    n, graph = read_matrix(input_file)
    mst_weight = prim_algorithm(n, graph)
    print(f"Total weight of the Minimum Spanning Tree is {mst_weight}")

if __name__ == "__main__":
    main()
