from itertools import permutations

INF = float('inf')


def tsp_brute_force(cost, n):
    """
    Brute Force solution for Travelling Salesman Problem
    """

    cities = list(range(1, n))
    best_cost = INF
    best_path = None

    for perm in permutations(cities):

        path = [0] + list(perm) + [0]

        current_cost = 0

        for i in range(n):
            current_cost += cost[path[i]][path[i + 1]]

        if current_cost < best_cost:
            best_cost = current_cost
            best_path = path

    return best_path, best_cost


# ---------------- Cost Matrix ----------------

cost = [
    [INF, 10, 8, 9, 7],
    [10, INF, 10, 5, 6],
    [8, 10, INF, 8, 9],
    [9, 5, 8, INF, 6],
    [7, 6, 9, 6, INF]
]

cities = ['A', 'B', 'C', 'D', 'E']
n = len(cost)

best_path, best_cost = tsp_brute_force(cost, n)

print("5-City TSP - Cost Matrix:\n")

print("      ", end="")
for city in cities:
    print(f"{city:>5}", end="")
print()

for i in range(n):
    print(f"{cities[i]:>3}", end="")

    for j in range(n):
        if cost[i][j] == INF:
            print(f"{'INF':>6}", end="")
        else:
            print(f"{cost[i][j]:>6}", end="")

    print()

print("\nOptimal Tour:", " -> ".join(cities[i] for i in best_path))
print("Minimum Cost:", best_cost)

print("\nPath verification:\n")

for i in range(n):
    u = best_path[i]
    v = best_path[i + 1]

    print(f"{cities[u]} -> {cities[v]}: cost = {cost[u][v]}")