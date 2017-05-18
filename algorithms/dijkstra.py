#This is a basic implementation of Dijkstra's Algorithm
#Andy Miller
#2017/5/18

#This might not make sense to anyone but me.
#Use 3 dictionaries. Parents, Weights, Total

#First we need something to determine cost:
def find_lowest_cost_node(costs):
	lowest_cost = float('inf')
	lowest_cost_node = None
	for node in costs:
		cost = costs[node]
		if cost < lowest_cost and node not in processed:
			lowest_cost = cost
			lowest_cost_node = node
	return lowest_cost_node

#You'll need a dict for each node.

#Your dictionaries for finding nodes and lowest costs:
graph = {}
costs = {}
parents = {}
processed = []

#Dijkstra:
node = find_lowest_cost_node(costs)
while node is not None:
	cost = costs[node]
	neighbors = graph[node]
	for n in neighbors.keys():
		new_cost = cost + neighbors[n]
		if costs[n] > new_cost:
			costs[n] = new_cost
			parents[n] = node
	processed.append(node) #marking processed to not double check
	node = find_lowest_cost_node(costs) #next node

#You'll need to edit this a bit depending on your networks set-up.
#Remember, no cycles, no negative weights.
#Dijkstra's can't do Markov or Boltzmann chains.