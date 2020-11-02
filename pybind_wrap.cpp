#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "pybind_read_write.cpp"
#include "pybind_vector_modify.cpp"
#include "pybind_iteration.cpp"

namespace py = pybind11;


PYBIND11_MODULE(pybind_wrap, m)
{
    m.doc() = "pybind11 example plugin"; // optional
    m.def("modify", &modify, "Multiply all entries of a list by 2.0");
    m.def("pybind_read_write", &pybind_read_write, "read and write text file");
    m.def("power_by_iteration", &power_by_iteration, "calculate power(a, b)");
}