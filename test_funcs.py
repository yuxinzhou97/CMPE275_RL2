import pybind_wrap
import original_funcs
from timeit import default_timer as timer
import cython_funcs as cython_funcs
# import cppimport
# funcs = cppimport.imp("wrap")


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
    # test_add()
    # end = timer()
    # print(end - start)

    # start = timer()
    # test_add_regular()
    # end = timer()
    # print(end - start)

    start = timer()
    test_original_modify()
    end = timer()
    print("python time: " + str(end - start))

    start = timer()
    test_cython_modify()
    end = timer()
    print("Cython time: " + str(end - start))

    start = timer()
    test_pybind_modify()
    end = timer()
    print("pybind11 time: " + str(end - start))









# import pybind_wrap
# import original_funcs
# from timeit import default_timer as timer
# import cython_funcs as cython_funcs
# # import cppimport
# # funcs = cppimport.imp("wrap")

# # totalTimeTaken = 0
# # maxTimeTaken = -float('inf')
# # minTimeTaken = float('inf')

# def test_pybind_modify():
#     for i in range(loop):
#         A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#         B = pybind_wrap.modify(A)
#     print(B)


# def test_cython_modify():
#     for i in range(loop)):
#         A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#         B = cython_funcs.cython_modify(A)
#     print(B)


# def test_original_modify():
    
#     for i in range(loop):
#         A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#         B = original_funcs.original_matrix_modify(A)
#     print(B)

# # def test_original_modify_matrix():


# if __name__ == '__main__':
#     loop = 1000000
#     totalTimeTaken = 0
#     maxTimeTaken = -float('inf')
#     minTimeTaken = float('inf')
#     start = timer()
#     test_original_modify()
#     end = timer()
#     # timeTaken = str(end - start)
#     timeTaken = end - start
#     totalTimeTaken += timeTaken
#     if timeTaken > maxTimeTaken:
# 	    maxTimeTaken = timeTaken
#     if timeTaken < minTimeTaken:
# 	    minTimeTaken = timeTaken
#     print("python time: " + str(end - start))
#     print('python average time: {}'.format(totalTimeTaken/loop))
#     print('python max time: {}'.format(maxTimeTaken))
#     print('python min time: {}'.format(minTimeTaken))

#     maxTimeTaken = -float('inf')
#     minTimeTaken = float('inf')
#     start = timer()
#     test_cython_modify()
#     end = timer()
#     timeTaken = end - start
#     totalTimeTaken += timeTaken
#     if timeTaken > maxTimeTaken:
# 	    maxTimeTaken = timeTaken
#     if timeTaken < minTimeTaken:
# 	    minTimeTaken = timeTaken
#     print("Cython time: " + str(end - start))
#     print('Cython average time: {}'.format(totalTimeTaken/loop))
#     print('Cython max time: {}'.format(maxTimeTaken))
#     print('Cython min time: {}'.format(minTimeTaken))

#     maxTimeTaken = -float('inf')
#     minTimeTaken = float('inf')
#     start = timer()
#     test_pybind_modify()
#     end = timer()
#     timeTaken = end - start
#     totalTimeTaken += timeTaken
#     if timeTaken > maxTimeTaken:
# 	    maxTimeTaken = timeTaken
#     if timeTaken < minTimeTaken:
# 	    minTimeTaken = timeTaken
#     print("pybind11 time: " + str(end - start))
#     print('pybind11 average time: {}'.format(totalTimeTaken/loop))
#     print('pybind11 max time: {}'.format(maxTimeTaken))
#     print('pybind11 min time: {}'.format(minTimeTaken))
    

# #haha
# # def analyze(f, loop=10, library='python'):
# # 	totalTimeTaken = 0
# # 	maxTimeTaken = -float('inf')
# #     minTimeTaken = float('inf')

# #     for _ in loop:
# # 		start = timer()
# # 		f()
# # 		end = timer()
# # 		timeTaken = str(end - start)
# # 		totalTimeTaken += timeTaken
# # 		if timeTaken > maxTimeTaken:
# # 			maxTimeTaken = timeTake
# #         if timeTaken < minTimeTaken:
# # 			minTimeTaken = timeTaken

# #     print('{} average time: {}'.format(library, totalTimeTaken/loop))
# #     print('{} max time: {}'.format(library, maxTimeTaken))
# #     print('{} min time: {}'.format(library, minTimeTaken))

# # if __name__ == '__main__':

# # 	LIBS = ['python', 'cython', 'pybind']		

# #     TEST_SUITE = [
# # 		['Matrix Modify', test_original_modify, test_cython_modify, test_pybind_modify],
# # 		# […],
# # 		# […]
# # 		]

# # 	for test in TEST_SUITE:
# # 		for i in range(len(LIBS)):
# # 			analyze(test[i+1], library=LIBS[i])

# # 		# analyze(test_original_modify, library='python')
# # 		# analyze(test_cython_modify, library='cython')
# # 		# analyze(test_pybind_modify, library='pybind11')
