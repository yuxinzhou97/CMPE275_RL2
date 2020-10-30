# from setuptools import setup, dist
# from distutils.extension import Extension
# import cython later
from setuptools import setup, Extension
from Cython.Build import cythonize
# dist.Distribution().fetch_build_eggs(['cython'])

extensions = [Extension('cython_funcs', ["cython_funcs.pyx"])]

setup(
    name='Cython test',
    ext_modules=cythonize(extensions),
    zip_safe=False,
)
