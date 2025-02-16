#TASK 1(B)
import heapq
tree = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3), ('G', 1)],
    'D': [('H', 3)],
    'E': [],
    'F': [('I', 1)],
    'G': [],
    'H': [],
    'I': []
}

class Environment:
    def __init__(self, tree):
        self.tree = tree
        self.current_node = None

    def get_percept(self, node):
        self.current_node = node
        return self.tree[node]

    def is_goal(self, node, goal):
        return node == goal

class Agent:
    def __init__(self):
        pass

    def ucs(self, graph, start, goal):
        frontier=[(0,start)]
        visited=set()
        costSoFar={start: 0}
        startPoint={start: None}

        while frontier:
            currentCost, currentNode = heapq.heappop(frontier)#Pop the low cost node
            if currentNode in visited:
                continue
            visited.add(currentNode)
            if currentNode == goal:
                path = []
                while currentNode is not None:
                    path.append(currentNode)
                    currentNode = startPoint[currentNode]
                path.reverse()
                print(f"Goal found with UCS. Path: {path}, Total Cost: {currentCost}")
                return path, currentCost
            for neighbor, cost in graph[currentNode]:
                newCost = currentCost+cost
                if neighbor not in costSoFar or newCost < costSoFar[neighbor]:
                    costSoFar[neighbor] = newCost
                    startPoint[neighbor] = currentNode
                    heapq.heappush(frontier, (newCost, neighbor))

        print("Goal not found")
        return None

print("Visiting tree using UCS.....")
environment = Environment(tree)
agent = Agent()
result = agent.ucs(tree, 'A', 'I')

if not result:
    print("Goal not found.")
