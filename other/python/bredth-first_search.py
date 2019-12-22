graph = {
	'0':['00', '01', '02'],
	'00':['000', '001', '01'],
	'01':['001', '010', '012', '02'],
	'02':['01', '020', '021'],
	'000':['00'],
	'001':['00', '0010'],
	'010':['01', '0010'],
	'012':['01', '0010', '0120'],
	'020':['02', '012'],
	'0120':['012', '021'],
	'021':['012', '02'],
	'0010':['010']
}


# init_n = '0'
# end_n = '0120'
# current_n = init_n
# visited = []

# def breadth_first(old_que, graph, visited):
# 	new_que = []
# 	for n0 in old_que:
# 		if n0 not in visited:
# 			if n0 != end_n:
# 				visited.append(n0)
# 			else:
# 				return visited
# 		for n00 in graph[n0]:
# 			if n00 not in new_que:
# 				new_que.append(n00)
# 	return breadth_first(new_que, graph, visited)

# visited = breadth_first([init_n], graph, [])
def checkNode(n, end_n):
	if n == end_n:
		return True
	else:
		return False

init_n = '0'
end_n = '0120'

visited = []
que = [init_n]

for n in que:
	if n not in visited:
		if checkNode(n, end_n):
			print('found')
			break
		else:
			visited.append(n)
			for n_new in graph[n]:
				if n_new not in que:
					que.append(n_new)
