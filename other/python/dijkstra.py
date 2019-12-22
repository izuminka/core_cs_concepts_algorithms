from math import inf

class Node(object):

	def __init__(self, name):
		self.name = name # remove when done debugging
		self.cost = inf
		self.path_cost_daughters = [] # cost the daughter, daughter node
		self.main_parent = None
		self.addedQue = False # rename to addedQue
		self.finalNode=False

	def better_parent_update(self,new_parent_name, new_cost):
			self.cost = new_cost
			self.main_parent = new_parent_name
			self.addedQue = True


# Input the graph
num_nodes = 10
nodes = [Node(n) for n in range(num_nodes)]

# Input edges of the graph and corresponding neighbors
nodes[0].path_cost_daughters = [(20,nodes[1]), (25, nodes[2])]
nodes[1].path_cost_daughters = [(15,nodes[3]), ( 5, nodes[4])]
nodes[2].path_cost_daughters = [( 5,nodes[4]), ( 7, nodes[5]), (10, nodes[6])]
nodes[3].path_cost_daughters = [(10,nodes[8])]
nodes[4].path_cost_daughters = [(35,nodes[8]), (11,nodes[7]), ( 5,nodes[5]), ( 5,nodes[2])]
nodes[5].path_cost_daughters = [( 5,nodes[4]), ( 2, nodes[7])]
nodes[6].path_cost_daughters = [( 5,nodes[7])]
nodes[7].path_cost_daughters = [(11,nodes[4]), ( 10,nodes[8])]
nodes[8].path_cost_daughters = [(10,nodes[7])]

#set initial and final nodes
start_node = 0
end_node = 8
nodes[start_node].cost = 0
nodes[end_node].finalNode = True


# Perform the search O(n^2)
que = [nodes[start_node]]
for c_node in que:
	for path_cost, d_node in c_node.path_cost_daughters:
		cost_to_d_node = path_cost + c_node.cost
		if not d_node.addedQue:
			que.append(d_node)
			d_node.better_parent_update(c_node.name, cost_to_d_node)
		elif (d_node.cost > cost_to_d_node):
			d_node.better_parent_update(c_node.name, cost_to_d_node)

# print out the most optimal path
node_name = end_node
while(node_name != None):
	print(node_name)
	node_name = nodes[node_name].main_parent










# def get_min_cost_node(dict_nodes, visited_nodes):
# 	"""
# 	look through all the unvisited nodes and pick the one with lowest cost
# 	"""
# 	min_val = inf
# 	min_node_name = None
# 	for k in dict_nodes:
# 		if k not in visited_nodes:
# 			if dict_nodes[k].cost <= min_val:
# 				min_val = dict_nodes[k].cost
# 				min_node_name = k
# 	return dict_nodes[min_node_name]



# # Input the graph
# node_names = ['a', 'b', 'c', 'd']
# dict_nodes = {nn:Node(nn) for nn in node_names}

# # Input edges of the graph and corresponding neighbors
# dict_nodes['a'].path_cost_daughters = [(10,dict_nodes['c']), (5, dict_nodes['d'])]
# # b no daughters
# dict_nodes['c'].path_cost_daughters = [(2, dict_nodes['b'])]
# dict_nodes['d'].path_cost_daughters = [(4, dict_nodes['c']), (20, dict_nodes['b'])]

# #set initial and final nodes
# start_node = 'a'
# dict_nodes[start_node].cost = 0
# end_node = 'b'
# dict_nodes[end_node].finalNode = True

# # Input the graph
# node_names = ['a', 'b', 'c', 'd','e','f']
# dict_nodes = {nn:Node(nn) for nn in node_names}

# # Input edges of the graph and corresponding neighbors
# dict_nodes['a'].path_cost_daughters = [(20,dict_nodes['b']), (15, dict_nodes['c'])]
# dict_nodes['b'].path_cost_daughters = [(10,dict_nodes['d']), (2, dict_nodes['e'])]
# dict_nodes['c'].path_cost_daughters = [(10,dict_nodes['d']), (10, dict_nodes['e'])]
# dict_nodes['d'].path_cost_daughters = [(7, dict_nodes['f'])]
# dict_nodes['e'].path_cost_daughters = [(6,dict_nodes['f'])]

# #set initial and final nodes
# start_node = 'a'
# end_node = 'f'
# dict_nodes[start_node].cost = 0
# dict_nodes[end_node].finalNode = True


# # Perform the search
# expanded_nodes = []
# while(True):
# 	c_node = get_min_cost_node(dict_nodes, expanded_nodes)
# 	if (c_node.cost == inf) or (c_node.finalNode and not c_node.unvisited):
# 		break
# 	else:
# 		for path_cost, d_node in c_node.path_cost_daughters:
# 			cost_to_d_node = path_cost + c_node.cost
# 			if (d_node.unvisited) or (d_node.cost > cost_to_d_node):
# 				d_node.better_parent_update(c_node.name, cost_to_d_node)
# 		c_node.unvisited = False
# 		expanded_nodes.append(c_node.name)


# # print out the most optimal path
# node_name = end_node
# while(node_name != None):
# 	print(node_name)
# 	node_name = dict_nodes[node_name].main_parent
