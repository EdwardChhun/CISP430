# Start at every "0" and do depth first search
# Constraint, next node must be equal to currNode + 1
# Keep a tally of total and add upon the amount of score from other trail heads

# Using an adjacency matrix
# we skim through the columns of each rows to find a 0 and do our searching algorithm there

# ========
# PART ONE
# ========

def foo(file):
    grid = [list(line.strip()) for line in open(file)]
    H, W = len(grid), len(grid[0])
    total_score = 0

    def dfs(r, c, grid, reached_nines):
        curr = int(grid[r][c])
        if curr == 9:
            reached_nines.add((r, c))
            return
        # explore four directions
        # direction row and direction columns
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            nr, nc = r + dr, c + dc # Exploring neighboring rows and columns
            if (0 <= nr < H and 0 <= nc < W
                and int(grid[nr][nc]) == curr + 1):
                dfs(nr, nc, grid, reached_nines)


    for r in range(H):
        for c in range(W):
            if grid[r][c] == '0':
                reached_nines = set()
                dfs(r, c, grid, reached_nines)
                total_score += len(reached_nines)
                
    return total_score

print("Part 1 test case:", foo("14_test.txt"))
print("Part 1 answer:", foo("14.txt"))

# ========
# PART TWO
# ========

# First part is how many 9's you can reach
# Second part is how many ways you can reach a single 9 for all the 0's you can reach
# bfs would be too expensive and exhausted

# Using a bottom up DP approach with dfs
def bar(file):
    grid = [list(line.strip()) for line in open(file)] 
    H, W = len(grid), len(grid[0])
    dp = [[0]*W for _ in range(H)]

    for r in range(H):
        for c in range(W):
            if grid[r][c] == '9':
                dp[r][c] = 1

    for h in range(8, -1, -1):
        for r in range(H):
            for c in range(W):
                if int(grid[r][c]) == h:
                    for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = r+dr, c+dc
                        if (0 <= nr < H and 0 <= nc < W and
                            int(grid[nr][nc]) == h+1):
                            dp[r][c] += dp[nr][nc]

    trailheads = [
        (r, c)
        for r in range(H)
        for c in range(W)
        if grid[r][c] == '0'
    ]
    return sum(dp[r][c] for r, c in trailheads)
    
print("Part 2 test case:", bar("14_test.txt"))
print("Part 2 answer:", bar("14.txt"))
