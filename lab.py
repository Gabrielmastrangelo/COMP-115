# Exercise 1

def n_beads_triangular(n_rows):
    '''
    Computes the number of beads necessary to produce the pendant
    of the shape showed in Exercise 1.
    input:
        n_rows: number of the rows for the pendant
    output:
        n_beads: total number of beads necessary
    '''
    n_beads = 0
    for i in range(n_rows):
        row = i*2+1
        n_beads += row
    return n_beads

assert n_beads_triangular(1) == 1
assert n_beads_triangular(3) == 9

# Exercise 2

def n_beads_triangular_increase_by_two(n_rows):
    '''
    Computes the number of beads necessary to produce the pendant
    of the shape showed in Exercise 2.
    input:
        n_rows: number of the rows for the pendant
    output:
        n_beads: total number of beads necessary
    '''
    n_beads = 0
    for i in range(n_rows):
        row = i*4+1
        n_beads += row
    return n_beads

assert n_beads_triangular_increase_by_two(1) == 1
assert n_beads_triangular_increase_by_two(3) == 15

# Exercise 3

def n_beads_triangular_increase_by_n(n_rows, n):
    '''
    Computes the number of beads necessary to produce a pendant
    that increases the size by n pieces.
    input:
        n_rows: number of the rows for the pendant
    output:
        n_beads: total number of beads necessary
    '''
    n_beads = 0
    for i in range(n_rows):
        row = (i*2)*n+1
        n_beads += row
    return n_beads

assert n_beads_triangular_increase_by_n(3, 2) == 15
assert n_beads_triangular_increase_by_n(3, 1) == 9

# Exercise 4

def quadrangular_pendant_n_beads(nrows):
    '''
    Computes the number of beads necessary to produce the pendant
    of the shape showed in Exercise 4.
    input:
        n_rows: number of the rows for the pendant
    output:
        n_beads: total number of beads necessary
    '''
    top_part = nrows//2+nrows%2
    bottom_part = nrows//2

    n_beads_top = n_beads_triangular(top_part)
    n_beads_bottom = n_beads_triangular(bottom_part)

    n_beads = n_beads_top+n_beads_bottom

    return n_beads

assert quadrangular_pendant_n_beads(5) == 13
assert quadrangular_pendant_n_beads(1) == 1
assert quadrangular_pendant_n_beads(11) == 61

# Exercise 5

def n_beads_two_color_pendant(n_rows_inside, n_rows_outside):
    '''
    It computes the amount of beads necessary for creating the pendant,
    for both white and blues pieces.
    input: 
        n_rows_inside: number of rows for the inside pendant
        n_rows_outside: number of rows for the outside pendant
    output:
        tuple (white beads,  blue beads): it returns a tuple with the number of white and blue beads
    '''
    white = quadrangular_pendant_n_beads(n_rows_inside)
    blue = quadrangular_pendant_n_beads(n_rows_outside) - white

    return (white, blue)

assert n_beads_two_color_pendant(3, 3) == (5, 0)
assert n_beads_two_color_pendant(1, 3) == (1, 4)

# Exercise 6

def input_for_quadrangular_pendant_n_beads():
    '''
    It computes the number of white and blue beads, based in the 
    user input.
    output:
        tuple (white beads,  blue beads): it returns a tuple with the number of white and blue beads
    '''
    nrows_outside = 2
    nrows_inside = 2
    while nrows_outside%2 == 0:
        nrows_outside = int(input('Number of rows of the outside pattern: '))
        if nrows_outside == 1:
            break
    while nrows_inside%2 == 0:
        nrows_inside = int(input('Number of rows of the inside pattern: '))
        if nrows_inside == 1:
            break
    
    n_beads_color = n_beads_two_color_pendant(nrows_inside, nrows_outside)

    return n_beads_color

input_for_quadrangular_pendant_n_beads()


