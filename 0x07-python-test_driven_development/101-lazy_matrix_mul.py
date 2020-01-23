#!/usr/bin/python3
import numpy as np
def lazy_matrix_mul(m_a, m_b):
    for i in [m_a, m_b]:
        if type(i) is not list:
            if i == m_a:
                raise TypeError("m_a must be a list")
            else:
                raise TypeError("m_b must be a list")
    for item in [m_a, m_b]:
        for i in item:
            if type(i) is not list:
                if item == m_a:
                    raise TypeError("m_a must be a list of lists")
                else:
                    raise TypeError("m_b must be a list of lists")
    for i in [m_a, m_b]:
        if i == [] or i == [[]]:
            if i == m_a:
                raise ValueError("m_a can't be empty")
            else:
                raise ValueError("m_b can't be empty")
    for item in [m_a, m_b]:
        for i in item:
            for j in i:
                if type(j) not in [float, int]:
                    if item == m_a:
                        raise TypeError("m_a should contain \
only integers or floats")
                    else:
                        raise TypeError("m_b should contain \
only integers or floats")

    for i in range(len(m_a)):
        if len(m_a[i]) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")

    for i in range(len(m_b)):
        if len(m_b[i]) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    A = np.array(m_a)
    B = np.array(m_b)
    return A.dot(B)
