graph=[
    [0,7,9,0,0,4],
    [7,0,10,15,0,0],
    [9,10,0,11,0,2],
    [0,15,11,0,6,0],
    [0,0,0,6,0,9],
    [4,0,2,0,9,0]
]

n=len(graph)
vis=[0]*n
par=[-1]*n
dist=[9999]*n

s=0
dist[s]=0

def relax(u,v):
    if(dist[v]>dist[u]+graph[u][v]):
        dist[v]=dist[u]+graph[u][v]
        par[v]=u

def minn():
    return min((dist[i], i) for i in range(n) if not vis[i])[1]

for i in range(n):
    u=minn()
    for v in range(n):
        if graph[u][v]!=0 and not vis[v]:
            relax(u,v)
    vis[u]=1

print(dist)
print(par)
