from matrix_element import MatrixElement


def read_sparse_matrix_from_file():
    filename = input("Please enter the file you want to read the sparse matrix from (with the .txt extension): ")

    with open(filename, "r") as f:
        sm = []
        elems = int(f.readline())

        print(f"There are {elems} elements in the sparse matrix text file.")

        for _ in range(elems):
            row = int(f.readline())
            col = int(f.readline())
            val = int(f.readline())

            elem = MatrixElement(row, col, val)
            sm.append(elem)

        print(f"Sparse matrix was read from file '{filename}'.")

        return sm


def write_sparse_matrix_to_file(sm):
    filename = input("Please enter the file you want to write the sparse matrix to (with the .txt extension): ")

    with open(filename, "w") as f:
        f.write(f"{str(len(sm))}\n")

        for elem in sm:
            f.write(f"{elem.row}\n")
            f.write(f"{elem.col}\n")
            f.write(f"{elem.val}\n")

        print(f"Sparse matrix was written to file '{filename}'.\n")


def print_matrix(sm):
    print("Printing matrix elements:")
    for elem in sm:
        print(elem)


def sort_matrix_rows(sm):
    for i in range(1, len(sm)):
        isFound = False

        for j in reversed(range(i, len(sm))):
            # Row check
            if sm[j].row < sm[j - 1].row:
                sm[j].row, sm[j - 1].row = sm[j - 1].row, sm[j].row
                sm[j].col, sm[j - 1].col = sm[j - 1].col, sm[j].col
                sm[j].val, sm[j - 1].val = sm[j - 1].val, sm[j].val

                isFound = True
            elif sm[j].row == sm[j - 1].row:
                # Column check
                if sm[j].col < sm[j - 1].col:
                    sm[j].row, sm[j - 1].row = sm[j - 1].row, sm[j].row
                    sm[j].col, sm[j - 1].col = sm[j - 1].col, sm[j].col
                    sm[j].val, sm[j - 1].val = sm[j - 1].val, sm[j].val

                    isFound = True

        if not isFound:
            break


def sort_matrix_columns(sm):
    for i in range(1, len(sm)):
        isFound = False

        for j in reversed(range(i, len(sm))):
            # Column check
            if sm[j].col < sm[j - 1].col:
                sm[j].row, sm[j - 1].row = sm[j - 1].row, sm[j].row
                sm[j].col, sm[j - 1].col = sm[j - 1].col, sm[j].col
                sm[j].val, sm[j - 1].val = sm[j - 1].val, sm[j].val

                isFound = True
            elif sm[j].col == sm[j - 1].col:
                # Row check
                if sm[j].row < sm[j - 1].row:
                    sm[j].row, sm[j - 1].row = sm[j - 1].row, sm[j].row
                    sm[j].col, sm[j - 1].col = sm[j - 1].col, sm[j].col
                    sm[j].val, sm[j - 1].val = sm[j - 1].val, sm[j].val

                    isFound = True

        if not isFound:
            break


def add_sparse_matrices(sm1, sm2):
    M = 0
    sm = []

    # Inserting first sparse matrix and adding common elements
    for i in range(len(sm1)):
        foundCommon = False

        for j in range(len(sm2)):
            if sm1[i].row == sm2[j].row and sm1[i].col == sm2[j].col:
                newRow = sm1[i].row
                newCol = sm1[i].col
                newVal = sm1[i].val + sm2[j].val

                elem = MatrixElement(newRow, newCol, newVal)
                sm.append(elem)

                M += 1
                foundCommon = True
                break

        if not foundCommon:
            newRow = sm1[i].row
            newCol = sm1[i].col
            newVal = sm1[i].val

            elem = MatrixElement(newRow, newCol, newVal)
            sm.append(elem)

            M += 1

    # Inserting elements from the second sparse matrix
    for i in range(len(sm2)):
        foundCommon = False

        for j in range(len(sm1)):
            if sm2[i].row == sm1[j].row and sm2[i].col == sm1[j].col:
                foundCommon = True
                break

        if not foundCommon:
            newRow = sm2[i].row
            newCol = sm2[i].col
            newVal = sm2[i].val

            elem = MatrixElement(newRow, newCol, newVal)
            sm.append(elem)

            M += 1

    print("The resulting sparse matrix will be printed.")
    print_matrix(sm)

    print("You are about to write the resulting addition sparse matrix to a file.")
    write_sparse_matrix_to_file(sm)


def subtract_sparse_matrices(sm1, sm2):
    M = 0
    sm = []

    # Inserting first sparse matrix and subtracting common elements
    for i in range(len(sm1)):
        foundCommon = False

        for j in range(len(sm2)):
            if sm1[i].row == sm2[j].row and sm1[i].col == sm2[j].col:
                newRow = sm1[i].row
                newCol = sm1[i].col
                newVal = sm1[i].val - sm2[j].val

                elem = MatrixElement(newRow, newCol, newVal)
                sm.append(elem)

                M += 1
                foundCommon = True
                break

        if not foundCommon:
            newRow = sm1[i].row
            newCol = sm1[i].col
            newVal = sm1[i].val

            elem = MatrixElement(newRow, newCol, newVal)
            sm.append(elem)

            M += 1

    # Inserting elements from the second sparse matrix with a minus sign
    for i in range(len(sm2)):
        foundCommon = False

        for j in range(len(sm1)):
            if sm2[i].row == sm1[j].row and sm2[i].col == sm1[j].col:
                foundCommon = True
                break

        if not foundCommon:
            newRow = sm2[i].row
            newCol = sm2[i].col
            newVal = -sm2[i].val

            elem = MatrixElement(newRow, newCol, newVal)
            sm.append(elem)

            M += 1

    print("The resulting sparse matrix will be printed.")
    print_matrix(sm)

    print("You are about to write the resulting addition sparse matrix to a file.")
    write_sparse_matrix_to_file(sm)


def multiply_sparse_matrices(sm1, sm2):
    M = 0
    sm = []

    # Only the common elements will be multiplied and inserted
    # since multiplying by 0 gives 0
    for i in range(len(sm1)):
        for j in range(len(sm2)):
            if sm1[i].row == sm2[j].row and sm1[i].col == sm2[j].col:
                newRow = sm1[i].row
                newCol = sm1[i].col
                newVal = sm1[i].val * sm2[j].val

                elem = MatrixElement(newRow, newCol, newVal)
                sm.append(elem)

                M += 1
                break

    print("The resulting sparse matrix will be printed.")
    print_matrix(sm)

    print("You are about to write the resulting addition sparse matrix to a file.")
    write_sparse_matrix_to_file(sm)
