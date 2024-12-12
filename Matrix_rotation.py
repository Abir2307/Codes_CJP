'''
Given a matrix of size N*N, you are provided with several queries and rules for rotating a sub-matrix. The task is to follow the specified rules and print the resulting matrix as a string.

Each query defines a sub-matrix and is represented in the format "row col size", where:

row - The starting row of the sub-matrix

col - The starting column of the sub-matrix.

size - The dimension of the sub-matrix.

For example, if the size is 3, the sub-matrix starts at (row, col) and spans a 3x3 area. You need to apply the below rules to form rotated version of this sub matrix and replace it in the original matrix.

Rules for rotation are given below.

The layer count starts from 1. For each sub-matrix, select the elements layer by layer starting from the topmost layer on the outside of the matrix. If the layer number K is odd, rotate the elements in that layer counterclockwise by K positions. Additionally, replace each letter with the one that comes immediately before it in the alphabet (e.g., 'C' becomes 'B', 'A' becomes 'Z').
If the layer number K is even, rotate the elements in that layer clockwise by K positions. Additionally, replace each letter with the one that comes immediately after it in the alphabet (e.g., 'C' becomes 'D', 'Z' becomes 'A').
If only one letter remains in the centre of the sub-matrix, it is not considered a layer. Leave it unchanged.
For example, consider the below matrix of size 4*4 and the query 0 0 4 which means you need to select the sub matrix starting at (0, 0) and spanning 4 rows, 4 columns from that point which means the entire given matrix.

com.tcs.cv.automata.ei.middleware.DocxToHtmlConverter@7e97551f:image1.png

Now the first layer is highlighted below with blue color.

com.tcs.cv.automata.ei.middleware.DocxToHtmlConverter@7e97551f:image2.png

Since the layer is odd so we rotate in anti-clock wise direction along with replacing each letter with the previous letter, matrix will become like below

com.tcs.cv.automata.ei.middleware.DocxToHtmlConverter@7e97551f:image3.png

The second layer is highlighted below with blue colour.

com.tcs.cv.automata.ei.middleware.DocxToHtmlConverter@7e97551f:image4.png


Since it's an even numbered layer, we rotate it 2 steps clockwise, while also replacing each letter with the next alphabet letter will become like below.

com.tcs.cv.automata.ei.middleware.DocxToHtmlConverter@7e97551f:image5.png

So, the final rotated matrix is

com.tcs.cv.automata.ei.middleware.DocxToHtmlConverter@7e97551f:image6.png

which when joined together from row 1 to row N, becomes

A B C G Z L K K D H G O H L M N

Given the matrix, queries, apply the above rotation rules and print the resulting string.

Constraints
1 <= N <= 50

1 <= Q <= 50

2 <= Size of each sub matrix <= 50

The matrix will only consist of upper-case alphabets.

Input
First line consists of an integer N denoting the size of the matrix.

Second line consists of an integer K denoting the number of queries.

Next K lines will be having 3 space separated integers denoting the row, col size of ith query.

Output
Rotate the matrix according to the above rules and print the resulting string.

Time Limit (secs)
1

Examples
Example 1

Input

5

A B C D E

F G H I J

K L M N O

P Q R S T

U V W X Y

2

1 1 4

3 0 2

Output

ABCDEFGHINKFTSSJOONXOTUVW

Explanation

After extracting the layers and implementing the rotation rules on them and placing them back in the original matrix in each query, it will give the below matrix

A B C D E

F G H I N

K F T S S

J O O N X

O T U V W

On joining all the rows, we will get the string - ABCDEFGHINKFTSSJOONXOTUVW

Example 2

Input

6

Q F H Y X C

A S D F G H

V G T H I J

M H Y J U K

V A I S H N

A V I H E Y

3

0 0 5

4 3 2

0 2 3

Output

EGVEGCPIWTSHZZGSDJUKIGGKLUZQDNAVIGGY

Explanation

After extracting the layers and implementing the rotation rules on them and placing them back in the original matrix in each query, it will give the below matrix

E G V E G C

P I W T S H

Z Z G S D J

U K I G G K

L U Z Q D N

A V I G G Y

On joining the above matrix, we get - EGVEGCPIWTSHZZGSDJUKIGGKLUZQDNAVIGGY'''
n = int(input())
matrix = [list(input().split()) for _ in range(n)]
q = int(input())
queries = [tuple(map(int, input().split())) for _ in range(q)]

def rotate_layer(layer, k, direction):
    n = len(layer)
    k %= n
    if direction == "counterclockwise":
        rotated = layer[k:] + layer[:k]
    else:
        rotated = layer[-k:] + layer[:-k]
    return rotated
  
def transform_letter(letter, is_even):
    if is_even:
        return chr(((ord(letter) - ord('A') + 1) % 26) + ord('A'))
    else:
        return chr(((ord(letter) - ord('A') - 1) % 26) + ord('A'))
      
def process_layer(matrix, top, left, size, layer_num):
    layer = []
    bottom, right = top + size - 1, left + size - 1

    for i in range(left, right + 1):
        layer.append(matrix[top][i])
    for i in range(top + 1, bottom):
        layer.append(matrix[i][right])
    for i in range(right, left - 1, -1):
        layer.append(matrix[bottom][i])
    for i in range(bottom - 1, top, -1):
        layer.append(matrix[i][left])

    direction = "counterclockwise" if layer_num % 2 != 0 else "clockwise"
    rotated_layer = rotate_layer(layer, layer_num, direction)
    transformed_layer = [transform_letter(char, layer_num % 2 == 0) for char in rotated_layer]

    idx = 0
    for i in range(left, right + 1):
        matrix[top][i] = transformed_layer[idx]
        idx += 1
    for i in range(top + 1, bottom):
        matrix[i][right] = transformed_layer[idx]
        idx += 1
    for i in range(right, left - 1, -1):
        matrix[bottom][i] = transformed_layer[idx]
        idx += 1
    for i in range(bottom - 1, top, -1):
        matrix[i][left] = transformed_layer[idx]
        idx += 1

def rotate_submatrix(matrix, row, col, size):
    num_layers = size // 2
    for layer_num in range(1, num_layers + 1):
        process_layer(matrix, row + layer_num - 1, col + layer_num - 1, size - 2 * (layer_num - 1), layer_num)

def process_queries(matrix, queries):
    for query in queries:
        row, col, size = query
        rotate_submatrix(matrix, row, col, size)

def matrix_to_string(matrix):
    return ''.join(''.join(row) for row in matrix)

process_queries(matrix, queries)
print(matrix_to_string(matrix))