def rotate(x1, y1, x2, y2, matrix):
    first = matrix[x1][y1]
    min_value = first

    for k in range(x1, x2):
        matrix[k][y1] = matrix[k + 1][y1]
        min_value = min(min_value, matrix[k + 1][y1])

    for k in range(y1, y2):
        matrix[x2][k] = matrix[x2][k + 1]
        min_value = min(min_value, matrix[x2][k + 1])

    for k in range(x2, x1, -1):
        matrix[k][y2] = matrix[x1][k - 1]
        min_value = min(min_value, matrix[x1][k - 1])

    matrix[x1][y1 + 1] = first
    return min_value


def solution(rows, columns, queries):
    matrix = [[(i) * columns + (j + 1) for j in range(columns)] for i in range(rows)]
    result = []
    for x1, y1, x2, y2 in queries:
        result.append(rotate(x1 - 1, y1 - 1, x2 - 1, y2 - 1, matrix))

    return result
