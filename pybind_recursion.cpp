#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
using namespace pybind11::literals;

using namespace std;
namespace py = pybind11;
// calculate a^b recursively
// a > 0, b is integer, assume never out of range
// time is O(N)
double power_by_recursion(double a, int n)
{
    if (n == 0) {
        return 1;
    } else if (n == 1) {
        return a;
    }
    
    double half = power_by_recursion(a, n/2);
    if (n % 2 == 1) {
        return half * half * a;
    }  else {
        return half * half;
    }
}