def conflict_free_team(n, conflicts, expertise):
    # Graph to represent conflicts
    graph = [[0] * n for _ in range(n)]
    for emp1, emp2 in conflicts:
        graph[emp1 - 1][emp2 - 1] = 1
        graph[emp2 - 1][emp1 - 1] = 1

    max_expertise_value = 0
    
    # Iterating through all possible team combinations
    for i in range(1 << n):
        total_expertise = 0
        valid_team = True
        for j in range(n):
            if (i & (1 << j)) != 0:
                total_expertise += expertise[j]
                for k in range(j):
                    if (i & (1 << k)) != 0 and graph[j][k] == 1:
                        valid_team = False
                        break
            if not valid_team:
                break
        if valid_team:
            max_expertise_value = max(max_expertise_value, total_expertise)

    return max_expertise_value

n, c = map(int, input().split())
conflicts = []
for _ in range(c):
    emp1, emp2 = map(int, input().split())
    conflicts.append((emp1, emp2))
expertise = list(map(int, input().split()))

print(conflict_free_team(n, conflicts, expertise))


    
    
    
