from utils import *

# `grid` is defined in the test code scope as the following:
# (note: changing the value here will _not_ change the test code)
# grid = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'

def grid_values(grid):
    """Convert grid string into {<box>: <value>} dict with '.' value for empties.

    Args:
        grid: Sudoku grid in string form, 81 characters long
    Returns:
        Sudoku grid in dictionary form:
        - keys: Box labels, e.g. 'A1'
        - values: Value in corresponding box, e.g. '8', or '.' if it is empty.
    """
    rows = 'ABCDEFGHI'
    cols = '123456789'
    def cross(a, b):
        return [s+t for s in a for t in b]
    boxes = cross(rows, cols)
    grid_dict = {}
    for i, value in enumerate(grid):
        if value == '.':
            value = '123456789'
        grid_dict[boxes[i]] = value
    return grid_dict

# or it can go like this:

def grid_values(grid):
    """Convert grid string into {<box>: <value>} dict with '.' value for empties.

    Args:
        grid: Sudoku grid in string form, 81 characters long
    Returns:
        Sudoku grid in dictionary form:
        - keys: Box labels, e.g. 'A1'
        - values: Value in corresponding box, e.g. '8', or '123456789' if it is empty.
    """
    values = []
    all_digits = '123456789'
    for c in grid:
        if c == '.':
            values.append(all_digits)
        elif c in all_digits:
            values.append(c)
    assert len(grid) == 81, "Input grid must be a string of length 81 (9x9)"
    return dict(zip(boxes, grid))

grid = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
display(grid_values(grid))

# my implementation
def eliminate(values):
    """Eliminate values from peers of each box with a single value.

    Go through all the boxes, and whenever there is a box with a single value,
    eliminate this value from the set of values of all its peers.

    Args:
        values: Sudoku in dictionary form.
    Returns:
        Resulting Sudoku in dictionary form after eliminating values.
    """
    rows = 'ABCDEFGHI'
    cols = '123456789'
    def cross(a, b):
        return [s+t for s in a for t in b]
    row_units = [cross(r, cols) for r in rows]
    column_units = [cross(rows, c) for c in cols]
    square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
    for k, v in values.items():
        if len(v) == 1:
            row_peers = row_units[rows.find(k[0])]
            col_peers = column_units[int(k[1])-1]
            square_peers = square_units[square_units.index([lst for lst in square_units if k in lst][0])]
            for key in row_peers:
                if len(values[key]) > 1:
                    values[key] = values[key].replace(str(v), '')
            for key in col_peers:
                if len(values[key]) > 1:
                    values[key] = values[key].replace(str(v), '')
            for key in square_peers:
                if len(values[key]) > 1:
                    values[key] = values[key].replace(str(v), '')
    return values

# Udacity implementation
def eliminate(values):
    """Eliminate values from peers of each box with a single value.

    Go through all the boxes, and whenever there is a box with a single value,
    eliminate this value from the set of values of all its peers.

    Args:
        values: Sudoku in dictionary form.
    Returns:
        Resulting Sudoku in dictionary form after eliminating values.
    """
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    for box in solved_values:
        digit = values[box]
        for peer in peers[box]:
            values[peer] = values[peer].replace(digit,'')
    return values
