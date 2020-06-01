tinyEWG_txt = """
{
    0:[(6,0.58),(2,0.26),(4,0.38),(7,0.16)],
    1:[(3,0.29),(2,0.36),(7,0.19),(5,0.32)],
    2:[(6,0.40),(7,0.34),(1,0.36),(0,0.26),(3,0.17)],
    3:[(6,0.52),(1,0.29),(2,0.17)],
    4:[(6,0.93),(0,0.38),(7,0.37),(5,0.35)],
    5:[(1,0.32),(7,0.28),(4,0.35)],
    6:[(4,0.93),(0,0.58),(3,0.52),(2,0.40)],
    7:[(2,0.34),(1,0.19),(0,0.16),(5,0.28)]
}
"""

## 模拟优先队列
class Min_PQ_:
    def __init__(self,f,reversed= False):
        self.data = []
        self.f = f
        self.__reversed = reversed
    def remove(self):
        return self.data.pop(0)
    def insert(self,item):
        self.data.append(item)
        self.data.sort(key=self.f,reverse=self.__reversed)
    def __len__(self):
        return len(self.data)
    def __str__(self):
        return str(self.data)



# 补全edge
def fill(g):
    for v in g:
        for i in range(0,len(g[v])):
            g[v][i] = (v,)+g[v][i]



def mst_prim(g):
    visited = set()
    pq = Min_PQ_(lambda x:x[-1])
    mst = []
    def visit(v):
        visited.add(v)
        for edge in g.get(v,[]):
            pq.insert(edge)
    visit(0)
    while pq:
        min_edge = pq.remove()
        x,y = min_edge[0],min_edge[1]
        if x in visited and y in visited:
            continue
        else:
            mst.append(min_edge)
            if x not in visited:
                visit(x)
            if y not in visited:
                visit(y)
    return mst




def get_edges_set(g):
    s = set()
    for v in g:
        for e in g.get(v,[]):
            a,b,weight = e[0],e[1],e[-1]
            if a<b:
                s.add((a,b,weight))
            else:
                s.add((b,a,weight))
    return s


def add_edge(g,x,y):
    if x in g:
        (g[x]).append(y)
    else:
        g[x]=[]
        add_edge(g,x,y)

def has_connected(g,x,y):
    has_connected__ = False
    visited = set()
    def __dfs(__x):
        visited.add(__x)
        for v in g.get(__x,[]):
            if v == y :
                nonlocal has_connected__
                has_connected__ = True
                return
            elif v not in visited:
                __dfs(v)
    __dfs(x)
    return has_connected__



def mst_kruskal(g):
    sorted_edges = list(get_edges_set(g))
    sorted_edges.sort(key = lambda x:x[-1])
    mst = []
    g_temp = dict()
    while sorted_edges:
        min_edge = sorted_edges.pop(0)
        x,y = min_edge[0],min_edge[1]
        if has_connected(g_temp,x,y): continue
        else:
            mst.append(min_edge)
            add_edge(g_temp,x,y)
            add_edge(g_temp,y,x)

    return mst

if __name__ == '__main__':
    g = eval(tinyEWG_txt)
    fill(g)
    print(mst_prim(g))