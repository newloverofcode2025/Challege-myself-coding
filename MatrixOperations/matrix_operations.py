def get_matrix(rows, cols, name="Matrix"):
    """
    Prompts the user to input a matrix of given dimensions.
    :param rows: Number of rows
    :param cols: Number of columns
    :param name: Name of the matrix (for display purposes)
    :return: A 2D list representing the matrix
    """
    print(f"Enter the elements of {name} ({rows}x{cols}), row by row:")
    matrix = []
    for i in range(rows):
        while True:
            try:
                row = list(map(float, input(f"Row {i + 1}: ").strip().split()))
                if len(row) != cols:
                    raise ValueError
                matrix.append(row)
                break
            except ValueError:
                print(f"Invalid input. Please enter exactly {cols} numbers.")
    return matrix


def print_matrix(matrix, name="Matrix"):
    """
    Prints a matrix in a readable format.
    :param matrix: The matrix to print
    :param name: Name of the matrix (for display purposes)
    """
    print(f"\n{name}:")
    for row in matrix:
        print(" ".join(f"{elem:8.2f}" for elem in row))


def add_matrices(matrix1, matrix2):
    """
    Adds two matrices element-wise.
    :param matrix1: First matrix
    :param matrix2: Second matrix
    :return: Resultant matrix after addition
    """
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrices must have the same dimensions for addition.")
    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]


def subtract_matrices(matrix1, matrix2):
    """
    Subtracts two matrices element-wise.
    :param matrix1: First matrix
    :param matrix2: Second matrix
    :return: Resultant matrix after subtraction
    """
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrices must have the same dimensions for subtraction.")
    return [[matrix1[i][j] - matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]


def multiply_matrices(matrix1, matrix2):
    """
    Multiplies two matrices.
    :param matrix1: First matrix
    :param matrix2: Second matrix
    :return: Resultant matrix after multiplication
    """
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Number of columns in the first matrix must equal the number of rows in the second matrix.")
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result


def transpose_matrix(matrix):
    """
    Transposes a matrix.
    :param matrix: The matrix to transpose
    :return: Transposed matrix
    """
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


if __name__ == "__main__":
    print("Welcome to the Matrix Operations Tool! 🧮")

    # Get dimensions for the first matrix
    rows1 = int(input("Enter the number of rows for Matrix A: "))
    cols1 = int(input("Enter the number of columns for Matrix A: "))
    matrix_a = get_matrix(rows1, cols1, "Matrix A")

    # Get dimensions for the second matrix
    rows2 = int(input("Enter the number of rows for Matrix B: "))
    cols2 = int(input("Enter the number of columns for Matrix B: "))
    matrix_b = get_matrix(rows2, cols2, "Matrix B")

    # Display the matrices
    print_matrix(matrix_a, "Matrix A")
    print_matrix(matrix_b, "Matrix B")

    # Perform operations
    print("\nSelect an operation:")
    print("1. Add Matrices")
    print("2. Subtract Matrices")
    print("3. Multiply Matrices")
    print("4. Transpose Matrix A")
    print("5. Transpose Matrix B")

    choice = input("Enter your choice (1-5): ").strip()

    try:
        if choice == "1":
            result = add_matrices(matrix_a, matrix_b)
            print_matrix(result, "Resultant Matrix (Addition)")
        elif choice == "2":
            result = subtract_matrices(matrix_a, matrix_b)
            print_matrix(result, "Resultant Matrix (Subtraction)")
        elif choice == "3":
            result = multiply_matrices(matrix_a, matrix_b)
            print_matrix(result, "Resultant Matrix (Multiplication)")
        elif choice == "4":
            result = transpose_matrix(matrix_a)
            print_matrix(result, "Transposed Matrix A")
        elif choice == "5":
            result = transpose_matrix(matrix_b)
            print_matrix(result, "Transposed Matrix B")
        else:
            print("Invalid choice. Please select a valid option.")
    except ValueError as e:
        print(f"Error: {e}")