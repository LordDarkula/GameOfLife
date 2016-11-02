from copy import deepcopy

row_of_three = {(0, 0):(True, False), (1, 0):(True, False), (2, 0):(True, False)}

def neighbors(location):
    """
    Returns list of locations
    of 8 adjacent squares given
    location of the cell.

    :type: location: tuple
    :rtype: list
    """
    x, y = location
    return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1),
            (x + 1, y + 1), (x - 1, y - 1), (x + 1, y - 1), (x - 1, y + 1)]

def number_neighbors(grid, location):
    """
    Calculates number of neighbors a
    cell has given the grid.

    :type: grid: dict
    :type: location: tuple
    :rtype: double
    """
    num_neighbors = 0

    for n_location in neighbors(location):
        if grid.get(n_location, (False, False))[0]:
            print(grid.get(n_location, (False, False)), "loc", n_location, num_neighbors)
            num_neighbors += 1
    if 2 <= num_neighbors <= 3:
        print(num_neighbors, location)

    return num_neighbors

def set_will_die(grid):
    """
    Sets second boolean in each tuple
    of each cell to whether the cell will
    die next turn. Also sets dead cells that will be
    alive next turn.

    :type: grid: dict
    """
    new_grid = {}
    for location, cell in grid.items():
        new_grid.update({location:(cell[0], 2 <= number_neighbors(grid, location) <= 3)})
        for n_location in neighbors(location):
            if number_neighbors(grid, n_location) == 3:
                print(n_location)
                new_grid.update({n_location:(False, True)})

    return new_grid

def update(grid):
    """
    Changes status of each cell to alive (True)
    or dead (False) depending on the second boolean
    in each cell.

    :type: grid: dict
    """
    new_grid = deepcopy(grid)
    for location, cell in grid.items():
        new_grid[location] = (cell[1], False)


    return new_grid

if __name__ == "__main__":
    print(row_of_three)
    row_of_three = set_will_die(row_of_three)
    print(row_of_three)
    row_of_three = update(row_of_three)
    print(row_of_three)