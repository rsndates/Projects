import networkx as nx
import sys
import matplotlib.pyplot as plt



#  Unity Id (rsdates)
# CSC 520
# NC State Univ
#

# Properties
searchtype= sys.argv[1]
srccityname= sys.argv[2]
destcityname= sys.argv[3]
tempList = []
finalList = []
data = dict()
flag = False
expandCount = 0
# plt.show()
# Set up graph tree
G=nx.Graph()

G.add_node("arad", visited=False)
G.add_node("bucharest", visited=False)
G.add_node("craiova", visited=False)
G.add_node("dobreta", visited=False)
G.add_node("eforie", visited=False)
G.add_node("fagaras", visited=False)
G.add_node("giurgiu", visited=False)
G.add_node("hirsova", visited=False)
G.add_node("iasi", visited=False)
G.add_node("lugoj", visited=False)
G.add_node("mehadia", visited=False)
G.add_node("neamt", visited=False)
G.add_node("oradea", visited=False)
G.add_node("pitesti", visited=False)
G.add_node("rimnicu_vilcea", visited=False)
G.add_node("sibiu", visited=False)
G.add_node("timisoara", visited=False)
G.add_node("urziceni", visited=False)
G.add_node("vaslui", visited=False)
G.add_node("zerind", visited=False)


G.add_edge("oradea", "zerind")
G.add_edge("zerind", "arad")
G.add_edge("arad", "timisoara")
G.add_edge("timisoara", "lugoj")
G.add_edge("lugoj", "mehadia")
G.add_edge("dobreta", "mehadia")
G.add_edge("oradea", "sibiu")
G.add_edge("arad", "sibiu")
G.add_edge("dobreta", "craiova")
G.add_edge("sibiu", "rimnicu_vilcea")
G.add_edge("sibiu", "fagaras")
G.add_edge("rimnicu_vilcea", "craiova")
G.add_edge("pitesti", "craiova")
G.add_edge("rimnicu_vilcea", "pitesti")
G.add_edge("bucharest", "pitesti")
G.add_edge("bucharest", "fagaras")
G.add_edge("bucharest", "giurgiu")
G.add_edge("bucharest", "urziceni")
G.add_edge("vaslui", "urziceni")
G.add_edge("hirsova", "urziceni")
G.add_edge("hirsova", "eforie")
G.add_edge("vaslui", "iasi")
G.add_edge("neamt", "iasi")



# nx.draw(G)
# plt.savefig("test")


# Define functions

def DFS(srcCityNode, destCityNode):
    global flag
    global expandCount
    G.node[srcCityNode]['visited'] = True
    tempList.append(srcCityNode)
    # Check if node on top is the goal node
    if srcCityNode == destCityNode:
        flag = True

    for key in sorted(G.neighbors_iter(srcCityNode)):
        if G.node[key]['visited'] == False:
            if flag:
                break
                return expandCount
            expandCount = expandCount + 1
            DFS(key, destCityNode)
    return expandCount


def BFS(scrCityNode, destCityNode):
    global expandCount
    tempQueue = []
    G.node[scrCityNode]['visited'] = True
    tempQueue.append(scrCityNode)
    while tempQueue:
        topNode = tempQueue.pop(0)
        tempList.append(topNode)
        if topNode == destCityNode:
            return expandCount
        for key in sorted(G.neighbors_iter(topNode)):
            if G.node[key]['visited'] == False:
                G.node[key]['visited'] = True
                tempQueue.append(key)

        expandCount = expandCount + 1
    return expandCount

if searchtype == "BFS" or searchtype == "bfs":
    print('The expansion count is',BFS(srccityname, destcityname))

if searchtype == "DFS" or searchtype == "dfs":
    print('The expansion count is',DFS(srccityname, destcityname))

print('The path is',tempList)
print('The length of the list is',len(tempList))