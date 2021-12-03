file = open("input.txt", "r")
lines = file.read().splitlines()

def transpose(matrix):
    result = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    
    return(result)

def calculate_paramaters(matrix, parameter):
    result_matrix = []

    for item in matrix:
        count_0 = 0
        count_1 = 0
        
        for digit in item:
            if digit == '0':
                count_0 += 1
            else:
                count_1 += 1 

        if parameter == "gamma":
            if count_0 > count_1:
                result_matrix.append("0")
            else:
                result_matrix.append("1")
        elif parameter == "epsilon":
            if count_0 > count_1:
                result_matrix.append("1")
            else:
                result_matrix.append("0")
    
    result = int(''.join([str(item) for item in result_matrix]), 2)

    return(result)

matrix = transpose(lines)

print(calculate_paramaters(matrix, "gamma") * calculate_paramaters(matrix, "epsilon"))









