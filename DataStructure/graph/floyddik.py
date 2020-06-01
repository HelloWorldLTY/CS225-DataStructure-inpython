import numpy as np

#floyd
N = 4
M = float('inf')
edge = np.mat([[0,2,6,4],[M,0,3,M],[7,M,0,1],[5,M,12,0]])
A = edge[:]
path = np.zeros((N,N))
 
def Floyd():
    for i in range(N):
        for j in range(N):
            if(edge[i,j] != M and edge[i,j] != 0):
                path[i][j] = i
 
    print ('init:')
    print (A,'\n',path)
    
    for a in range(N):
        for b in range(N):
            for c in range(N):
                if(A[b,a]+A[a,c]<A[b,c]):
                    A[b,c] = A[b,a] + A[a,c]
                    path[b][c] = path[a][c]+1
 
    print ('result:')
    print (A,'\n',path)
 
print('Floyd part')
Floyd()


#dijst
Inf = float('inf')
Adjacent = [[0, 1, 12, Inf, Inf, Inf],
            [Inf, 0, 9, 3, Inf, Inf],
            [Inf, Inf, 0, Inf, 5, Inf],
            [Inf, Inf, 4, 0, 13, 15],
            [Inf, Inf, Inf, Inf, 0, 4],
            [Inf, Inf, Inf, Inf, Inf, 0]]
Src, Dst, N = 0, 5, 6
 
 
def dijstra(adj, src, dst, n):
    dist = [Inf] * n
    dist[src] = 0
    book = [0] * n # 记录已经确定的顶点
    # 每次找到起点到该点的最短途径
    u = src
    for _ in range(n-1):    # 找n-1次
        book[u] = 1 # 已经确定
        # 更新距离并记录最小距离的结点
        next_u, minVal = None, float('inf')
        for v in range(n):    # w
            w = adj[u][v]
            if w == Inf:    # 结点u和v之间没有边
                continue
            if not book[v] and dist[u] + w < dist[v]: # 判断结点是否已经确定了，
                dist[v] = dist[u] + w
                if dist[v] < minVal:
                    next_u, minVal = v, dist[v]
        # 开始下一轮遍历
        u = next_u
    print(dist)
    return dist[dst]

print('dijstra min road')
dijstra(Adjacent, Src, Dst, N)

