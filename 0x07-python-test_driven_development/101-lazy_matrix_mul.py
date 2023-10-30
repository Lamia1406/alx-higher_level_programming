#!/usr/bin/python3
"""This module supplies one function, lazy_matrix_mul(m_a, m_b)"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """multiplies 2 matrices"""
    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    if type(m_b) != list:
        raise TypeError("m_b must be a list")
    for element in m_a:
        if type(element) != list:
            raise TypeError("m_a must be a list of lists")
        for item in element:
            if type(item) != int and type(item) != float:
                raise TypeError("m_a should contain only integers or floats")
        if len(element) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")

    for element in m_b:
        if type(element) != list:
            raise TypeError("m_b must be a list of lists")
        for item in element:
            if type(item) != int and type(item) != float:
                raise TypeError("m_b should contain only integers or floats")
        if len(element) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")
    if not m_a:
        raise ValueError("m_a can't be empty")
    if not m_b:
        raise ValueError("m_b can't be empty")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = np.dot(m_a, m_b)
    return result
