# Cython Compilation for Developers¶
import pyximport
pyximport.install()

import pybind_wrap
import original_funcs
from timeit import default_timer as timer
import cython_funcs as cython_funcs
import cython_read_write as cython_read_write
# import cppimport
# funcs = cppimport.imp("wrap")
# https: // norvig.com/ngrams/



def test_pybind_modify():
    for i in range(1000000):
        A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        B = pybind_wrap.modify(A)
    print(B)


def test_cython_modify():
    for i in range(1000000):
        A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        B = cython_funcs.cython_modify(A)
    print(B)


def test_original_modify():
    for i in range(1000000):
        A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        B = original_funcs.original_matrix_modify(A)
    print(B)


if __name__ == '__main__':

    # start = timer()
    # test_original_modify()
    # end = timer()
    # print("python time: " + str(end - start))

    # start = timer()
    # test_cython_modify()
    # end = timer()
    # print("Cython time: " + str(end - start))


    start = timer()
    test_pybind_modify()
    end = timer()
    print("pybind11 time: " + str(end - start))


    # Test 1: read and write test
    start = timer()
    input_path = 'sherlock_holmes.txt'
    output_path = 'sherlock_holmes_output_python.txt'
    original_funcs.test_python_read_and_write(input_path, output_path)
    end = timer()
    print("python read write text time: " + str(end - start))

    start = timer()
    input_path = 'sherlock_holmes.txt'
    output_path = 'sherlock_holmes_output_cython.txt'
    cython_read_write.test_cython_read_and_write(input_path, output_path)
    end = timer()
    print("Cython read and write time: " + str(end - start))

    start = timer()
    input_path = 'sherlock_holmes.txt'
    output_path = 'sherlock_holmes_output_pybind.txt'
    pybind_wrap.pybind_read_write(input_path, output_path)
    end = timer()
    print("Pybind read and write time: " + str(end - start))
