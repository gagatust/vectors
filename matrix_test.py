from matrix import *


def test_mul_matrix_scale():
    a = [[1, 2], [3, 4]]
    num = 2
    ans = [[2, 4], [6, 8]]
    assert ans == mul_matrix_scale(a, num)


def test_add_matrix():
    a = [[1, 2], [3, 4]]
    b = [[3, 4], [-1, 3]]
    ans = [[4, 6], [2, 7]]
    assert ans == add_matrix(a, b)


def test_sub_matrix():
    a = [[6, 7], [-4, 3]]
    b = [[1, 3], [2, -5]]
    ans = [[5, 4], [-6, 8]]
    assert ans == sub_matrix(a, b)


def test_mul_matrix():
    a = [[1, 2], [3, 4]]
    b = [[5, 6], [7, 8]]
    ans = [[19, 22], [43, 50]]
    assert ans == mul_matrix(a, b)


def test_trans_matrix():
    a = [[2, 3, 5], [5, 7, 6]]
    ans = [[2, 5], [3, 7], [5, 6]]
    assert ans == trans_matrix(a)


def test_get_row():
    a = [[1, 2], [3, 4], [5, 6]]
    index = 1
    ans = [3, 4]
    assert ans == get_row(a, index)


def test_get_col():
    a = [[1, 2], [3, 4], [5, 6]]
    index = 0
    ans = [1, 3, 5]
    assert ans == get_col(a, index)


def test_change_row():
    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    start_index = 0
    new_index = 1
    ans = [[4, 5, 6], [1, 2, 3], [7, 8, 9]]
    assert ans == change_row(a, start_index, new_index)


def test_mul_matrix_row_scale():
    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    num = 2
    index = 2
    ans = [[1, 2, 3], [4, 5, 6], [14, 16, 18]]
    assert ans == mul_matrix_row_scale(a, num, index)