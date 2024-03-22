
#матрица граф

edge_list = [[0, 1], [0, 2], [0, 3],
             [1, 2],  [1, 4], 
             [2, 4],  
             [3, 4],
             [4, 5], 
             [5, 3]
]
vert_num = 6

'''edge_list = [[0, 1],
             [1, 2],
             [2, 3],
             [3, 4],
             [4, 0]
]
vert_num = 5'''

adj_list = [[] for _ in range(vert_num)]
for u, v in edge_list:
    adj_list[u].append(v)
print(adj_list) 



adj_matrix = [[0 for _ in range(vert_num)] for _ in range(vert_num)]

for edge in edge_list:
    u = edge[0]
    v = edge[1]
    adj_matrix[u][v] = 1
    
print(adj_matrix)    


#поиск в глубину

g = adj_list

parents = [None for _ in range(vert_num)]
colors = ["w" for _ in range(vert_num)]
timer = 0
tin = [None for _ in range(vert_num)]
tout = [None for _ in range(vert_num)]

def dfs(v, p = -1):
    global timer
    cycle = []
    cycle_last = []
    parents[v] = p
    colors[v] = "g"
    timer += 1
    tin[v] = timer
    for u in g[v]:
        if colors[u] == "g":
            cycle.append(v)
            cycle.append(u)
            for i in range(u+1, vert_num):
                if colors[i] == "g":
                    cycle.append(i)
            for i in range(0, len(cycle)):
                cycle_last.append(str(cycle[i]))
                cycle_last.append('->')
            cycle_last = cycle_last[:-1] 
            if int(cycle_last[0]) == int(cycle_last[len(cycle_last) - 1]):
                cycle_last = cycle_last[2:]
            print("found cycle:", ' '.join(cycle_last))
            continue
        elif colors[u] == "b":
            continue
        elif colors[u] == "w":
            dfs(u, v)
    colors[v] = "b"
    timer += 1
    tout[v] = timer
    
    
dfs(0)
#print(tin)
#print(colors)
print("Exit_timer:", tout)

# Топологическая сортировка (перестановка вершин графа, такая что ребра ведут слева направо)


g = adj_list

parents = [None for _ in range(vert_num)]
colors = ["w" for _ in range(vert_num)]
timer = 0
tin = [None for _ in range(vert_num)]
tout = [None for _ in range(vert_num)]

def top_sort():
    for v in range(vert_num):
        if colors[v] == "w":
            dfs(v)
    vert_list = [i for i in range(vert_num)]
    ans = [
        x for y, x in sorted(zip(tout, vert_list), key = lambda pair: pair[0], reverse = True)
    ]
    return ans

print(top_sort())

