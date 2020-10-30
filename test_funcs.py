import pybind_wrap
import original_funcs
from timeit import default_timer as timer
# import cppimport
# funcs = cppimport.imp("wrap")


def test_modify_matrix():
    for i in range(1000000):
        A = [1, 2, 3, 4, 5, 6, 7]
        B = pybind_wrap.modify(A)
    print(B)


def test_original_modify():
    for i in range(1000000):
        A = [1, 2, 3, 4, 5, 6, 7]
        B = original_funcs.original_matrix_modify(A)
    print(B)


if __name__ == '__main__':
    # start = timer()
    # test_add()
    # end = timer()
    # print(end - start)

    # start = timer()
    # test_add_regular()
    # end = timer()
    # print(end - start)

    start = timer()
    test_modify_matrix()
    end = timer()
    print("pybind11 time: " + str(end - start))
    start = timer()
    test_original_modify()
    end = timer()
    print("python time: " + str(end - start))
