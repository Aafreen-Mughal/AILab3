#TASK 1(A)

tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': [],
    'F': ['I'],
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

    def dls(self, graph, start, goal, depth_limit):
        visited = []

        def dfs(node, depth):
            if depth > depth_limit:
                return None
            visited.append(node)
            if node == goal:
                print(f"Goal found with DLS, Path: {visited}")
                return visited

            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    path = dfs(neighbor, depth + 1)
                    if path:
                        return path

            visited.pop()
            return None

        return dfs(start, 0)

print("Visiting tree using DLS.....")
environment = Environment(tree)
agent = Agent()
result = agent.dls(tree, 'A', 'I', 4)
if not result:
    print("Goal not found within the depth limit.")
