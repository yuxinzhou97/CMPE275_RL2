# works with language_level=3,3str
def test_cython_read_and_write(input_path, output_path):
    with open(input_path, 'r') as reader:
        lines = reader.readlines()
    with open(output_path, 'w') as writer:
        for line in lines:
            writer.write(line)
