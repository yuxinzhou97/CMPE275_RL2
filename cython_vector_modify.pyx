# works with language_level=3,3str
cpdef cython_vector_modify(list):
    cdef int i = 0
    cdef int value = 0
    while i < len(list):
        value = list[i]
        list[i] = 2 * value
        i += 1
    return list