# There is a constraint on the containers, I can only use the ones given
# After each step, a container is removed from the list

# NOTE: The list of containers is going to decrease every step
# Bottom up approach by iterating backwards, so we don't have duplicate containers

# Need to print the list required to bring
def foo(liters: int, containers: list[int]) -> tuple[int, list[int]]:
    
    # Contruct dp array 0...liters + 1
    dp = [float('inf')]*(liters + 1)
    curr_containers = [-1]*(liters + 1)
    
    # Base case, it takes 0 containers to hold 0 liters 
    dp[0] = 0
    
    # Construct a bottom up approach by solving subproblems
    # dp[1],..., dp[liters]

    
    for container in containers:
        for i in range(liters, container-1, -1):
            if container <= i and dp[i-container] + 1 < dp[i]:
                # Compare the current steps with the new steps to find min
                # we add 1 because we used a step by subtracting or taking away 
                # the container's amount of liters from total liters
                dp[i] = dp[i - container] + 1 
                curr_containers[i] = container 
    
    if dp[liters] == float('inf'):
        return (-1,[])
    
    # example Liter=25, Containers=[20, 15, 10, 5, 5] 
    # then, curr_containers=[20, 15, 10, 10, 5]
    
    # We would need to clean the curr_containers to have only the required ones, especially the min amount.
    result = []
    remaining = liters
    while remaining > 0:
        result.append(curr_containers[remaining])
        remaining -= curr_containers[remaining]

    return (dp[liters], sorted(result))
        

if __name__ == "__main__":
    
    new_containers = []
    with open("7.txt", 'r') as f:
        for i in f:
            new_containers.append(int(i.strip("\n")))
            
    liters = 25
    containers = [20, 15, 10, 5, 5] 
    
    print("Test case part 1 and part 2 included: ")
    print(foo(25, containers))
    print("(# of containers, list[containers]) is what you are reading above")
    
    print("\nAnswer for part 2: ")
    print(foo(395, new_containers))