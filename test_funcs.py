import statistics as stat
import sys
import pybind_wrap
import original_funcs
from timeit import default_timer as timer
import cython_read_write as cython_read_write
import cython_vector_modify as cython_vector_modify
import cython_iteration as cython_iteration
import cython_recursion as cython_recursion
sys.setrecursionlimit(1500)


def create_list(count):
    list = []
    for i in range(count):
        list.append(i)
    return list

def read_write_test(read_write_func, input_path, output_path, times, repetition):
    # data in ms
    data = []
    # print("result for running test with "+ str(repetition) + " repetition and collect date "+ str(times) + " times:")
    for i in range(times):
        start = timer()
        for j in range(repetition): 
            read_write_func(input_path, output_path)
        end = timer()
        data.append((end - start) * 1000)
    avg = data_processing(data)
    return avg

def modify_list_test(modify_list_func, list, times, repetition):
    # data in ms
    data = []
    # print("result for running test with "+ str(repetition) + " repetition and collect date "+ str(times) + " times:")
    for i in range(times):
        start = timer()
        for j in range(repetition): 
            newlist = modify_list_func(list)
        end = timer()
        data.append((end - start) * 1000)
    avg = data_processing(data)
    return avg

def iteration_test(iteration_func, a, b, times, repetition):
    # data in ms
    data = []
    # print("result for running test with "+ str(repetition) + " repetition and collect date "+ str(times) + " times:")
    for i in range(times):
        start = timer()
        for j in range(repetition): 
            power_result = iteration_func(a, b)
        end = timer()
        data.append((end - start) * 1000)
    avg = data_processing(data)
    return avg

def recursion_test(recursion_func, a, b, times, repetition):
    # data in ms
    data = []
    # print("result for running test with "+ str(repetition) + " repetition and collect date "+ str(times) + " times:")
    for i in range(times):
        start = timer()
        for j in range(repetition): 
            power_result = recursion_func(a, b)
        end = timer()
        data.append((end - start) * 1000)
    avg = data_processing(data)
    return avg
        
def data_processing(data):
    avg = stat.mean(data)
    std = stat.stdev(data)
    lower_bound = avg - 2*std
    upper_bound = avg + 2*std
    min_val = min(data)   
    max_val = max(data)
    cleaned_data = []
    for num in data:
        if num >= lower_bound and num <= upper_bound:
            cleaned_data.append(num)
    # print("average in ms: " + str(avg))
    # print("standard deviation in ms: " + str(std))
    # print("+/- 2 standard deviation range in ms: [" + str(lower_bound) + ", " + str(upper_bound) +"]")
    # print("min in ms: " + str(min_val))
    # print("max in ms: " + str(max_val))
    # print("data:")
    # print(data)
    # print(cleaned_data)
    return stat.mean(cleaned_data)


if __name__ == '__main__':
    # Test 1: read and write test
    times = 10
    repetition = 1
    print("Test 1: read and write test ")
    print("------------------------------")
    # python test 1
    input_path = 'sherlock_holmes.txt'
    output_path = 'sherlock_holmes_output_python.txt'
    result = read_write_test(original_funcs.test_python_read_and_write, input_path, output_path, times, repetition)
    print("python time: "+ str(result) + " ms")
    # cython test 1
    input_path = 'sherlock_holmes.txt'
    output_path = 'sherlock_holmes_output_cython.txt'
    result = read_write_test(cython_read_write.test_cython_read_and_write, input_path, output_path, times, repetition)
    print("cython time: "+ str(result) + " ms")
    # pybind11 test 1
    input_path = 'sherlock_holmes.txt'
    output_path = 'sherlock_holmes_output_pybind.txt'
    result = read_write_test(pybind_wrap.pybind_read_write, input_path, output_path, times, repetition)
    print("pybind time: "+ str(result) + " ms")
    print()

    # Test 2: modify list 
    times = 10
    repetition = 1
    listA = create_list(1000)
    print("Test 2: modify list ")
    print("------------------------------")
    # python test 2
    result =  modify_list_test(original_funcs.original_matrix_modify, listA, times, repetition)
    print("python time: " + str(result) + " ms")
    # cython test 2
    result =  modify_list_test(cython_vector_modify.cython_vector_modify, listA, times, repetition)
    print("Cython time: " + str(result) + " ms")
    # pybind11 test 2
    result =  modify_list_test(pybind_wrap.modify, listA, times, repetition)
    print("pybind11 time: " + str(result) + " ms")
    print()

    # Test 3: iteration test, calculate power(a, b) by iteration
    # a > 0, b is integer, assume never out of range
    a = 0.99
    b = 1500
    times = 10
    repetition = 1
    print("Test 3: iteration test, calculate power(a, b) by iteration")
    print("------------------------------")
    # python test 3
    result = iteration_test(original_funcs.power_by_iteration, a, b, times, repetition)
    print("python time: " + str(result) + " ms")
    # cython test 3
    result = iteration_test(cython_iteration.power_by_iteration, a, b, times, repetition)
    print("cython time: " + str(result) + " ms")
    # pybind test 3
    result = iteration_test(pybind_wrap.power_by_iteration, a, b, times, repetition)
    print("pybind11 time: " + str(result) + " ms")
    print()

    # Test 4: recursion test, calculate power(a, b) by recursion
    # a > 0, b is integer, assume never out of range
    a = 0.99
    b = 1500
    times = 10
    repetition = 1
    print("Test 4: recursion test, calculate power(a, b) by iteration")
    print("------------------------------")
    # python test 4
    result = recursion_test(original_funcs.power_by_recursion, a, b, times, repetition)
    print("python time: " + str(result) + " ms")
    # cython test 4
    result = recursion_test(cython_recursion.power_by_recursion, a, b, times, repetition)
    print("cython time: " + str(result) + " ms")
    # pybind test 4
    result = recursion_test(pybind_wrap.power_by_recursion, a, b, times, repetition)
    print("cython time: " + str(result) + " ms")

