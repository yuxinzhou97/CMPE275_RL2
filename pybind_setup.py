import os
import sys

from distutils.core import setup, Extension
from distutils import sysconfig

cpp_args = ['-std=c++11', '-stdlib=libc++', '-mmacosx-version-min=10.7']

ext_modules = [
    Extension(
        'pybind_wrap',
        ['pybind_wrap.cpp'],
        include_dirs=['extern/pybind11/include/'],
        language='c++',
        extra_compile_args=cpp_args,
    ),
]

setup(
    ext_modules=ext_modules,
)
