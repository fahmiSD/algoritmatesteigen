def diagonal_difference(matrix):
    n = len(matrix)
    sum_primary = sum(matrix[i][i] for i in range(n)) 
    sum_secondary = sum(matrix[i][n - 1 - i] for i in range(n)) 
    difference = sum_primary - sum_secondary
    return sum_primary, sum_secondary, difference

matrix = [[1, 2, 0], [4, 5, 6], [7, 8, 9]]
sum_primary, sum_secondary, result = diagonal_difference(matrix)
print(f"Maka hasilnya adalah: {sum_primary} - {sum_secondary} = {result}")
