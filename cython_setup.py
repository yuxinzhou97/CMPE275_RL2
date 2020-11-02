# cython: language_level=3
# from setuptools import setup, dist
# from distutils.extension import Extension
from setuptools import setup, Extension
from Cython.Build import cythonize
# dist.Distribution().fetch_build_eggs(['cython'])

extensions = [Extension('cython_vector_modify', ["cython_vector_modify.pyx"]),
Extension('cython_read_write', ["cython_read_write.pyx"]) ]
# extensions = [Extension('cython_funcs', ["cython_funcs.pyx"])]

setup(
    name='Cython tests',
    ext_modules=cythonize(extensions),
    zip_safe=False,
)
