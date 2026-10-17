def two_d_list(matrix):
    new_list = []
    
    for row in matrix:
        row_total = sum(row)        
        new_list.append(row_total) 
        
    return new_list

my_2d_list = [[2, 3, 4], [1, 5, 7], [4, 6, 8]]
print(two_d_list(my_2d_list))  
