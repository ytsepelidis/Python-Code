from sparse_matrix_operations import *


def main():
    print("This is a program for computing operations between sparse matrices")
    print("with the I/O of said matrices occurring with files given by the user.")

    isSorted = False
    isRowSorted = False

    # Reading sparse matrix
    sm1 = read_sparse_matrix_from_file()
    print_matrix(sm1)

    # Choice menu loop
    while True:
        print("~~~~ MENU ~~~~")
        print("1) Sort sparse matrix by rows and columns")
        print("2) Sort sparse matrix by columns and rows")
        print("3) Add two sparse matrices")
        print("4) Subtract two sparse matrices")
        print("5) Multiply two sparse matrices")
        print("0) Exit")

        # Checking user input
        while True:
            choice = input("Enter your choice [0 - 5]: ")

            if choice.isnumeric():
                choice = int(choice)
                break
            else:
                print("Invalid input. You entered text.")

        match choice:
            case 1:
                sort_matrix_rows(sm1)
                print("Sorted sparse matrix by rows and columns.")
                print_matrix(sm1)

                isSorted = True
                isRowSorted = True
            case 2:
                sort_matrix_columns(sm1)
                print("Sorted sparse matrix by columns and rows.")
                print_matrix(sm1)

                isSorted = True
                isRowSorted = False
            case 3:
                # Checking whether sparse matrix is sorted
                if not isSorted:
                    print("The sparse matrix read from file has not been sorted.")
                    print("To execute the operation the matrix has to be sorted.")
                    print()
                    continue

                print("You have to provide the filename for another sparse matrix for the operation to occur.")
                sm2 = read_sparse_matrix_from_file()

                # Sorting second sparse matrix in the same manner
                if isRowSorted:
                    print("Sorted the second sparse matrix by rows.")
                    sort_matrix_rows(sm2)
                else:
                    print("Sorted the second sparse matrix by columns.")
                    sort_matrix_columns(sm2)

                print("The sorted second sparse matrix will be printed.")
                print_matrix(sm2)

                # Adding the sparse matrices
                add_sparse_matrices(sm1, sm2)
            case 4:
                # Checking whether sparse matrix is sorted
                if not isSorted:
                    print("The sparse matrix read from file has not been sorted.")
                    print("To execute the operation the matrix has to be sorted.")
                    print()
                    continue

                print("You have to provide the filename for another sparse matrix for the operation to occur.")
                sm2 = read_sparse_matrix_from_file()

                # Sorting second sparse matrix in the same manner
                if isRowSorted:
                    print("Sorted the second sparse matrix by rows.")
                    sort_matrix_rows(sm2)
                else:
                    print("Sorted the second sparse matrix by columns.")
                    sort_matrix_columns(sm2)

                print("The sorted second sparse matrix will be printed.")
                print_matrix(sm2)

                # Subtracting the sparse matrices
                subtract_sparse_matrices(sm1, sm2)
            case 5:
                # Checking whether sparse matrix is sorted
                if not isSorted:
                    print("The sparse matrix read from file has not been sorted.")
                    print("To execute the operation the matrix has to be sorted.")
                    print()
                    continue

                print("You have to provide the filename for another sparse matrix for the operation to occur.")
                sm2 = read_sparse_matrix_from_file()

                # Sorting second sparse matrix in the same manner
                if isRowSorted:
                    print("Sorted the second sparse matrix by rows.")
                    sort_matrix_rows(sm2)
                else:
                    print("Sorted the second sparse matrix by columns.")
                    sort_matrix_columns(sm2)

                print("The sorted second sparse matrix will be printed.")
                print_matrix(sm2)

                # Multiplying the sparse matrices
                multiply_sparse_matrices(sm1, sm2)
            case 0:
                print("You want to exit the program. Exiting program . . .")
                break
            case _:
                print("Number you entered is not a valid choice. [0 - 5]")

        print()


main()
