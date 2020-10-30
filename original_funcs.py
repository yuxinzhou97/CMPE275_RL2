def original_matrix_modify(list):
    i = 0
    while i < len(list):
        value = list[i]
        list[i] = 2 * value
        i += 1
    return list
