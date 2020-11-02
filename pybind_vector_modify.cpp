#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <vector>
using namespace std;
namespace py = pybind11;
vector<int> modify(vector<int> &input)
{
    vector<int> result(input.size());
    for (unsigned long i = 0; i < input.size(); i++)
    {
        result[i] = 2 * input[i];
    }
    return result;
}