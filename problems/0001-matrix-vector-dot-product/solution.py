def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
    # Return a list where each element is the dot product of a row of 'a' with 'b'.
    # If the number of columns in 'a' does not match the length of 'b', return -1.
    dot_product = []

    if len(a[0]) != len(b):
        return -1

    for vec in a:
        temp_dot_product = 0
        for i, j in zip(vec, b):
            temp_dot_product += i * j
        dot_product.append(temp_dot_product)

    return dot_product