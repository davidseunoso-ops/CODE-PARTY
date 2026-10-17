def corresponding_index_list(matrix):
    new_list = [0] * len(matrix[0])
  
    for index in range(len(matrix[0])):
        column_total = 0

        for row in matrix:
            new_list[index] += row[index]

    return new_list

result = [[2, 3, 4], [1, 5, 7], [4, 6, 8]]
print(corresponding_index_list(result))

