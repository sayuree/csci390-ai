#Author: Dinh-Mao Bui, Anh-Tu Nguyen
#Rule of traversing: Alphabetical ordered, then left to right, 
#Points: 2
def traverse(tree, init):    	
	queue = [init]
	traversed = []
	while queue:
		node = queue.pop(0)
		if node not in traversed:
			traversed.append(node)
			leaves = tree[node]
			for leaf in leaves:
				queue.append(leaf)
	return traversed

#Points: 3
def pathfinder(tree, init, goal):
	traversed = []
	queue = [[init]]
	if init == goal:
		return "No kidding, pls"
	while queue:
		traversed=queue.pop(0)
		node=traversed[-1]
		leaves=tree[node]
		for leaf in leaves:
			if leaf not in traversed:
				if leaf==goal:
					return traversed+[leaf]
					break
			queue.append(traversed+[leaf])
	return "No such path exists"
