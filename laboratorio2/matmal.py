
import random
import numpy as np
def random_matrix(m, n):
    out = []
    for row in range(m):
        out.append([random.random() for _ in range(n)])
    return out


def matmul(A, B):
    """Multiply matrix A by matrix B."""
    
    # Convierte las matrices de entrada en matrices NumPy
    A_np = np.array(A)
    B_np = np.array(B)

    # Verifica la compatibilidad de las matrices para la multiplicación
    if A_np.shape[1] != B_np.shape[0]:
        raise Exception("Can't multiply matrices. Incompatible sizes")

    # Realiza la multiplicación de matrices utilizando NumPy
    result_np = np.dot(A_np, B_np)

    # Convierte el resultado a una lista de listas antes de devolverlo
    result = result_np.tolist()

    return result


a= random_matrix(3, 4)
b= random_matrix(4, 5)






print(matmul(a, b))

