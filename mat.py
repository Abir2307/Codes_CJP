def find_path(matrix):
    m,n=len(matrix),len(matrix[0])
    x,y=m-1,n-matrix[m-1][::-1].index(1)-1
    path=[]
    visited=set()
    while True:
        path.append((x,y))
        visited.add((x, y))
        if(x==0 and y==0):
            break
        elif(x>0 and matrix[x-1][y]==1 and (x-1,y) not in visited ):
            x-=1
        elif(x>m-1 and matrix[x+1][y]==1 and (x+1,y) not in visited ):
            x-=1
        elif(y>0 and matrix[x][y-1]==1 and (x,y-1) not in visited ):
            y-=1
        elif(y<n-1 and matrix[x][y+1]==1 and (x,y+1) not in visited ):
            y+=1
        else:
            break
    return path

def count_path(matrix):
    path=find_path(matrix)
    for i,(x,y) in enumerate(path):
        matrix[x][y]=i+1
    return matrix

def mirror_horizontal(matrix):
    path = find_path(matrix)
    m,n = len(matrix), len(matrix[0])
    
    for x, y in path:
        matrix[x][n - y - 1] = 1
    
    return matrix

def mirror_vertical(matrix):
    m,n=len(matrix), len(matrix[0])
    path=find_path(matrix)
    for x,y in path:
        matrix[m-x-1][y]=1
    return matrix
matrix = [
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 1, 1, 1],
    [1, 0, 0, 0],
    [1, 1, 0, 0]
]
path=find_path(matrix)
for coord in path:
    print (coord)
print("\n")  

matrix=count_path(matrix)
for row in matrix:
    print(row) 
print("\n")  

matrix = [
    [0, 1, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 1, 1]
    ]
matrix = mirror_horizontal(matrix)
for row in matrix:
    print(row)
print("\n") 
matrix = [
    [0, 1, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 1, 1]
    ]
matrix = mirror_vertical(matrix)
for row in matrix:
    print(row)
print("\n") 
