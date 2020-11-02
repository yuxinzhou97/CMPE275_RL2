# works with language_level=3,3str
#include <stdio.h>
#include <stdlib.h>

cpdef test_cython_read_and_write(input_path, output_path):
    with open(input_path, 'r') as reader:
        lines = reader.readlines()
    with open(output_path, 'w') as writer:
        for line in lines:
            writer.write(line)

# https://cython.readthedocs.io/en/latest/src/tutorial/strings.html
