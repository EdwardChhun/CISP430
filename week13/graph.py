from itertools import permutations

def compute_route_distance(order, matrix):
    """Sum distances along the given permutation of indices."""
    total = 0
    for i in range(len(order) - 1):
        total += matrix[order[i]][order[i+1]]
    return total

def solve(distances):
    """
    distances: dict of (city1, city2) -> dist (undirected)
    returns (shortest, longest)
    """
    # Map each city to an index
    cities = sorted({c for pair in distances for c in pair})
    idx    = {city: i for i, city in enumerate(cities)}
    n      = len(cities)

    # Build adjacency matrix
    mat = [[0]*n for _ in range(n)]
    for (u, v), d in distances.items():
        i, j = idx[u], idx[v]
        mat[i][j] = d
        mat[j][i] = d

    # permutations
    shortest = float('inf')
    longest  = 0
    for perm in permutations(range(n)):
        dist = compute_route_distance(perm, mat)
        shortest = min(shortest, dist)
        longest  = max(longest,  dist)

    return shortest, longest

if __name__ == "__main__":
    test_distances = {}
    with open("13_test.txt") as fin:
        for line in fin:
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            # e.g. ["London","to","Dublin","=","464"]
            city1, city2, dist = parts[0], parts[2], int(parts[4])
            test_distances[(city1, city2)] = dist

    test_short, test_long = solve(test_distances)
    print("ANSWERS FROM 13_test.TXT")
    print("Test shortest route:", test_short)  
    print("Test longest  route:", test_long)   
    print()

    distances = {}
    with open("13.txt") as fin:
        for line in fin:
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            city1, city2, dist = parts[0], parts[2], int(parts[4])
            distances[(city1, city2)] = dist

    shortest, longest = solve(distances)
    print("ANSWERS FROM 13.TXT")
    print("Shortest route distance:", shortest)
    print("Longest  route distance:",  longest)
