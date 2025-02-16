Dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
class Environment:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])

    def isSafe(self, x, y):
        if (x >= 0 and x < self.rows) and (y >= 0 and y < self.cols) and self.grid[x][y] != 1:
            return True
        return False

    def traversal(self, item):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j] == item:
                    return (i, j)
        return 0

def bfs(environment):
    start = environment.traversal('S')
    goal = environment.traversal('G')

    if not start or not goal:
        return "source and destination are not defined!"

    queue=[start] #store urrent pos
    queue_path=[[start]] #store current path
    visited=set([start])

    while queue:
        (x, y)=queue[0] #get co-ord for current pos
        path = queue_path[0] 
        queue = queue[1:]#remove path now 
        queue_path = queue_path[1:] 

        if (x, y) == goal:
           return path

        for dx,dy in Dir:
            nx,ny=x+dx,y+dy
            nPos=(nx, ny)

            if environment.isSafe(nx, ny) and nPos not in visited:
                queue.append(nPos) 
                queue_path.append(path+[nPos]) 
                visited.add(nPos)#mark visited 

    return "No path found!"
def display_path(self,path):
    for i in range(self.rows):
        for j in range(self.cols):
            if (i, j) in path:
              print(f"({i},{j})",end=' -> ')

arr=[[1, 0, 0, 1, 'G'],
    [1, 1, 0, 1, 0],
    [0, 1, 'S', 0, 0],
    [0, 0, 0, 1, 0]
]
print("TRAVERSING USING BFS......",end=' ')
environment = Environment(arr)
s_path = bfs(environment)
print("\nShortest path to reach G...")
display_path(environment,s_path)