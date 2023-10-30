#!/usr/bin/python3
"""This module supplies one function, lazy_matrix_mul(m_a, m_b)"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """multiplies 2 matrices"""
    result = np.matmul(m_a, m_b)
    return result
