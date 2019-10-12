#Assignment 2
from as2_tree import Tree
class Result:
	def __init__(self, sol=[], val=-1000):
			self.solution = sol
			self.value = val
			
class MNX:
	def __init__(self, data_list):
		self.tree = Tree()	
		self.tree.init_tree(data_list)
		self.root = self.tree.root
		self.currentNode = None
		self.successors = []		
		return
        
	def terminalTest(self, node):
		assert node is not None
		return len(node.children) == 0

	def utilityChecking(self, node):
		assert node is not None
		return node.value

	def getChildren(self, node):
		assert node is not None
		return node.children

	def minimax(self):	
		terminal_val = self.max_v(self.root)
		traversed=[] #example of solution_array
		res=Result()
		self.currentNode=self.root
		traversed.append(self.root.Name) 
		while(self.terminalTest(self.currentNode)==False):
			self.successors = self.getChildren(self.currentNode)
			for successor in self.successors:
				if(self.utilityChecking(successor)==terminal_val):
					traversed.append(successor.Name)
					self.currentNode=successor		
		res.solution=traversed
		res.value=terminal_val
		return res

	def max_v(self, node):		
		if self.terminalTest(node):
			return self.utilityChecking(node)		
		max_v = -1000 #we use 1000 as the initial_maximum value
		deeper_layer = self.getChildren(node)
		for deeper_node in deeper_layer:
			max_v = max(max_v, self.min_v(deeper_node))
		node.value=max_v
		return max_v

	def min_v(self, node):		
		if self.terminalTest(node):
			return self.utilityChecking(node)
		min_v = 1000 #we use -1000 as the initial_minimum value
		deeper_layer = self.getChildren(node)
		for deeper_node in deeper_layer:
			min_v = min(min_v, self.max_v(deeper_node))
		node.value=min_v
		return min_v
