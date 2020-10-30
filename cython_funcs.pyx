# def say_hello_to(name):
#     return name

def cython_modify(list):
    cdef int i = 0
    cdef int value = 0
    while i < len(list):
        value = list[i]
        list[i] = 2 * value
        i += 1
    return list
