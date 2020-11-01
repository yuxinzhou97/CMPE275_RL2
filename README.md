# CMPE275_RL2

```
python3.8 -m pip install cython
```

pybind11 is already loaded in this repo, run

```
python3 cython_setup.py install
python3 cython_setup.py build_ext -inplace
python3 pybind_setup.py build_ext -i
python3 test_funcs.py
```

if you want to configure the pybind11 by yourself, cd into the directory, then install pybind11 as a submodule

```
git submodule add ../../pybind/pybind11 extern/pybind11 -b stable
git submodule update --init
```

```
cd /extern/pybind11
mkdir build
cd build
cmake ..
make check -j 4
```

test1 cython: cython_read_write.pyx     
test1 python: original_funcs.py  
test1 pybind: pybind_read_write.cpp -> pybind.wrap.cpp   

