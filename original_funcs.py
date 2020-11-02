def original_matrix_modify(list):
    i = 0
    while i < len(list):
        value = list[i]
        list[i] = 2 * value
        i += 1
    return list

def test_python_read_and_write(input_path, output_path):
    with open(input_path, 'r') as reader:
        lines = reader.readlines()
    with open(output_path, 'w') as writer:
        for line in lines:
            writer.write(line)

# calculate a^b iteratively, assume never out of range
# time is O(N)
def power_by_iteration(a, b):
    result = 1
    for i in range(b):
        result = result * a
    return result
