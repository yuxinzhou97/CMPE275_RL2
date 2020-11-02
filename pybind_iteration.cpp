#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
using namespace pybind11::literals;

using namespace std;
namespace py = pybind11;
// calculate a^b iteratively
// a > 0, b is integer, assume never out of range
// time is O(N)
double power_by_iteration(double a, int n)
{
    double result = 1.0;
    for (int i = 0; i < n; i++) {
        result = result * a;
    }  
    return result;
}