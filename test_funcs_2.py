import pybind_wrap
import original_funcs
from timeit import default_timer as timer
import cython_funcs as cython_funcs

def test_pybind_arithmetic():
    # A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # B = pybind_wrap.modify(A)
    # cython_funcs.cython_simple_add(100, 1000)
    pass


def test_cython_arithmetic():
    # A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # B = cython_funcs.cython_modify(A)
    # cython_funcs.cython_simple_add(100, 1000)
    pass


def test_original_arithmetic():
    original_funcs.original_simple_add(100, 1000)
    original_funcs.original_simple_mul(100, 1000)

def test_pybind_modify():
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    B = pybind_wrap.modify(A)


def test_cython_modify():
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    B = cython_funcs.cython_modify(A)


def test_original_modify():
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    B = original_funcs.original_matrix_modify(A)


def analyze(f, loop=10, library='python'):
    totalTimeTaken = 0
    maxTimeTaken = -float('inf')
    minTimeTaken = float('inf')

    for _ in range(loop):
        start = timer()
        f()
        end = timer()
        timeTaken = end - start
        totalTimeTaken += timeTaken
        if timeTaken > maxTimeTaken:
            maxTimeTaken = timeTaken
        if timeTaken < minTimeTaken:
            minTimeTaken = timeTaken
    print('Number of loops: {}'.format(loop))
    print('{} total time: {}'.format(library, totalTimeTaken))
    print('{} average time: {}'.format(library, totalTimeTaken/loop))
    print('{} max time: {}'.format(library, maxTimeTaken))
    print('{} min time: {}'.format(library, minTimeTaken))
    print()

if __name__ == '__main__':

    LIBS = ['python', 'cython', 'pybind']		

    TEST_SUITE = [
        {
            'name': 'Simple Arithmetic',
            'functions': [test_original_arithmetic, test_cython_modify, test_pybind_modify],
            'loops': 1000000
        },
        {
            'name': 'List Modify',
            'functions': [test_original_modify, test_cython_modify, test_pybind_modify],
            'loops': 1000000
        }
        # […],
        # […]
    ]

    for test in TEST_SUITE:
        for i in range(len(LIBS)):
            lib = LIBS[i]
            print('Running {} for {}'.format(test['name'], lib))
            analyze(test['functions'][i], loop=test['loops'], library=lib)

    # analyze(test_original_modify, library='python')
    # analyze(test_cython_modify, library='cython')
    # analyze(test_pybind_modify, library='pybind11')
