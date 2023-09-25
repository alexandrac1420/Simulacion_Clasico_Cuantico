import numpy as np

def len_vec(v1,v2):
    if len(v1)==len(v2):
        return True
    return False

def sum_vec_complex(vec1,vec2):
    if len_vec(vec1,vec2) == True:
        return np.add(vec1,vec2)
    else:
        raise Exception ("Error: Los vectores no son del mismo tamaño")

def inv_vec_complex(vec1):
    return np.negative(vec1)

def mult_esc_vec(num, vec1):
    return np.multiply(num,vec1)

def len_matrix(matrix1,matrix2):
    if len(matrix1) == len(matrix2):
        for i in range (len(matrix1)):
            if len(matrix1[i])==len(matrix2[i]):
                return True
            return False
    return False

def sum_matrix(matrix1,matrix2):
    if len_matrix(matrix1,matrix2) == True:
        return np.add(matrix1,matrix2)
    else:
        raise Exception("Error: Las matrices no cumplen con las condiciones para su suma")

def inv_matrix(matrix1):
    return np.negative(matrix1)

def mult_esca_matrix(num, matrix1):
    return np.multiply(num,matrix1)

def trans_matrix(matrix1):
    return np.transpose(matrix1)

def conj_matrix(matrix1):
    return np.conjugate(matrix1)

def adj_matrix(matrix1):
    result = np.conjugate(matrix1)
    mat_result = np.transpose(result)
    return mat_result

def act_matrix_vec(matrix1, vec1):
    return np.dot(matrix1,vec1)

def len_col_row(matrix1,matrix2):
    if len(matrix1[0])== len(matrix2):
        return True
    return False

def mult_matrix(matrix1,matrix2):
    if len_col_row(matrix1, matrix2) == True:
        return np.dot(matrix1,matrix2)
    else:
        raise Exception ("Error: El numero de columnas de la matriz 1 no es igual al numero de columnas de la matriz 2")

def prod_int_vec(vec1,vec2):
    return np.vdot(vec1,vec2)

def norm_vec(vec1):
    return np.linalg.norm(vec1)

def dist_vec(vec1,vec2):
    sub = np.subtract(vec1,vec2)
    return norm_vec(sub)

def val_prop_matrix(matrix1):
    return np.linalg.eig(matrix1)

def prod_tens_vec(vec1,vec2):
    return np.outer(vec1,vec2)

def prod_tens_matrix(matrix1, matrix2):
    return np.kron(matrix1, matrix2)

def hermitian_matrix(matrix1):
    if np.array_equal(adj_matrix(matrix1),matrix1):
        return True
    return False

def unit_matrix(matrix1):
    unit = mult_matrix(adj_matrix(matrix1), matrix1)
    if np.allclose(unit, np.eye(matrix1.shape[0], dtype=complex)):
        return True
    return False