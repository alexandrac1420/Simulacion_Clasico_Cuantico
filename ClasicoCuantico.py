import vec_matrix_complex as lb
import numpy as np
import matplotlib.pyplot as plt

def check_inputs_matrix(matrix):
    n, m = matrix.shape
    for i in range(n):
        colum = matrix[:, i]
        if 1 in colum:
            continue
        else:
            return False
    return True

def check_sum_inputs_matrix(matrix):
    n, m = matrix.shape
    for j in range(m):
        sum_col = sum(matrix[i][j] for i in range(n))
        if sum_col != 1:
            return False
    return True

def check_sum_inputs_matrix_imag(matrix):
    n, m = matrix.shape
    for j in range(m):
        column = matrix[:, j]
        norm_squared = np.sum(np.abs(column) )
        if norm_squared == 1:
            return True
        return False

def simulaCanicas(matrix, inicial_state, clicks):
    if check_inputs_matrix(matrix):
        final_state = inicial_state
        if clicks > 0:
            for i in range (clicks):
                final_state = lb.act_matrix_vec(matrix,final_state)
        return final_state
    else:
        raise ValueError("Error: Cada nodo debe tener minimo una salida")


def generate_inicial_state(matrix):
    num_rows, num_cols = matrix.shape
    vector = [0] * num_rows
    vector[0] = 1
    return vector

def generate_inicial_state_imag(matrix):
    dim = matrix.shape[0]
    vector = np.zeros(dim, dtype=np.complex128)
    vector[0] = 1
    return vector

def simul_multi_slit(matrix, clicks, plot=True):
    inicial_state = generate_inicial_state(matrix)
    if check_sum_inputs_matrix(matrix):
        final_state = inicial_state
        if clicks > 0:
            for i in range (clicks):
                final_state = lb.act_matrix_vec(matrix,final_state)
            if plot:
                plot_and_save_probabilities(final_state,"probabilistico")

            return final_state
        else:
            raise ValueError("Error: Cada salida debe sumar 1")


def simul_multi_slit_imag(matrix, clicks, plot =True):
    inicial_state = generate_inicial_state_imag(matrix)
    if check_sum_inputs_matrix_imag(matrix):
        final_state = inicial_state
        if clicks > 0:
            for i in range (clicks):
                final_state = lb.act_matrix_vec(matrix,final_state)
                if plot:
                    plot_and_save_probabilities(final_state,"cuantico")
            return final_state
        else:
            raise ValueError("Error: Cada salida debe sumar 1")

def plot_and_save_probabilities(vector, filename="probabilities.png"):
    num_states = len(vector)
    indices = np.arange(num_states)
    probabilities = np.abs(vector)

    plt.figure(figsize=(8, 6))
    plt.bar(indices, probabilities, align='center', alpha=0.7)
    plt.xlabel('Estado')
    plt.ylabel('Probabilidad')
    plt.title('Probabilidades del Vector de Estados')
    plt.savefig(filename)
    plt.show()

