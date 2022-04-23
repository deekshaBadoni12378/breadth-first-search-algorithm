

def bfs(vc, graph, cn):
    vc.append(cn)
    queue = []
    queue.append(cn)
 
    while queue:
        s = queue.pop(0)
        print(s)
 
        for branch in graph[s]:
            if branch not in vc:
                vc.append(branch)
                queue.append(branch)
 

	
	
				

graph = {
    'A': ['B', 'C', "D"],
    'B': ['E', "F"],
    'C': ['G', "I"],
    'D': ['I'],
    'E': ['G','F'],
    "F": ['I','C'],
    'G': ['A','B'],
    "I": ['B','C']
}
bfs([], graph, 'D')