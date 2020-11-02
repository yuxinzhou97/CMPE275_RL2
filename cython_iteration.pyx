# works with language_level=3,3str

# calculate a^n iteratively
# a > 0, b is integer, assume never out of range
# time is O(N)
def power_by_iteration(a, b):
    return c_power_iteration(a, b)


cdef double c_power_iteration(double a, int n):
    cdef double result = 1.0
    for i in range(n):
        result = result * a
    return result

