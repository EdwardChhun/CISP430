import heapq #Using lazyPQ took too long, I had to find a different solution

def read_file(filename):
    with open(filename, 'r') as f:
        return [[int(c) for c in line.strip()] for line in f]

def expand_grid(grid, times=5):
    rows, cols = len(grid), len(grid[0])
    full = [[0] * (cols * times) for _ in range(rows * times)]
    for i in range(rows * times):
        for j in range(cols * times):
            val = grid[i % rows][j % cols] + (i // rows) + (j // cols)
            full[i][j] = (val - 1) % 9 + 1
    return full

def dijkstra(grid):
    rows, cols = len(grid), len(grid[0])
    heap = [(0, 0, 0)]  # (cost, row, col)
    visited = [[False] * cols for _ in range(rows)]
    costs = [[float('inf')] * cols for _ in range(rows)]
    costs[0][0] = 0

    while heap:
        cost, x, y = heapq.heappop(heap)
        if visited[x][y]:
            continue
        visited[x][y] = True
        if x == rows - 1 and y == cols - 1:
            return cost
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                new_cost = cost + grid[nx][ny]
                if new_cost < costs[nx][ny]:
                    costs[nx][ny] = new_cost
                    heapq.heappush(heap, (new_cost, nx, ny))
    return -1

test_grid = read_file("15_test.txt")
test_grid_part2 = read_file("15_test_part2.txt")
full_grid = read_file("15.txt")
expanded_full_grid = expand_grid(full_grid)

print("Test Part 1:", dijkstra(test_grid))
print("Test Part 2:", dijkstra(test_grid_part2))
print("Answer Part 1:", dijkstra(full_grid))
print("Asnwer Part 2:", dijkstra(expanded_full_grid))

