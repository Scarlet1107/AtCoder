def read_matrix(filename):
    with open(filename, 'r') as f:
        n = int(f.readline().strip())
        matrix = []
        for _ in range(n):
            row = list(map(int, f.readline().strip().split()))
            matrix.append(row)
    return n, matrix

def warshall_algorithm(n, adj_matrix):
    reach = [[adj_matrix[i][j] for j in range(n)] for i in range(n)]
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])
    
    return reach

def find_unreachable_vertices(n, reach_matrix):
    unreachable_vertices = []
    for j in range(n):
        reachable = False
        for i in range(n):
            if reach_matrix[i][j] == 1:
                reachable = True
                break
        if not reachable:
            unreachable_vertices.append(j + 1)
    return unreachable_vertices

# Main function
def main():
    input_file = 'Ex06input_adj.txt'
    n, adj_matrix = read_matrix(input_file)
    reach_matrix = warshall_algorithm(n, adj_matrix)
    unreachable_vertices = find_unreachable_vertices(n, reach_matrix)
    print("Unreachable vertices from any other vertices:", unreachable_vertices)

if __name__ == "__main__":
    main()
