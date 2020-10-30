#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <vector>
using namespace std;

vector<int> modify(vector<int> &input)
{
    vector<int> result(input.size());
    for (unsigned long i = 0; i < input.size(); i++)
    {
        result[i] = 2 * input[i];
    }
    return result;
}

namespace py = pybind11;

PYBIND11_MODULE(pybind_wrap, m)
{
    m.doc() = "pybind11 example plugin"; // optional
    m.def("modify", &modify, "Multiply all entries of a list by 2.0");
}