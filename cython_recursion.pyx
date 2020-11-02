# works with language_level=3,3str

# calculate a^n recursively
# a > 0, b is integer, assume never out of range
# time is O(N)
def power_by_recursion(a, n):
    return c_power_recursion(a, n)


cdef double c_power_recursion(double a, int n):
    if n == 0:
        return 1
    elif (n == 1):
        return a
    cdef double half = power_by_recursion(a, n/2)
    if (n % 2 == 1):
        return half * half * a
    else:
        return half * half
        
