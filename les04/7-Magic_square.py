# DISCLAIMER: (most of) this code was made past midnight, while I was half-asleep. In other words: it sucks.

# This is a terrible function. It's ugly, has unnecessary variables, etc.
def check_numbers_old(matrix):
    found_numbers = set()
    is_magic_square = True
    for sublist in matrix:
        for num in sublist:
            if num in found_numbers or num not in range(1, 17):
                is_magic_square = False
                break
            else:
                found_numbers.add(num)
        if not is_magic_square:
            break
    return is_magic_square


# Using this absolute GENIUS way to figure out if all numbers are in a list
# https://stackoverflow.com/questions/3899782/how-to-check-whether-elements-appears-in-the-list-only-once-in-python
def check_numbers(matrix):
    # In order to make this work, we need one list of all the elements inside the matrix
    list_of_matrix = []
    for sublist in matrix:
        list_of_matrix.extend(sublist)  # extends the list with the sublist (each element gets added to it)

    # Now we use the 9001 IQ way of testing if all numbers are inside:
    # If the set of the list is as long as the list itself, it means each element only appeared once.
    # if this is the same as the maximum, which should be 16, and the minimum is 1,
    # assuming every element is an integer, this means that all elements from 1 to 16 are present.
    # If a larger number was present, it's not equal to the length of the list.
    # So: if the minimum is 1, and all integers appear only once, and max == length: return True
    if len(set(list_of_matrix)) == len(list_of_matrix) == max(list_of_matrix) and min(list_of_matrix) == 1:
        return True
    return False


def check_sum_row(matrix):
    i = 0
    sums = [0, 0, 0, 0]
    for row in matrix:
        sums[i] = sum(row)
        i += 1  # I just spent 15 minutes rewriting 30% of my code to realise I forgot this.
        # Next time you see me, please hit me in the head as hard as you can.
    return sums


def check_sum_column(matrix):
    sums = [0, 0, 0, 0]
    # for each element index, we run through all rows, and add them up:
    # [[0, 1, 2]   first, we add the first elements of each list together
    #  [0, 1, 2]   then, we move to the next column: the second element of each list
    #  [0, 1, 2]]  so: sum each row, per column => for column in... before for row in...
    for col_ind in range(0, 4):  # this stands for the element in the sublist
        for row_ind in range(0, 4):  # this stands for the sublist in the matrix
            sums[col_ind] += matrix[row_ind][col_ind]
    return sums


def check_diagonals(matrix):
    sum_lr = 0
    for i in range(0, 4):
        sum_lr += matrix[i][i]
    sum_rl = 0
    for i in range(-4, 0):
        sum_rl += matrix[i][i]
    return [sum_lr, sum_rl, sum_rl, sum_rl]  # I can then first just check if all lists are the same


def check_magic_square(matrix):
    numbs = check_numbers(matrix)
    if not numbs:
        return False
    else:
        row_sums = check_sum_row(matrix)
        col_sums = check_sum_column(matrix)
        diags_sums = check_diagonals(matrix)
        if row_sums == col_sums == diags_sums:
            for num in row_sums[1:]:
                if num != row_sums[0]:
                    return False
        else:
            return False
    return True


# It's 1:40 AM please send help
please_work = [[1, 15, 14, 4], [12, 6, 7, 9], [8, 10, 11, 5], [13, 3, 2, 16]]
print(check_magic_square(please_work))
# Attempt 1: didn't work
# Attempt 2: check_rows is [34, 0, 0, 0], there's the b!tch that makes it turn "False"!
# Attempt 3: Fixed it. Works. God damn it. It's 2 AM. Why am I doing this?

# in hindsight, might've been able to use the functions we saw in P&O regarding matrices?
# Though, those probably used numpy/sympy specific arrays... Which are probably harder to work with