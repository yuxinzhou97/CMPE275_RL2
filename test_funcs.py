# # Cython Compilation for Developers¶
# import pyximport
# pyximport.install()

import pybind_wrap
import original_funcs
from timeit import default_timer as timer
import cython_read_write as cython_read_write
import cython_vector_modify as cython_vector_modify


def test_pybind_modify(list, times):
    for i in range(times):
        result = pybind_wrap.modify(list)
    # print(result)


def test_cython_modify(list, times):
    for i in range(times):
        result = cython_vector_modify.cython_vector_modify(list)
    # print(result)


def test_original_modify(list, times):
    for i in range(times):
        result = original_funcs.original_matrix_modify(list)
    # print(result)

def create_list(count):
    list = []
    for i in range(count):
        list.append(i)
    return list

if __name__ == '__main__':
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

    # Test 2: modify vector
    listA = create_list(1000000)
    start = timer()
    test_original_modify(listA, 1)
    end = timer()
    print("python time: " + str(end - start))

    start = timer()
    test_cython_modify(listA, 1)
    end = timer()
    print("Cython time: " + str(end - start))


    start = timer()
    test_pybind_modify(listA, 1)
    end = timer()
    print("pybind11 time: " + str(end - start))
