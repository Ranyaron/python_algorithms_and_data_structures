"""2. Доработать алгоритм Дейкстры (рассматривался на уроке),
чтобы он дополнительно возвращал список вершин, которые необходимо обойти."""

g = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0],
]


def dijkstra(graph, start, end):
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    parent = [-1] * length

    cost[start] = 0
    min_cost = 0

    prev = []

    while min_cost < float('inf'):

        is_visited[start] = True

        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:

                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start

        min_cost = float('inf')

        for j in range(length):
            if min_cost > cost[j] and not is_visited[j]:
                min_cost = cost[j]
                start = j

    # записываем вершины, которые необходимо обойти
    x = True
    while x:
        if cost[end] == float('inf'):
            prev.append(None)
            break
        for i in range(len(parent)):
            if i == end:
                if end == 0:
                    x = False
                    break
                prev.append(end)
                end = parent[i]
                continue
    else:
        prev.append(end)
    prev.reverse()

    return [cost, prev]


s = int(input("От какой вершины начинаем: "))
e = int(input("До какой вершины идем: "))
dijkstra = dijkstra(g, s, e)

if None is dijkstra[1][0]:
    print(f"{dijkstra[0]} - стоимость путей до каждой вершины\n"
          f"от вершины {s} до вершины {e} нет пути")
else:
    print(f"{dijkstra[0]} - стоимость путей до каждой вершины\n"
          f"{dijkstra[1]} - вершины, которые необходимо обойти от {s} до {e}")
