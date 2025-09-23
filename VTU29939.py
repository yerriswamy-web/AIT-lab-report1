
def create_graph():
    graph={}
n=int(input("enter no of nodes"))
for i in range(n):
    node=input(f"enter the namse of the node {i+1}")
graph[node]=[]
e=int(input("enter the no of edges(paths):"))
for i in range(e):
    src=input("enter source node for edges[i+1}:")
dest=input("enter destination node for edge{i+1};")
if src in graph and dest in graph:
           graph[src].append(dest)
else:
     print("error one of the nodes'{src}' or '{dest]' does not exist")
def dfs(graph,node,visited=None):
                if visisted is None:
                    visisted=set()
                    if node not in visited:
                        print(f"visited:{node}")
                        visited.add(node)
                        for neighbor in graph[node]:
                            dfs(graph,neighbor,visited)
                            def bfs(graph,start):
                                visisted=set()
                                queue=deque([start])
                                while queue:
                                    node=queue.popleft()
                                    if node not in visited:
                                        print(f"visited:{node}")
                                        visited.add(node)
                                        for neighbor in graph[node]:
                                            if neighbor not in visited:
                                                queue.append(neighbor)
                                                def main():
                                                    print("=====graph creation =====")
                                                    graph=create-graph()
                                                    print("\n======grapg structure =====")
                                                    for node,neighbors in graph.items():
                                                        print(f"{node}->{neighbors}")
                                                        start=input("\enter starting node for traversal :")
                                                        if start not in graph:
                                                            print("invalid starting node")
                                                        return
                                                        print("\n ==dfs Traversal==")
                                                        dfs(graph,start)
                                                        print("\n =====BFS traversal=====")
                                                        bfs(graph,start)
                                                        if__name__="__main__";
                                                        main()
                                
                              
