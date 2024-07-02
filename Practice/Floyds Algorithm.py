import os

def read_matrix(filename):
    with open(filename, 'r') as f:
        n = int(f.readline().strip())
        matrix = []
        for _ in range(n):
            row = list(map(int, f.readline().strip().split()))
            matrix.append(row)
    return n, matrix

def floyd_warshall(n, dist_matrix):
    dist = [[dist_matrix[i][j] if dist_matrix[i][j] != 99999 else float('inf') for j in range(n)] for i in range(n)]
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist

def find_shortest_and_longest_paths(n, dist_matrix):
    shortest_dist = float('inf')
    longest_dist = float('-inf')
    shortest_pair = None
    longest_pair = None
    
    for i in range(n):
        for j in range(n):
            if i != j:
                if dist_matrix[i][j] < shortest_dist:
                    shortest_dist = dist_matrix[i][j]
                    shortest_pair = (i + 1, j + 1)
                if dist_matrix[i][j] > longest_dist and dist_matrix[i][j] != float('inf'):
                    longest_dist = dist_matrix[i][j]
                    longest_pair = (i + 1, j + 1)
    
    return shortest_pair, shortest_dist, longest_pair, longest_dist

# Main function
def main():
    input_file = os.path.join(os.getcwd(), 'Ex06input_dis1.txt')
    n, dist_matrix = read_matrix(input_file)
    dist_matrix = floyd_warshall(n, dist_matrix)
    shortest_pair, shortest_dist, longest_pair, longest_dist = find_shortest_and_longest_paths(n, dist_matrix)
    
    print(f"Shortest path is between vertices {shortest_pair} with distance {shortest_dist}")
    print(f"Longest path is between vertices {longest_pair} with distance {longest_dist}")

if __name__ == "__main__":
    main()
