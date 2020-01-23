#!/usr/bin/python3
import numpy as np
def lazy_matrix_mul(m_a, m_b):
    if m_a is not list:
        raise TypeError("m_a must be a list")
    if m_b is not list:
        raise TypeError("m_a must be a list")

    A = np.array(m_a)
    B = np.array(m_b)
    return A.dot(B)
