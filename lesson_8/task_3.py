"""3. Написать программу, которая обходит не взвешенный ориентированный граф без петель,
в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
Примечания:
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин."""


def graph_generation(num_vert):
    # генерируем граф без петель, в котором все вершины связаны
    graph_gen = [[0 + _ for _ in range(num_vert)] for _ in range(num_vert)]

    # преобразуем граф в список смежностей
    i = 0
    while i != len(graph_gen):
        for g in graph_gen[i]:
            if i == g:
                graph_gen[i].remove(g)
        i += 1

    return graph_gen


def dfs(node):
    is_visited[node] = True
    for i in graph[node]:
        if not is_visited[i]:
            dfs(i)
    return i


nv = int(input("Введите число вершин: "))
graph = graph_generation(nv)
print(*graph, sep='\n')

is_visited = [False] * len(graph)

for j in range(len(graph)):
    if not is_visited[j]:
        print(f"Обход завершен, последняя вершина = {dfs(j)}")
