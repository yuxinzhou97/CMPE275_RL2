# CMPE275_RL2

# Environment
macOS > 10.7
Clang
Visual Studio
Anaconda3
Python3.8

# Run the code
```
python3.8 -m pip install cython
```

To download this repo with submodule pybind11
```
git clone --recursive https://github.com/yuxinzhou97/CMPE275_RL2
```

Check extern folder to see if pybind11 is already loaded in this repo. If so run

```
python3 cython_setup.py install
python3 cython_setup.py build_ext -inplace
python3 pybind_setup.py install
python3 pybind_setup.py build_ext -i
python3 test_funcs.py
```

If you would like to configure pybind11 by yourself, cd into the directory, then install pybind11 as a submodule

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

